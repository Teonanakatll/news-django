DEBUG = False
ALLOWED_HOSTS = ['*']
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