import os

# We want to seamlessy run our API both locally and on Heroku. If running on
# Heroku, sensible DB connection settings are stored in environment variables.
#MONGO_HOST = os.environ.get('MONGO_HOST', 'localhost')
#MONGO_PORT = os.environ.get('MONGO_PORT', 27017)
#MONGO_USERNAME = os.environ.get('MONGO_USERNAME', 'user')
#MONGO_PASSWORD = os.environ.get('MONGO_PASSWORD', 'user')
#MONGO_DBNAME = os.environ.get('MONGO_DBNAME', 'evedemo')

X_DOMAINS = '*'


# Enable reads (GET), inserts (POST) and DELETE for resources/collections
# (if you omit this line, the API will default to ['GET'] and provide
# read-only access to the endpoint).
RESOURCE_METHODS = ['GET', 'POST', 'DELETE']

# Enable reads (GET), edits (PATCH) and deletes of individual items
# (defaults to read-only item access).
ITEM_METHODS = ['GET', 'PATCH', 'DELETE']

# We enable standard client cache directives for all resources exposed by the
# API. We can always override these global settings later.
CACHE_CONTROL = ' '
CACHE_EXPIRES = 0

PAGINATION = True

noise = {
	'item_title': 'noise',

    'additional_lookup': {
        'url': 'regex("[\d]+")',
        'field': 'point_id'
    },

	'schema': {
        'x': {'type': 'integer'},
        'y': {'type': 'integer'},
        'value': {'type': 'integer'},
        'point_id': {'type': 'integer'}
	}
}

# The DOMAIN dict explains which resources will be available and how they will
# be accessible to the API consumer.
DOMAIN = {
    'noise': noise,
}