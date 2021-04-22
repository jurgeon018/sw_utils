import ast
from decouple import config
from pathlib import Path
LOGIN_REDIRECT_URL = '/'
ACCOUNT_LOGOUT_ON_GET = True
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend'
)
INTERNAL_IPS = [
    '127.0.0.1',
]
ROOT_URLCONF       = 'sw_utils.urls'
WSGI_APPLICATION   = 'sw_utils.wsgi.application'
# BASE_DIR           = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
# BASE_DIR           = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
BASE_DIR = Path(__file__).resolve().parent.parent.parent

print(BASE_DIR)
ALLOWED_HOSTS      = ['*']
SECRET_KEY         = config('SECRET_KEY') 
DEBUG              = config('DEBUG', cast=bool)
STATICFILES_DIRS   = (BASE_DIR / "static", )
STATIC_ROOT        = BASE_DIR / "static_root"
MEDIA_ROOT         = BASE_DIR / "media"
STATIC_URL         = '/static/'
MEDIA_URL          = '/media/'
SITE_ID            = 1
# https://stackoverflow.com/questions/47585583/the-number-of-get-post-parameters-exceeded-settings-data-upload-max-number-field
# DATA_UPLOAD_MAX_NUMBER_FIELDS = 10240 
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
MIDDLEWARE = [
    'django.middleware.common.BrokenLinkEmailsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
    'django.contrib.redirects.middleware.RedirectFallbackMiddleware',
    
    'sw_utils.middleware.PutParsingMiddleware',
    'sw_utils.middleware.JSONParsingMiddleware',
    'sw_utils.middleware.DisableCSRF',
]
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': False,
        # 'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'sw_utils.context_processors.context',
            ],
            'loaders':[
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
                # "admin_tools.template_loaders.Loader",
            ]
        },
    },
]
# AUTH_PASSWORD_VALIDATORS = [
#     {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
#     {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
#     {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
#     {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'}
# ]
