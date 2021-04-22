from ._django import BASE_DIR
from decouple import config

DB = config('DB', None)
if DB == 'postgres':
    default = {
        'ENGINE':    'django.db.backends.postgresql_psycopg2',
        'NAME':      config('POSTGRES_DB_NAME'),
        'USER' :     config('POSTGRES_DB_USERNAME'),
        'PASSWORD' : config('POSTGRES_DB_PASSWORD'),
        'HOST' :     config('POSTGRES_DB_HOST', '127.0.0.1'),
        'PORT' :     config('POSTGRES_DB_PORT', '5432'),
    }
elif DB == 'mysql':
    default = {}
else:
    default = {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
DATABASES = {
    'default': default,
}



