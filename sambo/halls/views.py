from django.views.generic import ListView
from django.views.generic import DetailView

from .models import Hall


class HallList(ListView):
    def get_queryset(self):
        return Hall.objects.published(self.request.user)


class HallDetail(DetailView):
    def get_queryset(self):
        return Hall.objects.published(self.request.user)

    def get_context_data(self, **kwargs):
        ctx = super(HallDetail, self).get_context_data(**kwargs)
        ctx['hall_pos'] = self.object.get_pos()
        return ctx

