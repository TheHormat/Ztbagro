from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from django.views.generic.base import TemplateView
from django.conf.urls.i18n import i18n_patterns
from teserrufat.sitemaps import *

from teserrufat.views import set_language

sitemaps = {
    "services": ServiceSiteMap,
    "static_sitemap": Static_Sitemap,
}

urlpatterns = [
    path('akm1n/', admin.site.urls),
    path("", include("teserrufat.urls")),
    path('rosetta/', include('rosetta.urls')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path("robots.txt", TemplateView.as_view(template_name="robots.txt", content_type="text/plain")),
    path('set_language/<str:lang_code>/', set_language, name="set_lang"),
    path('i18n/', include('django.conf.urls.i18n')),
]

urlpatterns = [
    *i18n_patterns(*urlpatterns, prefix_default_language=False),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
