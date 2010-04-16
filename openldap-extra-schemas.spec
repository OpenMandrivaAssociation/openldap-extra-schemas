%{!?ol_major: %global ol_major %nil}
%define schema_dir %{_datadir}/openldap%{ol_major}/schema

Name: openldap%{ol_major}-extra-schemas
Summary: Some extra schemas for OpenLDAP
Version: 1.3
Release: %mkrel 10
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
Source20: http://debian.jones.dk/debian/local/honda/pool-ldapv3/woody-jones/openldap2/schemas/dns.schema
Source21: http://debian.jones.dk/debian/local/honda/pool-ldapv3/woody-jones/openldap2/schemas/cron.schema
Source22: http://debian.jones.dk/debian/local/honda/pool-ldapv3/woody-jones/openldap2/schemas/qmailControl.schema
Source23: sudo.schema
Source24: dhcp.schema
Source25: autofs.schema

# LDIF versions of the same schema, created by:
# 1)Making a minimal config with schema and their dependencies
# 2)Running '/usr/sbin/slaptest -f /tmp/schema.conf -F /tmp/ldapns/' or similar
# 3)Cleaning up the file names, with e.g.: for i in cn=*;do mv $i ${i#*\}};done
# 4)Cleaning up the resulting ldif with e.g.: 
#  perl -p0e 's/\n(structuralObjectClass|entryUUID|creatorsName|createTimestamp|entryCSN|modifiersName|modifyTimestamp)[^\n]*//g;s/cn(=|: ){\d+}/cn$1/g;s/^(dn: cn=\w+)\n/$1,cn=schema,cn=config\n/g' *.ldif 
# specifically: remove operational attributes, clean names to match original schema
# names, add cn=schema,cn=config suffix required for adding over the wire

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
Source125: autofs.ldif



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
		%{SOURCE20} %{SOURCE21} %{SOURCE22} %{SOURCE23} %{SOURCE24} \
		%{SOURCE25} \
		%{SOURCE101}  %{SOURCE102}  %{SOURCE104}  %{SOURCE105} \
		%{SOURCE106}  %{SOURCE107}  %{SOURCE108}  %{SOURCE109}  %{SOURCE110} \
		%{SOURCE111} %{SOURCE113} %{SOURCE114} \
		%{SOURCE115} %{SOURCE118} \
		%{SOURCE121} %{SOURCE122} %{SOURCE123} %{SOURCE124} \
		%{SOURCE125} \
%{buildroot}%{schema_dir}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{schema_dir}/*.schema
%{schema_dir}/*.ldif

