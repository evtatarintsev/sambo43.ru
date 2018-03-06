from django.conf.urls import url

from . import views


urlpatterns = [
    url('^$', views.HallList.as_view(), name='hall_list'),
    url('^(?P<slug>.*)/$', views.HallDetail.as_view(), name='hall_detail'),
]
