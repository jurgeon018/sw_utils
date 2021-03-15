from django.contrib import admin
from django.urls import path, include 
from django.views.i18n import JavaScriptCatalog as js_cat
from django.contrib.sitemaps.views import sitemap
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from django.conf import settings
from django.views.decorators.cache import cache_page
from django.apps import apps
from django.conf import settings
from importlib import import_module
from importlib.util import find_spec
from sw_utils.views import robots, set_lang, testmail
from sw_utils.sitemaps import StaticSitemap
from . import settings as core_settings
from .views import *

from importlib import import_module
from filebrowser.sites import site

admin.site.site_header = "STARWAY CMS"
admin.site.site_title  = "STARWAY CMS"
admin.site.index_title = "STARWAY CMS"

handler400 = core_settings.HANDLER_400
handler403 = core_settings.HANDLER_403
handler404 = core_settings.HANDLER_404
handler500 = core_settings.HANDLER_500


def generate_sitemaps():
  sitemaps = {
      'static':  StaticSitemap,
  }
  for project_name, path_name in settings.SITEMAP_PATHS.items():
    try:
      p, m      = path_name.rsplit('.', 1)
      mod       = import_module(p)
      met       = getattr(mod, m)
      sitemaps.update({
        project_name:met
      })
    except:
      pass
  # if 'sw_utils.sw_content' in settings.INSTALLED_APPS:
  #   from sw_content.sitemaps import PageSitemap
  #   sitemaps.update({
  #     'pages':PageSitemap,
  #   })
  if 'sw_catalog' in settings.INSTALLED_APPS:
    from sw_catalog.sitemaps import ItemSitemap, ItemCategorySitemap
    sitemaps.update({
    'items':           ItemSitemap,
    'item_categories': ItemCategorySitemap,
    })
  if 'sw_blog' in settings.INSTALLED_APPS:
    from sw_blog.sitemaps import PostSitemap, PostCategorySitemap
    sitemaps.update({
      'posts':           PostSitemap, 
      'post_categories': PostCategorySitemap, 
    })

  return sitemaps

# def get_box_apps():
#   box_apps = [
#     # 'sw_utils',
#     'sw_modelclone',
#     'sw_global_config',
#     'sw_solo',
#     'sw_watermarker',
#     'sw_model_search',
#     'sw_currency',
#     'sw_content',
#     'sw_contact_form',
#     'sw_auth',
#     'sw_delivery',
#     'sw_novaposhta',
#     'sw_delivery_auto',
#     'sw_sat',
#     'sw_catalog',
#     'sw_order',
#     'sw_cart',
#     'sw_customer',
#     'sw_liqpay',
#     'sw_wayforpay',
#     'sw_interkassa',
#     'sw_blog',
#   ]
#   return box_apps

def generate_urlpatterns():
  PROJECT_CORE              = [path('', include(url)) for url in core_settings.PROJECT_CORE_URLS]
  PROJECT_CORE_MULTILINGUAL = [path('', include(url)) for url in core_settings.PROJECT_CORE_MULTILINGUAL_URLS]
  for i in PROJECT_CORE_MULTILINGUAL:
    print(i)

  excluded_apps = [
    'sw_utils', 
  ]
  box_apps = []
  for app in settings.INSTALLED_APPS:
    if app.startswith('sw_') and app not in excluded_apps:
    # if app in get_box_apps() and app not in excluded_apps:
      box_apps.append(app)

  box = []
  box_multilingual = []

  for app in box_apps:
    urls_path = f'{app}.urls'
    if find_spec(urls_path) is not None:
      url = path('', include(urls_path))
      box.append(url)
        
  for app in box_apps:
    urls_path = f'{app}.multilingual_urls'
    if find_spec(urls_path) is not None:
      url = path('', include(urls_path))
      box.append(url)

  multilingual = i18n_patterns(
    path('admin/',    admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('rosetta/',  include('rosetta.urls')),
    path(core_settings.URL_400, custom_bad_request),
    path(core_settings.URL_403, custom_permission_denied),
    path(core_settings.URL_404, custom_page_not_found),
    path(core_settings.URL_500, custom_server_error),
    *box_multilingual,
    *PROJECT_CORE_MULTILINGUAL,
    prefix_default_language=False,
  )
  static_urlpatterns = []

  # if settings.DEBUG == True:
  static_urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
  static_urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
  urlpatterns = [
    *PROJECT_CORE,
    *multilingual,
    *box,
    *static_urlpatterns,
    path('sitemap.xml/',     sitemap, {'sitemaps':generate_sitemaps()}, name='sitemap'),
    path('robots.txt/',      robots,           name='robots'),
    path('i18n/',            include('django.conf.urls.i18n')),
    path('set_lang/<new_lang>/', set_lang,     name="set_lang"),
    path('jsi18n/',          js_cat.as_view(), name='javascript-catalog'),
    path('tinymce/',         include('tinymce.urls')),
    path('api-auth/',        include('rest_framework.urls', namespace='rest_framework')),
    path('_nested_admin/',   include('nested_admin.urls')),
    path('filebrowser/',     site.urls),
  ]

  if core_settings.DJANGO_DEBUG_TOOLBAR_ON and settings.DEBUG:
      import debug_toolbar
      urlpatterns.extend([
          path('__debug__/', include(debug_toolbar.urls)),
      ])

  return urlpatterns



urlpatterns = generate_urlpatterns()
# for i in urlpatterns:
#   print(i) 
