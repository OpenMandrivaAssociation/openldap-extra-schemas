#!/bin/bash

cat > schema.conf <<EOF
include /usr/share/openldap/schema/core.schema
include /usr/share/openldap/schema/cosine.schema
#include /usr/share/openldap/schema/nis.schema
include /usr/share/openldap/schema/inetorgperson.schema
EOF

echo "Note: skipping autofs,qmail and apple if present"
find SOURCES -name '*.schema'|sed -e 's/^/include /g'|grep -Ev '(autofs|apple|qmail)' >> schema.conf

rm -Rf slapd.d
mkdir slapd.d
/usr/sbin/slaptest -f schema.conf -F slapd.d || exit 1

pushd slapd.d/cn=config/cn=schema >/dev/null
perl -p0i -e 's/\n(structuralObjectClass|entryUUID|creatorsName|createTimestamp|entryCSN|modifiersName|modifyTimestamp)[^\n]*//g;s/cn(=|: ){\d+}/cn$1/g;s/^(dn: cn=\w+)\n/$1,cn=schema,cn=config\n/g' *.ldif

for i in cn=*;do mv $i ${i#*\}};done
popd >/dev/null

for i in slapd.d/cn=config/cn=schema/*.ldif
do
	schema=`basename $i`
	if ! diff -u SOURCES/$schema slapd.d/cn=config/cn=schema/$schema 
	then cp slapd.d/cn=config/cn=schema/$schema SOURCES/$schema
	fi
done
rm -Rf slapd.d
