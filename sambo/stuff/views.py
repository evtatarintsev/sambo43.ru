from django.views.generic import ListView
from django.views.generic import DetailView
from mezzanine.core.models import CONTENT_STATUS_PUBLISHED
from .models import Person


class PersonList(ListView):
    def get_queryset(self):
        return Person.objects.filter(status=CONTENT_STATUS_PUBLISHED)


class PersonDetail(DetailView):
    def get_queryset(self):
        return Person.objects.filter(status=CONTENT_STATUS_PUBLISHED)

