from django.conf.urls import include, url
from django.contrib import admin

import mezzanine.pages.views


admin.autodiscover()


urlpatterns = [
    url('^admin/', include(admin.site.urls)),
    url('^$', mezzanine.pages.views.page, {'slug': '/'}, name='home'),
    url('^stuff/', include('sambo.stuff.urls')),
    url('^halls/', include('sambo.halls.urls')),
    url('^', include('sambo.media.urls')),
    url('^', include('mezzanine.urls')),
]

handler404 = 'mezzanine.core.views.page_not_found'
handler500 = 'mezzanine.core.views.server_error'
