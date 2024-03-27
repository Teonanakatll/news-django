DEBUG = False
ALLOWED_HOSTS = ['news.dve-verevki.ru', 'www.news.dve-verevki.ru']
INTERNAL_IPS = None

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'ffaaeepi_news',
        'USER': 'ffaaeepi_news',
        'PASSWORD': '*K50coOG',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
