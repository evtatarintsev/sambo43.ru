from django.db import models
from django.utils.encoding import force_text
from django.utils.translation import ugettext_lazy as _
from string import punctuation

from mezzanine.galleries.models import BaseGallery
from mezzanine.core.models import Displayable
from mezzanine.core.models import Orderable
from mezzanine.core.fields import FileField


class Gallery(Displayable, BaseGallery):
    class Meta:
        verbose_name = _("Gallery")
        verbose_name_plural = _("Galleries")

    @models.permalink
    def get_absolute_url(self):
        return 'gallery_detail', [], {'slug': self.slug}

    def cover(self):
        return self.images.first()


class GalleryImage(Orderable):
    gallery = models.ForeignKey(Gallery, verbose_name=_('Галлерея'), related_name="images")
    file = FileField(_("File"), max_length=200, format="Image", upload_to='galleries/%Y/%m/%d')
    description = models.CharField(_("Description"), max_length=1000,blank=True)

    class Meta:
        verbose_name = _("Image")
        verbose_name_plural = _("Images")

    def __str__(self):
        return self.description

    def save(self, *args, **kwargs):
        """
        If no description is given when created, create one from the
        file name.
        """
        if not self.id and not self.description:
            name = force_text(self.file)
            name = name.rsplit("/", 1)[-1].rsplit(".", 1)[0]
            name = name.replace("'", "")
            name = "".join([c if c not in punctuation else " " for c in name])
            # str.title() doesn't deal with unicode very well.
            # http://bugs.python.org/issue6412
            name = "".join([s.upper() if i == 0 or name[i - 1] == " " else s
                            for i, s in enumerate(name)])
            self.description = name
        super(GalleryImage, self).save(*args, **kwargs)
