from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from mezzanine.core.admin import DisplayableAdmin

from .models import Gallery
from .models import GalleryImage


class GalleryImageInline(admin.TabularInline):
    model = GalleryImage
    extra = 1


@admin.register(Gallery)
class GalleryAdmin(DisplayableAdmin):
    list_display = ('title', 'status')
    inlines = (GalleryImageInline, )

    fieldsets = (
        (None, {
            "fields": ["title", 'zip_import', ],
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
