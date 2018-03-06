
from __future__ import absolute_import, unicode_literals
import os

from django import VERSION as DJANGO_VERSION
from django.utils.translation import ugettext_lazy as _


######################
# MEZZANINE SETTINGS #
######################

ADMIN_MENU_ORDER = (
    ('Content', (
        'pages.Page',
        'blog.BlogPost',
        (_('Media Library'), 'media-library'),
        'media.Gallery',
        'stuff.Person',
        'stuff.Rank',
        'halls.Hall',
     )),
    ("Site", ("sites.Site", "redirects.Redirect", "conf.Setting", "auth.User", "auth.Group",)),
)

# A three item sequence, each containing a sequence of template tags
# used to render the admin dashboard.
#
# DASHBOARD_TAGS = (
#     ("blog_tags.quick_blog", "mezzanine_tags.app_list"),
#     ("comment_tags.recent_comments",),
#     ("mezzanine_tags.recent_actions",),
# )

# A sequence of templates used by the ``page_menu`` template tag. Each
# item in the sequence is a three item sequence, containing a unique ID
# for the template, a label for the template, and the template path.
# These templates are then available for selection when editing which
# menus a page should appear in. Note that if a menu template is used
# that doesn't appear in this setting, all pages will appear in it.

PAGE_MENU_TEMPLATES = (
    (1, _('Top navigation bar'), 'pages/menus/menu.html'),
    (2, _('Footer'), 'pages/menus/footer.html'),
)

EXTRA_MODEL_FIELDS = (
    (
        # Dotted path to field.
        "mezzanine.blog.models.BlogPost.gallery",
        # Dotted path to field class.
        "django.db.models.ForeignKey",
        # Positional args for field class.
        ("media.Gallery",),
        # Keyword args for field class.
        {"verbose_name": _("Галлерея"), "blank": True, "null": True},
    ),
    # Example of adding a field to *all* of Mezzanine's content types:
    # (
    #     "mezzanine.pages.models.Page.another_field",
    #     "IntegerField", # 'django.db.models.' is implied if path is omitted.
    #     (_("Another name"),),
    #     {"blank": True, "default": 1},
    # ),
)

BLOG_USE_FEATURED_IMAGE = True
ADMIN_THUMB_SIZE = '50x50'
BLOG_POST_PER_PAGE = 10
MAX_PAGING_LINKS = 6

THUMBNAILS_DIR_NAME = 'thumbnails'


USE_MODELTRANSLATION = False

TIME_ZONE = 'UTC'

USE_TZ = True
USE_I18N = True

LANGUAGE_CODE = "ru"

LANGUAGES = (
    ('ru', _('Русский')),
)

SESSION_EXPIRE_AT_BROWSER_CLOSE = True

SITE_ID = 1


AUTHENTICATION_BACKENDS = ('mezzanine.core.auth_backends.MezzanineBackend',)

FILE_UPLOAD_PERMISSIONS = 0o644

# Full filesystem path to the project.
PROJECT_APP_PATH = os.path.dirname(os.path.abspath(__file__))
PROJECT_APP = os.path.basename(PROJECT_APP_PATH)
PROJECT_ROOT = BASE_DIR = os.path.dirname(PROJECT_APP_PATH)

CACHE_MIDDLEWARE_KEY_PREFIX = PROJECT_APP

STATIC_URL = '/static/'
MEDIA_URL = '/media/'

STATIC_ROOT = os.path.join(PROJECT_ROOT, 'public_html', 'static')
MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'public_html', 'media')

ROOT_URLCONF = '%s.urls' % PROJECT_APP

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(PROJECT_ROOT, 'sambo/templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.static',
                'django.template.context_processors.media',
                'django.template.context_processors.request',
                'django.template.context_processors.tz',
                'mezzanine.conf.context_processors.settings',
                'mezzanine.pages.context_processors.page',
            ],
            'builtins': [
                'mezzanine.template.loader_tags',
            ],
        },
    },
]


if DJANGO_VERSION < (1, 9):
    del TEMPLATES[0]['OPTIONS']['builtins']

STATICFILES_DIRS = (
    os.path.join(PROJECT_ROOT, 'frontend', 'build'),
)

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.redirects',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'django.contrib.staticfiles',
    'mezzanine.boot',
    'mezzanine.conf',
    'mezzanine.core',
    'mezzanine.generic',
    'mezzanine.pages',
    'mezzanine.blog',
    'mezzanine.forms',
    'mezzanine.galleries',
    'mezzanine.twitter',
    # 'mezzanine.accounts',
    # 'mezzanine.mobile',

    'easy_thumbnails',

    'sambo.content_pages',
    'sambo.stuff',
    'sambo.media',
    'sambo.halls',
)

MIDDLEWARE_CLASSES = (
    'mezzanine.core.middleware.UpdateCacheMiddleware',

    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'mezzanine.core.request.CurrentRequestMiddleware',
    'mezzanine.core.middleware.RedirectFallbackMiddleware',
    'mezzanine.core.middleware.TemplateForDeviceMiddleware',
    'mezzanine.core.middleware.TemplateForHostMiddleware',
    'mezzanine.core.middleware.AdminLoginInterfaceSelectorMiddleware',
    'mezzanine.core.middleware.SitePermissionMiddleware',
    'mezzanine.pages.middleware.PageMiddleware',
    'mezzanine.core.middleware.FetchFromCacheMiddleware',
)

PACKAGE_NAME_FILEBROWSER = 'filebrowser_safe'
PACKAGE_NAME_GRAPPELLI = 'grappelli_safe'


OPTIONAL_APPS = (
    'debug_toolbar',
    'django_extensions',
    'compressor',
    PACKAGE_NAME_FILEBROWSER,
    PACKAGE_NAME_GRAPPELLI,
)


from .local_settings import *


####################
# DYNAMIC SETTINGS #
####################

# set_dynamic_settings() will rewrite globals based on what has been
# defined so far, in order to provide some better defaults where
# applicable. We also allow this settings module to be imported
# without Mezzanine installed, as the case may be when using the
# fabfile, where setting the dynamic settings below isn't strictly
# required.
try:
    from mezzanine.utils.conf import set_dynamic_settings
except ImportError:
    pass
else:
    set_dynamic_settings(globals())
