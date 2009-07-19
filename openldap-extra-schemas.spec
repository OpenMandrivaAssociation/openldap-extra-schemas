%{!?ol_major: %global ol_major %nil}
%define schema_dir %{_datadir}/openldap%{ol_major}/schema

Name: openldap%{ol_major}-extra-schemas
Summary: Some extra schemas for OpenLDAP
Version: 1.3
Release: %mkrel 7
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
Source16: http://dev.inversepath.com/openssh-lpk/openssh-lpk_sun.schema
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

URL: http://www.openldap.org
BuildRoot: %{_tmppath}/%{name}-%{version}-root-%(id -u -n)
BuildArch: noarch
Requires: openldap-servers
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
		%{SOURCE15} %{SOURCE16} %{SOURCE17} %{SOURCE18} %{SOURCE19} \
		%{SOURCE20} %{SOURCE21} %{SOURCE22} %{SOURCE23} %{SOURCE24} \
		%{SOURCE25} \
%{buildroot}%{schema_dir}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{schema_dir}/*.schema

