from copy import deepcopy
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from mezzanine.pages.admin import PageAdmin
from mezzanine.core.admin import TabularDynamicInlineAdmin
from mezzanine.blog.admin import BlogPostAdmin
from mezzanine.blog.models import BlogPost

from .models import HomePage
from .models import Slide


class SlideInline(TabularDynamicInlineAdmin):
    model = Slide
    extra = 0


@admin.register(HomePage)
class HomePageAdmin(PageAdmin):
    inlines = (SlideInline, )
    fieldsets = (
        (None, {
            "fields": ["title", 'content_title', 'content'],
        }),
        ('Сотрудник', {
            'fields': ['person', 'person_text', 'person_date']
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


blog_fieldsets = deepcopy(BlogPostAdmin.fieldsets)
blog_fieldsets[0][1]["fields"].insert(-2, "gallery")


class CustomBlogPostAdmin(BlogPostAdmin):
    fieldsets = blog_fieldsets
    raw_id_fields = ('gallery', )


admin.site.unregister(BlogPost)
admin.site.register(BlogPost, CustomBlogPostAdmin)
