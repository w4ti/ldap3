from ldap3 import Server, Connection, ALL
server = Server('ipa.demo1.freeipa.org')
conn = Connection(server, 'uid=admin, cn=users, cn=accounts, dc=demo1, dc=freeipa, dc=org', 'Secret123', auto_bind=True)
print(conn.extend.standard.who_am_i())
print(server.schema)
print(server.info)
print(server.schema.object_classes['inetorgperson'])
print(server.schema.object_classes['organizationalperson'])
print(server.schema.object_classes['person'])
print(server.schema.object_classes['top'])

conn.search('dc=demo1, dc=freeipa, dc=org', '(&(objectclass=person)(uid=admin))', attributes=['sn', 'krbLastPwdChange', 'objectclass'])
entry = conn.entries[0]

print(entry)

# conn.add('ou=ldap3-tutorial, dc=demo1, dc=freeipa, dc=org', 'organizationalUnit')
# conn.add('cn=b.young,ou=ldap3-tutorial,dc=demo1,dc=freeipa,dc=org', 'inetOrgPerson', {'givenName': 'Beatrix', 'sn': 'Young', 'departmentNumber': 'DEV', 'telephoneNumber': 1111})
# conn.add('cn=j.smith,ou=ldap3-tutorial,dc=demo1,dc=freeipa,dc=org', 'inetOrgPerson', {'givenName': 'John', 'sn': 'Smith', 'departmentNumber': 'DEV', 'telephoneNumber': 2222})
# conn.add('cn=m.smith,ou=ldap3-tutorial,dc=demo1,dc=freeipa,dc=org', 'inetOrgPerson', {'givenName': 'Marianne', 'sn': 'Smith', 'departmentNumber': 'QA',  'telephoneNumber': 3333})
# conn.add('cn=quentin.cat,ou=ldap3-tutorial,dc=demo1,dc=freeipa,dc=org', 'inetOrgPerson', {'givenName': 'Quentin', 'sn': 'Cat', 'departmentNumber': 'CC', 'telephoneNumber': 4444})
conn.search('ou=ldap3-tutorial,dc=demo1,dc=freeipa,dc=org', '(cn=*)', attributes=['objectclass'])
print(conn.entries)