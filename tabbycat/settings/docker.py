# ==============================================================================
# Docker
# ==============================================================================

import os

ALLOWED_HOSTS = ["*"]

CSRF_TRUSTED_ORIGINS = ['https://*.cargotab.net','https://cargotab.net']

TIME_ZONE = 'Asia/Dhaka'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'tabbycat',
        'USER': 'tabbycat',
        'PASSWORD': 'tabbycat',
        'HOST': 'db',
        'PORT': 5432, # Non-standard to prevent collisions,
    }
}

if bool(int(os.environ['DOCKER_REDIS'])) if 'DOCKER_REDIS' in os.environ else False:
    CACHES = {
        "default": {
            "BACKEND": "django_redis.cache.RedisCache",
            "LOCATION": "redis://redis:6379/1",
            "OPTIONS": {
                "CLIENT_CLASS": "django_redis.client.DefaultClient",
                "SOCKET_CONNECT_TIMEOUT": 5,
                "SOCKET_TIMEOUT": 60,
            },
        },
    }

    CHANNEL_LAYERS = {
        "default": {
            "BACKEND": "channels_redis.core.RedisChannelLayer",
            "CONFIG": {
                "hosts": [("redis", 6379)],
                "group_expiry": 10800,
            },
        },
    }

# Email settings for local development using Gmail
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'cargotab.mail@gmail.com'  # Your Gmail email address
EMAIL_HOST_PASSWORD = 'xcgthnuqedecmfyi'  # Your Gmail password
EMAIL_PORT = 587  # Use TLS port
EMAIL_USE_TLS = True  # Use TLS for secure connection
DEFAULT_FROM_EMAIL = 'cargotab.mail@gmail.com'  # Replace with your Gmail email address