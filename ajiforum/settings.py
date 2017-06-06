"""Django settings."""
from os.path import dirname, abspath, join
import uuid

BASE_DIR = dirname(dirname(abspath(__file__)))
SECRET_KEY = 'uzi-g3ri_95le=lj6i+t)=)+y1gkay8wcj9s8&ym$d@tlzsw2d'
DEBUG = True
ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
]
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'topics',
]
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
ROOT_URLCONF = 'ajiforum.urls'
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [join(BASE_DIR, 'templates')],
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
WSGI_APPLICATION = 'ajiforum.wsgi.application'
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Taipei'
USE_I18N = True
USE_L10N = True
USE_TZ = True
STATIC_URL = '/static/'

TOPICS = {
    str(uuid.uuid4()): {
        'title': '[翻譯] 喜劇藝人酸觀眾腦殘,結果酸錯人當場崩潰',
        'content': '',
        'datetime': '',
        'upvotes': 0,
        'downvotes': 0,
    },
    str(uuid.uuid4()): {
        'title': '[kuso] 黑人頭果然百搭啊!',
        'content': '',
        'datetime': '',
        'upvotes': 0,
        'downvotes': 0,
    },
    str(uuid.uuid4()): {
        'title': '[笑話] 老梗',
        'content': '',
        'datetime': '',
        'upvotes': 0,
        'downvotes': 0,
    },
    str(uuid.uuid4()): {
        'title': '[猜謎] 為甚麼女生體育課不能跑步',
        'content': '',
        'datetime': '',
        'upvotes': 0,
        'downvotes': 0,
    },
    str(uuid.uuid4()): {
        'title': '[猜謎]這麼多宅肥，87是誰的錯',
        'content': '',
        'datetime': '',
        'upvotes': 0,
        'downvotes': 0,
    },
    str(uuid.uuid4()): {
        'title': '[猜謎] 不相連又拆不開',
        'content': '',
        'datetime': '',
        'upvotes': 0,
        'downvotes': 0,
    },
    str(uuid.uuid4()): {
        'title': '[ＸＤ] 網路搞笑圖片翻譯（兩百七十二）',
        'content': '',
        'datetime': '',
        'upvotes': 0,
        'downvotes': 3,
    },
    str(uuid.uuid4()): {
        'title': '[猜謎] 為什麼Skoda的車那麼好坐？',
        'content': '',
        'datetime': '',
        'upvotes': 0,
        'downvotes': 20,
    },
    str(uuid.uuid4()): {
        'title': '[囧rz] 這個影片....我很難認真看下去...',
        'content': '',
        'datetime': '',
        'upvotes': 87,
        'downvotes': 10,
    },
    str(uuid.uuid4()): {
        'title': '[耍冷] 藍受香菇',
        'content': '',
        'datetime': '',
        'upvotes': 10,
        'downvotes': 0,
    },
    str(uuid.uuid4()): {
        'title': '[猜謎] 甲甲變性',
        'content': '',
        'datetime': '',
        'upvotes': 0,
        'downvotes': 0,
    },
}
