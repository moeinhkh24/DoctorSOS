from .base import *




DATABASES_CONFIG = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
        'USER' : env('POSTGRES_USER'),
        'PASSWORD' : env('POSTGRES_PASSWORD'),
        'HOST': env('POSTGRES_HOST'),
        'PORT': env('POSTGRES_PORT'),
    }
}



def get_config_database(overrides=None):
    
    config = DATABASES_CONFIG.copy()
    
    if overrides:
        for db, params in overrides.item():
            if db in config:
                config[db].update(params)
            else:
                config[db] = params
                
    return config