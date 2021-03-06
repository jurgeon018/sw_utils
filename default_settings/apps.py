# crispy forms
CRISPY_TEMPLATE_PACK = 'bootstrap4'

# corsheaders
CORS_ORIGIN_ALLOW_ALL = True 

# ckeditor
CKEDITOR_UPLOAD_PATH = ''

# django debug toolbar
DEBUG_TOOLBAR_PANELS = [
    'debug_toolbar.panels.versions.VersionsPanel',
    'debug_toolbar.panels.timer.TimerPanel',
    'debug_toolbar.panels.settings.SettingsPanel',
    'debug_toolbar.panels.headers.HeadersPanel',
    'debug_toolbar.panels.request.RequestPanel',
    'debug_toolbar.panels.sql.SQLPanel',
    'debug_toolbar.panels.staticfiles.StaticFilesPanel',
    'debug_toolbar.panels.templates.TemplatesPanel',
    'debug_toolbar.panels.cache.CachePanel',
    'debug_toolbar.panels.signals.SignalsPanel',
    'debug_toolbar.panels.logging.LoggingPanel',
    'debug_toolbar.panels.redirects.RedirectsPanel',
    'debug_toolbar.panels.profiling.ProfilingPanel',
]


DEBUG_TOOLBAR_CONFIG = {
    # # Toolbar options
    # 'RESULTS_CACHE_SIZE': 3,
    # 'SHOW_COLLAPSED': True,
    # # Panel options
    # 'SQL_WARNING_THRESHOLD': 100,   # milliseconds
}

# django rest framework

# 'DEFAULT_AUTHENTICATION_CLASSES'= (
#     # 'rest_framework.authentication.SessionAuthentication',
#     'sw_utils.authentication.CsrfExemptSessionAuthentication',
#     'rest_framework.authentication.BasicAuthentication'
# ),

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ),
    # 'DATETIME_FORMAT': "%Y-%m-%d - %H:%M:%S", 
    'DATETIME_FORMAT': "%d-%m-%Y %H:%M",
}

# rest

SIMPLE_JWT = {
   'AUTH_HEADER_TYPES': ('JWT',),
}
DJOSER = {
    'PASSWORD_RESET_CONFIRM_URL': 'auth/password/reset/confirm/{uid}/{token}',
    'USERNAME_RESET_CONFIRM_URL': '#/username/reset/confirm/{uid}/{token}',
    'ACTIVATION_URL': '#/activate/{uid}/{token}',
    'SEND_ACTIVATION_EMAIL': True,
    'SERIALIZERS': {},
}
