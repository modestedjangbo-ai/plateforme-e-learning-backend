from pathlib import Path


# Chemin du projet
BASE_DIR = Path(__file__).resolve().parent.parent



# Clé secrète Django
SECRET_KEY = 'django-insecure-change-this-key'


# Mode développement
DEBUG = True


ALLOWED_HOSTS = [
    '127.0.0.1',
    'localhost',
]



# Applications installées

INSTALLED_APPS = [

    # Django
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',


    # API
    'rest_framework',
    'corsheaders',


    # Applications du projet
    'accounts',
    'courses',
    'lessons',
    'enrollement',
    'contact',
    'quiz',

]



# Middleware

MIDDLEWARE = [

    'corsheaders.middleware.CorsMiddleware',

    'django.middleware.security.SecurityMiddleware',

    'django.contrib.sessions.middleware.SessionMiddleware',

    'django.middleware.common.CommonMiddleware',

    'django.middleware.csrf.CsrfViewMiddleware',

    'django.contrib.auth.middleware.AuthenticationMiddleware',

    'django.contrib.messages.middleware.MessageMiddleware',

    'django.middleware.clickjacking.XFrameOptionsMiddleware',

]



ROOT_URLCONF = 'core.urls'



# Templates HTML

TEMPLATES = [

    {

        'BACKEND': 'django.template.backends.django.DjangoTemplates',

        'DIRS': [
            BASE_DIR / 'templates'
        ],

        'APP_DIRS': True,


        'OPTIONS': {

            'context_processors': [

                'django.template.context_processors.request',

                'django.contrib.auth.context_processors.auth',

                'django.contrib.messages.context_processors.messages',

            ],

        },

    },

]



WSGI_APPLICATION = 'core.wsgi.application'





# Base de données

DATABASES = {

    'default': {

        'ENGINE': 'django.db.backends.sqlite3',

        'NAME': BASE_DIR / 'db.sqlite3',

    }

}




# Validation des mots de passe

AUTH_PASSWORD_VALIDATORS = [

    {
        'NAME':
        'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },

    {
        'NAME':
        'django.contrib.auth.password_validation.MinimumLengthValidator',
    },

    {
        'NAME':
        'django.contrib.auth.password_validation.CommonPasswordValidator',
    },

    {
        'NAME':
        'django.contrib.auth.password_validation.NumericPasswordValidator',
    },

]





# Langue

LANGUAGE_CODE = 'fr-fr'


TIME_ZONE = 'Africa/Dakar'


USE_I18N = True


USE_TZ = True





# Fichiers statiques

STATIC_URL = 'static/'


STATICFILES_DIRS = [

    BASE_DIR / "static",

]





# Fichiers médias

MEDIA_URL = '/media/'


MEDIA_ROOT = BASE_DIR / 'media'





# Modèle utilisateur personnalisé

AUTH_USER_MODEL = 'accounts.User'





# Django REST Framework

REST_FRAMEWORK = {


    'DEFAULT_AUTHENTICATION_CLASSES': (

        'rest_framework_simplejwt.authentication.JWTAuthentication',

    ),


}




# Autoriser Angular

CORS_ALLOW_ALL_ORIGINS = True





# Type de clé primaire

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'