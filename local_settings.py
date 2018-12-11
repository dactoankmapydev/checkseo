# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '2*#fc3wkv+j%d@fj9&#rciq3ld@n636xe#@w#-&h2270r%wl7p'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['checkseo.herokuapp.com']

SECURE_SSL_REDIRECT = True

# Configure Django App for Heroku.
import django_heroku
django_heroku.settings(locals())
