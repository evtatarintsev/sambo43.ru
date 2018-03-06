import requests
import functools
from django.db import models
from django.utils.translation import ugettext_lazy as _
from mezzanine.core.models import Displayable
from mezzanine.core.fields import FileField
from mezzanine.core.fields import RichTextField


class Hall(Displayable):
    photo = FileField(_('Фото'), format='Image', upload_to='halls', help_text=_('Пропорционально 1000x300'))
    address = models.CharField(_('Адрес'), max_length=100, help_text=_('Полный адрес с указанием города'))
    phone_no = models.CharField(_('Телефон'), max_length=30, null=True, blank=True)
    content = RichTextField(_('Текст'))
    gallery = models.ForeignKey('media.Gallery', verbose_name=_('Галлерея'), null=True, blank=True)
    coaches = models.ManyToManyField('stuff.Person', verbose_name=_('Тренера'), blank=True)

    class Meta:
        verbose_name = _('Зал')
        verbose_name_plural = _('Залы')

    def __str__(self):
        return self.title

    @models.permalink
    def get_absolute_url(self):
        return 'hall_detail', [], {'slug': self.slug}

    @functools.lru_cache()
    def get_pos(self):
        geocoder_url = 'https://geocode-maps.yandex.ru/1.x/'
        try:
            response = requests.get(geocoder_url, {'geocode': self.address, 'format': 'json'}, timeout=2).json()
            pos = response['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos']
        except:
            return None

        return pos.split()[::-1]

