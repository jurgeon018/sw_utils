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
    'sw_utils.sw_global_config',
    'sw_utils.sw_solo',
    'sw_utils.sw_watermarker',
    'sw_utils.sw_model_search',
    'sw_utils.sw_currency',
    'sw_utils.sw_content',
    'sw_utils.sw_contact_form',
    'sw_utils.sw_auth',
]
box_delivery = [
    'sw_delivery',
    'sw_novaposhta',
    'sw_delivery_auto',
    'sw_sat',
]
box_shop = [
    'sw_shop',      # !! не забирай це, бо тоді з адмінки пропадуть блочки з django-admin-tools
    'sw_shop.sw_catalog',
    'sw_shop.sw_order',
    'sw_shop.sw_cart',
    'sw_shop.sw_customer',
]
box_payment = [
    'sw_payment',   # !! не забирай це, бо тоді з адмінки пропадуть блочки з django-admin-tools
    'liqpay',
    'wayforpay',
    'interkassa',
]
box_blog = [
    'sw_blog',
]
INSTALLED_APPS  = [
    *priority_third_party,
    *django_contrib,
    *third_party,
    *box_core,
    *box_delivery,
    *box_shop,
    *box_payment,
    *box_blog,
]

