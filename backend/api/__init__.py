# @Author  : Edlison
# @Date    : 12/28/20 18:06
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.urandom(24)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://library:library@119.23.107.61:3306/library'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    db.init_app(app)
    from .user import user_blu  # 要在db创建后引入！
    app.register_blueprint(user_blu)
    print('router map: \n', app.url_map)
    return app