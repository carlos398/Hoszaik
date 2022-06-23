from pathlib import Path
import environ

env = environ.Env()
environ.Env().read_env()

BASE_DIR = Path(__file__).resolve().parent.parent


SQLITE = {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
}

POSTGRES = {
	'ENGINE': 'django.db.backends.postgresql',
	'NAME': env('POSTGRES_DB'),
	'USER': env('POSTGRES_USER'),
	'PASSWORD': env('POSTGRES_PASSWORD'),
	'HOST': env('POSTGRES_HOST'),
	'PORT': env('POSTGRES_PORT'),
}
