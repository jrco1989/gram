import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'tet%b61i5iqhjg3(dc-5$(5__k4=25+&=t54p*^0&3-vuiqd0t'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',#takes care of the connection with the database 
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'posts',
    'user',
]
#son una serie de hooks y apis que nos permiten modificar el objeto request antes de que llegue a la vista 
#  y response antes de que salga de la vista
#son llamados antes y después de la petición 
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',#este se encarga d ecomprobar todas las medidas de seguridad 
    'django.contrib.sessions.middleware.SessionMiddleware',# es escargado de validar una sesíon 
    'django.middleware.common.CommonMiddleware',#se encarga de ver lo del "deboger", cosas relacionadas del framework
    'django.middleware.csrf.CsrfViewMiddleware',#es el que nos permite llamar a nuestro token para validar formularios 
    'django.contrib.auth.middleware.AuthenticationMiddleware',#agrega cosas como request.user sin necesidad de llamar un template
    'django.contrib.messages.middleware.MessageMiddleware',#relacionado al framework de mensajes de django 
    'django.middleware.clickjacking.XFrameOptionsMiddleware',#seguridad con frameoptions 
    'pgram.middleware.ProfileCompletionMiddleware',#se pone la ruta de la API para agregarla 
]

ROOT_URLCONF = 'pgram.urls' # main urls file

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'pgram.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/Bogota'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'# a partir de cual url se servirán los datos
#STATIC_ROOT = os.path.join(BASE_DIR, 'static')#ruta absoluta de la ubicacion de los archivos estaáticos 
STATICFILES_DIRS=[    #idendica cuáles son los directorios donde están los archivos estáticos. 
    os.path.join(BASE_DIR, 'static'),
    ]
STATICFILES_FINDER= [ #métodos para encontrar los archivos estáticos 
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]
MEDIA_ROOT=os.path.join(BASE_DIR, 'media')
MEDIA_URL='/media/' #ubicacion del directorio de media
LOGIN_URL='/users/ingreso' #ubicación de la vista para loguearnos

"""set
#during
#handling
#above
#patterns
#unable to access
#denied
#caution
#letters
foreign
feed
releases
released
issue
finders
middleware
submit
path
forbidden 
#fives
#tens"""