from ._django import BASE_DIR, os, config 

if config('DB') == 'postgres':
    default = {
        'ENGINE':    'django.db.backends.postgresql_psycopg2',
        'NAME':      config('POSTGRES_DB_NAME'),
        'USER' :     config('POSTGRES_DB_USERNAME'),
        'PASSWORD' : config('POSTGRES_DB_PASSWORD'),
        'HOST' :     config('POSTGRES_DB_HOST') or '127.0.0.1',
        'PORT' :     config('POSTGRES_DB_PORT') or '5432',
    }
elif config('DB') == 'mysql':
    default = {}
else:
    default = {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
DATABASES = {
    'default': default,
}



