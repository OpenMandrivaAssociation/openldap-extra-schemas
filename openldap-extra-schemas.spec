%{!?ol_major: %global ol_major %nil}
%define schema_dir %{_datadir}/openldap%{ol_major}/schema

Name: openldap%{ol_major}-extra-schemas
Summary: Some extra schemas for OpenLDAP
Version: 1.3
Release: %mkrel 14
License: Several, see each file
Group: Databases
Source0: autofs.schema
# Get from qmail-ldap patch (http://www.nrg4u.com/qmail/)
Source1: qmail.schema
# from rfc2739, updated for schema correctness, used by evo for calendar attrs
Source2: calendar.schema
# from bind sdb_ldap page:http://www.venaas.no/ldap/bind-sdb/dnszone-schema.txt
Source4: dnszone.schema
# from evolution package
Source5: evolutionperson.schema
Source6: kerberosobject.schema
Source7: kolab.schema
# from Heimdal kerberos sources
Source8: krb5-kdc.schema
Source9: ldapns.schema
Source10: rfc822-MailMember.schema
# Get from samba source, examples/LDAP/samba.schema
Source11: samba.schema
# from MIT krb5-1.6.x:
Source13: MIT-kerberos.schema
Source14: rfc2307bis.schema
# from openssh-lpk patch at http://dev.inversepath.com/trac/openssh-lpk
Source15: http://dev.inversepath.com/openssh-lpk/openssh-lpk_openldap.schema
# See http://mattfleming.com/node/190
Source17: http://mattfleming.com/files/active/0/apple.schema
# from http://cvs.pld.org.pl/SOURCES/openldap-dhcp.schema
Source18: http://debian.jones.dk/debian/local/honda/pool-ldapv3/woody-jones/openldap2/schemas/netscape-profile.schema
Source19: http://debian.jones.dk/debian/local/honda/pool-ldapv3/woody-jones/openldap2/schemas/trust.schema
# incomplete:
#Source20: http://debian.jones.dk/debian/local/honda/pool-ldapv3/woody-jones/openldap2/schemas/dns.schema
Source21: http://debian.jones.dk/debian/local/honda/pool-ldapv3/woody-jones/openldap2/schemas/cron.schema
Source22: http://debian.jones.dk/debian/local/honda/pool-ldapv3/woody-jones/openldap2/schemas/qmailControl.schema
Source23: sudo.schema
Source24: dhcp.schema
# From courier-authlib-ldap
Source26: authldap.schema

# LDIF versions of the same schema, created by:
# 1)Making a minimal config with schema and their dependencies
# 2)Running '/usr/sbin/slaptest -f /tmp/schema.conf -F /tmp/ldapns/' or similar
# 3)Cleaning up the file names, with e.g.: for i in cn=*;do mv $i ${i#*\}};done
# 4)Cleaning up the resulting ldif with e.g.: 
#  perl -p0e 's/\n(structuralObjectClass|entryUUID|creatorsName|createTimestamp|entryCSN|modifiersName|modifyTimestamp)[^\n]*//g;s/cn(=|: ){\d+}/cn$1/g;s/^(dn: cn=\w+)\n/$1,cn=schema,cn=config\n/g' *.ldif 
# specifically: remove operational attributes, clean names to match original schema
# names, add cn=schema,cn=config suffix required for adding over the wire

# This is now done in the script below (catered for use in svn)
Source99: convert.sh

Source100: autofs.ldif
Source101: qmail.ldif
Source102: calendar.ldif
Source104: dnszone.ldif
Source105: evolutionperson.ldif
Source106: kerberosobject.ldif
Source107: kolab.ldif
Source108: krb5-kdc.ldif
Source109: ldapns.ldif
Source110: rfc822-MailMember.ldif
Source111: samba.ldif
Source113: MIT-kerberos.ldif
Source114: rfc2307bis.ldif
Source115: openssh-lpk_openldap.ldif
#Source117: apple.ldif
Source118: netscape-profile.ldif
#Source119: trust.ldif
#Source120: dns.ldif
Source121: cron.ldif
Source122: qmailControl.ldif
Source123: sudo.ldif
Source124: dhcp.ldif
Source126: authldap.ldif


URL: http://www.openldap.org
BuildRoot: %{_tmppath}/%{name}-%{version}-root-%(id -u -n)
BuildArch: noarch
Requires: openldap%{ol_major}-servers
# add conflicts when the schemas have been removed from
# openldap-servers
#Conflicts: openldap-server <= 1:2.3.30-1nl
Conflicts: openldap%{ol_major}-servers < 2.4.17

