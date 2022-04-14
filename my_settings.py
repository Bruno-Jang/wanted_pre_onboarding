from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

DATABASES = {
    'default': {
        # 'ENGINE': 'django.db.backends.sqlite3',
        # 'NAME': BASE_DIR / 'db.sqlite3',
        'ENGINE': 'django.db.backends.mysql',
        'NAME': '', # DB 이름 입력
        'USER': 'root',
        'PASSWORD': '', # DB 비밀번호 입력
        'HOST': 'localhost',
        'PORT': ''
    }
}

SECRET_KEY = 'django-insecure-^&#90=g3%@r9$4n8mp6m6gudlca8#7c+1(&-9wrt453x1yubb@'
