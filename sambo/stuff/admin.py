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
    raw_id_fields = ('gallery', )
    fieldsets = (
        (None, {
            "fields": ["title", 'position', 'rank', 'photo', 'content', 'gallery'],
        }),

        (_("Meta data"), {
            "fields": ["_meta_title", "slug",
                       ("description", "gen_description"),
                       "keywords", "in_sitemap"],
            "classes": ("collapse-closed",)
        }),
        ('Настройки публикации', {
            'fields': ["status", ("publish_date", "expiry_date")]
        })
    )
