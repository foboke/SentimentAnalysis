import os


class TwitterConfig:
    CONSUMER_KEY = os.environ.get('KLw0iN06rCgzDwrUA4IIGsK8G')
    CONSUMER_SECRET = os.environ.get('GfjQFJBnRHD80ab9XkhrZUb7maQ7qsg8tmLwvIMeD5Uq9A1q64')
    ACCESS_TOKEN = os.environ.get('1207725624556699654-VYYIQCrlxQpJHGDjMw6DyqkVT3kl2x')
    ACCESS_TOKEN_SECRET = os.environ.get('k3PPlS8mRGtUxWXu3RjfVO0vYG2xrCHsxY3FML8Pis3BI')


class DBConfig:
    USER = os.environ.get('DB_USER')
    PWORD = os.environ.get('DB_PWORD')
    HOST = os.environ.get('DB_HOST')


if __name__ == '__main__':
    print(type(os.environ.get('CONSUMER_KEY')))
