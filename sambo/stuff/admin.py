from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from mezzanine.core.admin import DisplayableAdmin
from .models import Rank
from .models import Person


@admin.register(Rank)
class RankAdmin(admin.ModelAdmin):
    pass


@admin.register(Person)
class PersonAdmin(DisplayableAdmin):
    list_display = ('title', 'rank', 'status')
