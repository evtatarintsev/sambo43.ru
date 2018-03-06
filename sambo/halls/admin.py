from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from mezzanine.core.admin import DisplayableAdmin

from .models import Hall


@admin.register(Hall)
class PersonAdmin(DisplayableAdmin):
    list_display = ('title', 'address', 'phone_no', 'status')
    raw_id_fields = ('gallery', )
    filter_horizontal = ('coaches', )
    fieldsets = (
        (None, {
            "fields": ["title", 'address', 'phone_no', 'photo', 'content', 'gallery', 'coaches'],
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
