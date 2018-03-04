from django.conf.urls import url

from . import views


urlpatterns = [
    url('^$', views.PersonList.as_view(), name='person_list'),
    url('^(?P<slug>.*)/$', views.PersonDetail.as_view(), name='person_detail'),
]
