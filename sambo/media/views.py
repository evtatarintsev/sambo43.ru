from django.views.generic import ListView
from django.views.generic import DetailView

from .models import Gallery


class GalleryList(ListView):
    def get_queryset(self):
        return Gallery.objects.published(self.request.user)


class GalleryDetail(DetailView):
    def get_queryset(self):
        return Gallery.objects.published(self.request.user)