%description
This package contains some extra schemas for use with the OpenLDAP server.

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{schema_dir}
#install -m 0644 %{_sourcedir}/*.schema %{buildroot}%{schema_dir}
install -m 0644 %{SOURCE1}  %{SOURCE2}  %{SOURCE4}  %{SOURCE5} \
		%{SOURCE6}  %{SOURCE7}  %{SOURCE8}  %{SOURCE9}  %{SOURCE10} \
		%{SOURCE11} %{SOURCE13} %{SOURCE14} \
		%{SOURCE15} %{SOURCE17} %{SOURCE18} %{SOURCE19} \
		%{SOURCE21} %{SOURCE22} %{SOURCE23} %{SOURCE24} \
		%{SOURCE26} \
		%{SOURCE101}  %{SOURCE102}  %{SOURCE104}  %{SOURCE105} \
		%{SOURCE106}  %{SOURCE107}  %{SOURCE108}  %{SOURCE109}  %{SOURCE110} \
		%{SOURCE111} %{SOURCE113} %{SOURCE114} \
		%{SOURCE115} %{SOURCE118} \
		%{SOURCE121} %{SOURCE122} %{SOURCE123} %{SOURCE124} \
		%{SOURCE126} \
%{buildroot}%{schema_dir}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{schema_dir}/*.schema
%{schema_dir}/*.ldif



%changelog
* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 1.3-13mdv2011.0
+ Revision: 666956
- mass rebuild

  + Buchan Milne <bgmilne@mandriva.org>
    - Update ldapns.schema to the version used by OpenLDAPs nssov overlay
    - Fix schema conversion script (exit on slaptest failure, skip qmail schema for now)

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 1.3-12mdv2011.0
+ Revision: 607019
- rebuild

  + Buchan Milne <bgmilne@mandriva.org>
    - Add authldap.schema (from courier-authlib-ldap) and authldap.ldif (convert from it)

* Fri Jun 11 2010 Buchan Milne <bgmilne@mandriva.org> 1.3-11mdv2010.1
+ Revision: 547866
- Update dnszone and dhcp schema (mmc needs newer versions)
- Drop dns.schema, it is incomplete and unused
- Add script to automate schema to ldif conversion
- Comment namedObject in rfc2307bis.schema, conflicts with kolab
- Sync other minor schema changes to ldif

* Fri Apr 16 2010 Buchan Milne <bgmilne@mandriva.org> 1.3-10mdv2010.1
+ Revision: 535500
- Ship LDIF format versions suitable for use with back-config after conversion
- Drop openssh-lpk_sun.schema, we already have an LDIF version for OpenLDAP
- Fix schema errors in netscape-profile and qmailControl

* Mon Jan 04 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.3-9mdv2010.1
+ Revision: 486148
- update LPK schemas (attributes are now optional)

  + Buchan Milne <bgmilne@mandriva.org>
    - Version openldap-servers require by ol_major

* Sun Jul 19 2009 Buchan Milne <bgmilne@mandriva.org> 1.3-7mdv2010.0
+ Revision: 397984
- Add autofs schema

* Sun Jul 19 2009 Buchan Milne <bgmilne@mandriva.org> 1.3-6mdv2010.0
+ Revision: 397916
- Migrate the rest of the non-core schema out
- Fix versioning

* Sun Jul 19 2009 Buchan Milne <bgmilne@mandriva.org> 1.3-5mdv2010.0
+ Revision: 397235
- Allow building a package for versioned openldap-servers package
- Conflict with openldap-servers which ships the same schema files

* Fri Dec 05 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.3-4mdv2009.1
+ Revision: 310796
- drop schemas conflicting with openldap--server package (fix #38971):
- sudo schema (only cosmetics differences)
- dhcp schema (actual differences, but the alternate one is already shipped in dhcp server package)

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Buchan Milne <bgmilne@mandriva.org>
    - add hdb.schema from http://people.su.se/~lha/patches/heimdal/hdb.schema
    - Add apple.schema from http://mattfleming.com/node/190

  + Andreas Hasenack <andreas@mandriva.com>
    - fix indentation error in sudo.schema

* Mon Jul 23 2007 Andreas Hasenack <andreas@mandriva.com> 1.2-1mdv2008.0
+ Revision: 54799
- updated dhcp schema from version 3.0.5 of the patch

* Fri Jun 01 2007 Andreas Hasenack <andreas@mandriva.com> 1.1-1mdv2008.0
+ Revision: 34339
- added lpk schemas (openssh + ldap)

* Thu May 03 2007 Andreas Hasenack <andreas@mandriva.com> 1.0-2mdv2008.0
+ Revision: 22052
- added rfc2307bis.schema


* Wed Jan 03 2007 Andreas Hasenack <andreas@mandriva.com> 1.0-1mdv2007.0
+ Revision: 103813
- Import openldap-extra-schemas

