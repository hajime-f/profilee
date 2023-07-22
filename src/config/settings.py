"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 3.2.20.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

import os
from pathlib import Path

import environ

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

env = environ.Env()
env.read_env(os.path.join(BASE_DIR, '.env'))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# django-allauth関係。django.contrib.sitesで使用するSITE_IDを指定する
SITE_ID = 1

# django-allauthログイン時とログアウト時のリダイレクトURL
LOGIN_REDIRECT_URL = '/'
ACCOUNT_LOGOUT_REDIRECT_URL = '/'


# djangoallauthでメールでユーザー認証する際に必要になる認証バックエンド
AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
]

# ログイン時の認証方法はemailとパスワードとする
ACCOUNT_AUTHENTICATION_METHOD = "email"

# ログイン時にユーザー名(ユーザーID)は使用しない
ACCOUNT_USERNAME_REQUIRED = False

# ユーザー登録時に入力したメールアドレスに、確認メールを送信する事を必須(mandatory)とする
ACCOUNT_EMAIL_VARIFICATION = "mandatory"

# ユーザー登録画面でメールアドレス入力を要求する(True)
ACCOUNT_EMAIL_REQUIRED = True


# DEBUGがTrueのとき、メールの内容は全て端末に表示させる(実際にメールを送信したい時はここをコメントアウトする)
if DEBUG:
    EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
else:
    # TODO:SendgridのAPIキーと送信元メールアドレスを入れていない時、以下が実行されると必ずエラーになる点に注意。
    EMAIL_BACKEND = "sendgrid_backend.SendgridBackend"
    DEFAULT_FROM_EMAIL = "ここにデフォルトの送信元メールアドレスを指定"

    # 【重要】APIキーの入力後、GitHubへのプッシュは厳禁。可能であれば.gitignoreに指定した別ファイルから読み込む
    SENDGRID_API_KEY = "ここにsendgridのAPIkeyを記述する"

    # Sendgrid利用時はサンドボックスモードを無効化しておく。
    SENDGRID_SANDBOX_MODE_IN_DEBUG = False


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'accounts',
]

AUTH_USER_MODEL = "accounts.User"

ACCOUNT_FORMS = {
    "signup": "accounts.forms.CustomUserCreationForm",
}

ACCOUNT_ADAPTER = 'accounts.adapter.AccountAdapter'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
            os.path.join(BASE_DIR, 'templates', 'allauth')
        ],
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

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': env('ENGINE'),
        'NAME': env('NAME'),
        'USER': env('USER'),
        'PASSWORD': env('PASSWORD'),
        'PORT': env('PORT'),
        'HOST': env('HOST'),
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'ja'

TIME_ZONE = 'Asia/Tokyo'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
