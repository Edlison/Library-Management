# @Author  : Edlison
# @Date    : 1/4/21 20:20
import os
from datetime import timedelta


class Config:
    DIALECT = 'mysql'
    DRIVER = 'pymysql'
    USERNAME = 'library'
    PASSWORD = 'library'
    HOST = '119.23.107.61'
    PORT = '3306'
    DATABASE = 'library'
    SECRET_KEY = os.urandom(24)
    SESSION_COOKIE_NAME = 'library-session'
    PERMANENT_SESSION_LIFETIME = timedelta(days=1)
    SQLALCHEMY_DATABASE_URI = '{}+{}://{}:{}@{}:{}/{}'.format(DIALECT, DRIVER, USERNAME, PASSWORD, HOST, PORT, DATABASE)
    SQLALCHEMY_TRACK_MODIFICATIONS = True