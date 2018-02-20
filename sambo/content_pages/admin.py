from django.contrib import admin
from mezzanine.pages.admin import PageAdmin
from mezzanine.core.admin import TabularDynamicInlineAdmin

from .models import HomePage
from .models import Slide


class SlideInline(TabularDynamicInlineAdmin):
    model = Slide
    extra = 0


@admin.register(HomePage)
class HomePageAdmin(PageAdmin):
    inlines = (SlideInline, )
