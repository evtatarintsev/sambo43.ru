from django.conf.urls import url

from . import views


urlpatterns = [
    url('^photos/$', views.GalleryList.as_view(), name='gallery_list'),
    url('^photos/(?P<slug>.*)/$', views.GalleryDetail.as_view(), name='gallery_detail'),
]
