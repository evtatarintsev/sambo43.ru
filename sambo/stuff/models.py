from django.db import models
from django.utils.translation import ugettext_lazy as _
from mezzanine.core.models import Displayable
from mezzanine.core.fields import FileField


class Rank(models.Model):
    name = models.CharField(_('Название'), max_length=50)

    class Meta:
        verbose_name = _('Разряд')
        verbose_name_plural = _('Разряды')
        ordering = ['name', ]

    def __str__(self):
        return self.name


class Person(Displayable):
    rank = models.ForeignKey(Rank, verbose_name=_('Разряд'))
    photo = FileField(_('Фото'), format='Image', upload_to='stuff')

    class Meta:
        verbose_name = _('Сотрудник')
        verbose_name_plural = _('Сотрудники')

    def __str__(self):
        return self.title



