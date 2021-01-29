priority_third_party = [
    'corsheaders',
    'dal', 'dal_select2',
    'admin_auto_filters',
    'modeltranslation',
]
django_contrib = [
    'django.contrib.auth',
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.redirects',
    'django.contrib.flatpages',
    'django.contrib.sitemaps',
]
third_party = [
    "mptt",
    "tinymce",
    'ckeditor', 'ckeditor_uploader',
    'allauth','allauth.account','allauth.socialaccount', 'allauth.socialaccount.providers.google',
    'import_export',
    'rosetta',
    'colorfield',
    'adminsortable2',
    "rest_framework", 'rest_framework.authtoken', 'rest_framework_simplejwt',
    "rangefilter",
    'debug_toolbar',
    'nested_admin',
]
box_core = [
    'sw_utils',
    'sw_modelclone',
    'sw_global_config',
    'sw_solo',
    'sw_watermarker',
    'sw_model_search',
    'sw_currency',
    'sw_content',
    'sw_contact_form',
    # 'sw_auth',
]
delivery = [
    'sw_delivery',
    'sw_novaposhta',
    'sw_delivery_auto',
    'sw_sat',
]
shop = [
    'sw_catalog',
    'sw_order',
    'sw_cart',
    'sw_customer',
]
payment = [
    'sw_liqpay',
    'sw_wayforpay',
    'sw_interkassa',
]
blog = [
    'sw_blog',
]
INSTALLED_APPS  = [
    *priority_third_party,
    *django_contrib,
    *third_party,
    *box_core,
    *delivery,
    *shop,
    *payment,
    *blog,
]

