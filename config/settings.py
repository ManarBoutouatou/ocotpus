from pathlib import Path
from django.utils.translation import gettext_lazy as _
from decouple import Csv, config
import os 
from django.contrib.messages import constants as messages

BASE_DIR = Path(__file__).resolve().parent.parent



SECRET_KEY = "<dsvsdvdsvqvqdfbfbsfdnbtnhrt"

DEBUG = True

ALLOWED_HOSTS = ["*"]


INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
# Apps
    'core',
    'business',
# third party
    'django_cleanup.apps.CleanupConfig',
    'import_export',
    'tinymce',
    'markdownx',
    "django_htmx",

]

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

ROOT_URLCONF = "config.urls"

INTERNAL_IPS = ["127.0.0.1"]

WSGI_APPLICATION = "config.wsgi.application"


# ==============================================================================
# MIDDLEWARE SETTINGS
# ==============================================================================

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    'django.middleware.locale.LocaleMiddleware', # for translation
    "django_htmx.middleware.HtmxMiddleware", #HTMX
    'whitenoise.middleware.WhiteNoiseMiddleware',
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]


# ==============================================================================
# TEMPLATES SETTINGS
# ==============================================================================

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "business.context_processors.infos",
            ],        
        },
    },
]


# ==============================================================================
# DATABASES SETTINGS
# ==============================================================================

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'shop4000',
#         'USER': 'postgres',#octopus
#         'PASSWORD': 'miyou0209',#octopus2021@! 
#         'HOST': '127.0.0.1',
#         'PORT': '5432',
#     }
# }
# ==============================================================================
# AUTHENTICATION AND AUTHORIZATION SETTINGS
# ==============================================================================

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
] 
TINYMCE_DEFAULT_CONFIG = {
    "height": "320px",
    "width": "960px",
    "menubar": "file edit view insert format tools table help",
    "plugins": "advlist autolink lists link image charmap print preview anchor searchreplace visualblocks code "
    "fullscreen insertdatetime media table paste code help wordcount spellchecker",
    "toolbar": "undo redo | bold italic underline strikethrough | fontselect fontsizeselect formatselect | alignleft "
    "aligncenter alignright alignjustify | outdent indent |  numlist bullist checklist | forecolor "
    "backcolor casechange permanentpen formatpainter removeformat | pagebreak | charmap emoticons | "
    "fullscreen  preview save print | insertfile image media pageembed template link anchor codesample | "
    "a11ycheck ltr rtl | showcomments addcomment code",
    "custom_undo_redo_levels": 10,
    "language": "fr_FR"
}


# ==============================================================================
# I18N AND L10N SETTINGS
# ==============================================================================

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True

LOCALE_PATHS = [BASE_DIR / "locale"]


# ==============================================================================
# STATIC FILES SETTINGS
# ==============================================================================

# STATIC_URL = "/static/"

# STATIC_ROOT = BASE_DIR / "assets"

# STATICFILES_DIRS = [BASE_DIR / "static"]

# STATICFILES_FINDERS = (
#     "django.contrib.staticfiles.finders.FileSystemFinder",
#     "django.contrib.staticfiles.finders.AppDirectoriesFinder",
# )
# STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'

# STATIC_URL = '/static/'


STATIC_ROOT = BASE_DIR / "static"
MEDIA_URL = "/media/" 

MEDIA_ROOT = BASE_DIR / "media"

STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
### 
STATIC_URL = '/static/'
# STATICFILES_DIR = [ BASE_DIR / 'static' ]
STATIC_ROOT = BASE_DIR / 'assets'
STATICFILES_DIRS = ['static']
STATICFILES_FINDERS = (
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
    
    # other finders..
)
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/' 
###
# ==============================================================================
# MEDIA FILES SETTINGS
# ==============================================================================

MEDIA_URL = "/media/"

MEDIA_ROOT = BASE_DIR / "media"


# ==============================================================================
# THIRD-PARTY SETTINGS
# ==============================================================================

# EMAIL_BACKEND  = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_PORT = 587
# SERVER_EMAIL = 'octopus.emailing@gmail.com'
EMAIL_HOST_USER = 'octopus.emailing@gmail.com'
# EMAIL_HOST_PASSWORD = 'Mi.you20905991'

# EMAIL_USE_TLS = True
# EMAIL_USE_SSL = False

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# ==============================================================================
# FIRST-PARTY SETTINGS
# ==============================================================================

# sunlab_ENVIRONMENT = config("sunlab_ENVIRONMENT", default="local")
try:
    from .local_settings import *
except ImportError:
    pass

MESSAGE_TAGS = {
    messages.DEBUG: 'alert-info',
    messages.INFO: 'alert-info',
    messages.SUCCESS: 'alert-success',
    messages.WARNING: 'alert-warning',
    messages.ERROR: 'alert-danger',
}

