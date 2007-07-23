%define schema_dir %{_datadir}/openldap/schema

Name: openldap-extra-schemas
Summary: Some extra schemas for OpenLDAP
Version: 1.2
Release: %mkrel 1
License: Several, see each file
Group: Databases
Source0: autofs.schema
# Get from qmail-ldap patch (http://www.nrg4u.com/qmail/)
Source1: qmail.schema
# from rfc2739, updated for schema correctness, used by evo for calendar attrs
Source2: calendar.schema
# from http://home.ntelos.net/%7Emasneyb/dhcp-3.0.5-ldap-patch
Source3: dhcp.schema
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
# from README.LDAP in sudo (pre-1.6.8) CVS:
Source12: sudo.schema
# from MIT krb5-1.6.x:
Source13: MIT-kerberos.schema
Source14: rfc2307bis.schema
# from openssh-lpk patch at http://dev.inversepath.com/trac/openssh-lpk
Source15: http://dev.inversepath.com/openssh-lpk/openssh-lpk_openldap.schema
Source16: http://dev.inversepath.com/openssh-lpk/openssh-lpk_sun.schema
URL: http://www.openldap.org
BuildRoot: %{_tmppath}/%{name}-%{version}-root-%(id -u -n)
BuildArch: noarch
Requires: openldap-servers
# add conflicts when the schemas have been removed from
# openldap-servers
#Conflicts: openldap-server <= 1:2.3.30-1nl

%description
This package contains some extra schemas for use with the OpenLDAP server.

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{schema_dir}
install -m 0644 %{_sourcedir}/*.schema %{buildroot}%{schema_dir}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{schema_dir}/*.schema

