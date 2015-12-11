"""
Definition of urls for Jolley.
"""

from datetime import datetime
import sys

from django.conf import settings
from django.conf.urls import include
from django.conf.urls import patterns
from django.conf.urls import url

from mviews.router.routes import routes

# Uncomment the next lines to enable the admin:
# from django.conf.urls import include
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'', include(routes.urls)),
)

if 'linux' not in sys.platform.lower():
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)