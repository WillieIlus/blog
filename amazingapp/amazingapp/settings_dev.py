import os

from .settings import BASE_DIR

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'qbfj=o1$m&um&7tbeqr%_coeso72zym)g%s!oca-zh1%l=@e4u'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['http://my-amazing-app.captain.test.biasharahub.com/', '0.0.0.0',
                 'http://django-blog.captain.test.biasharahub.com/',
                 '*', 'localhost', '127.0.0.1',
                 'biasharahub.herokuapp.com', 'biasharahub.com']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/
STATIC_ROOT = os.path.join(BASE_DIR, "static")

STATIC_URL = '/static/'
