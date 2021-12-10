from .base import *


DATABASES = {
    'default':{
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'configuracion',
        'USER': 'cristian',
        'PASSWORD':'',
        'HOST':'localhost',
        'PORT':'3306',
    }
}