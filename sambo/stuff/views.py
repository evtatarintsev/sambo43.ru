from django.views.generic import ListView
from django.views.generic import DetailView

from .models import Person


class PersonList(ListView):
    def get_queryset(self):
        return Person.objects.published(self.request.user)


class PersonDetail(DetailView):
    def get_queryset(self):
        return Person.objects.published(self.request.user)

