from django.db import models
from django.utils.translation import ugettext_lazy as _
from mezzanine.core.models import Displayable
from mezzanine.core.fields import FileField
from mezzanine.core.fields import RichTextField


class Rank(models.Model):
    name = models.CharField(_('Название'), max_length=50)

    class Meta:
        verbose_name = _('Разряд')
        verbose_name_plural = _('Разряды')
        ordering = ['name', ]

    def __str__(self):
        return self.name


class Person(Displayable):
    POSITIONS = (
        (0, _('Тренер')),
        (10, _('Спортсмен')),
        (20, _('Президент федерации')),
        (30, _('Вице президент федерации')),
    )
    position = models.PositiveIntegerField(_('Должность'), default=0, choices=POSITIONS)
    rank = models.ForeignKey(Rank, verbose_name=_('Разряд'))
    photo = FileField(_('Фото'), format='Image', upload_to='stuff')
    phone_no = models.CharField(_('Телефон'), max_length=30, null=True, blank=True)
    content = RichTextField(_('Тескт'))
    gallery = models.ForeignKey('media.Gallery', verbose_name=_('Галлерея'), null=True, blank=True)

    class Meta:
        verbose_name = _('Сотрудник')
        verbose_name_plural = _('Сотрудники')

    def __str__(self):
        return self.title

    @models.permalink
    def get_absolute_url(self):
        return 'person_detail', [], {'slug': self.slug}


