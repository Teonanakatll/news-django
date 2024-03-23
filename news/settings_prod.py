DEBUG = False
ALLOWED_HOSTS = ['news.dve-verevki.ru', 'www.news.dve-verevki.ru']
INTERNAL_IPS = None

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'ffaaeepi_news',
        'USER': 'ffaaeepi_news',
        'PASSWORD': '&hdb*Y2J',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',


    'news_app.apps.NewsAppConfig',
    # https://django-extensions.readthedocs.io/en/latest/ документация по расширениям джанго
    'django_extensions',
    # 'debug_toolbar',

    'django.contrib.sites',
    'django.contrib.sitemaps',
    'metatags',
    'django_ckeditor_5',
    'taggit',
    'sorl.thumbnail',

]