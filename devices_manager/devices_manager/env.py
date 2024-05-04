import os

DEBUG = os.environ.get('DEBUG', 'False')

TIME_ZONE = os.environ.get('TIME_ZONE', 'Asia/Shanghai')

# 数据库
DATABASES = os.environ.get('MYSQL_DATABASE', 'default')
DATABASES_HOST = os.environ.get('MYSQL_HOST', 'default')
DATABASES_USER = os.environ.get('MYSQL_USER', 'default')
DATABASES_PASSWORD = os.environ.get('MYSQL_PASSWORD', 'default')
