from django.db import models
from django.utils.translation import ugettext_lazy as _

from mezzanine.pages.models import Page
from mezzanine.core.fields import FileField
from mezzanine.core.fields import RichTextField
from mezzanine.core.models import Orderable

from sambo.stuff.models import Person


class HomePage(Page):
    content_title = models.CharField('Заголовок контента', max_length=100)
    content = RichTextField('Текст')

    # Сниппет с тренером или спортсменом
    person = models.ForeignKey(Person, verbose_name=_('Сотрудник'), null=True, blank=True,
                               help_text=_('Показывается на странице, если не выбрано, будет показан случайный сотрудник'))
    person_text = models.CharField(_('Текст на сотруднике'), max_length=50, null=True, blank=True)
    person_date = models.DateField(_('Дата на сотруднике'), null=True, blank=True)

    class Meta:
        verbose_name = 'Главная страница'

    def get_template_name(self):
        return 'index.html'

    def slider(self):
        return self.slide_list.filter(published=True)


class Slide(Orderable):
    page = models.ForeignKey(Page, verbose_name='Слайдер', related_name='slide_list')
    image = FileField(verbose_name='Изображение',
                      upload_to='slider', format="Image", max_length=255)
    image_mobile = FileField(verbose_name='Изображение mobile', null=True, blank=True,
                             upload_to='slider', format="Image", max_length=255)

    link = models.URLField('Ссылка', null=True, blank=True)

    published = models.BooleanField('Опубликовано', default=True)

    class Meta:
        verbose_name = 'Слайд'
        verbose_name_plural = 'Слайды'




