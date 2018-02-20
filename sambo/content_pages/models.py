from django.db import models
from mezzanine.pages.models import Page
from mezzanine.core.fields import FileField
from mezzanine.core.fields import RichTextField
from mezzanine.core.models import Orderable


class HomePage(Page):
    content_title = models.CharField('Заголовок контента', max_length=100)
    content = RichTextField('Текст')

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




