db = 'bbvasuiza-14-0-2418309-det-2101904'

info = {
	'url': 'https://{db}.dev.odoo.com'.format(db=db),
	'db': db,
	'username': 'admin',
	'password': 'admin',
}

print(info)

import xmlrpc.client

url, db, username, password = \
    info['url'], info['db'], info['username'], info['password']

# public
common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
print(common.version())

# authenticate
uid = common.authenticate(db, username, password, {})
print(uid)

models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))

# search_read
res = models.execute_kw(db, uid, password,
    'res.partner', 'search_read',
    [[], ['name', 'display_name', 'business_industry']], {'limit': 5})

print(res)

# list fields of the model
res = models.execute_kw(
    db, uid, password, 'res.partner', 'fields_get',
    [], {'attributes': ['string', 'help', 'type']})

# print(res)

# create record
id = models.execute_kw(db, uid, password, 'res.partner', 'create', [{
    'name': "New Partner",
}])
