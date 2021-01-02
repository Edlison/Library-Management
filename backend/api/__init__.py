# @Author  : Edlison
# @Date    : 12/28/20 18:06
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
# TODO Config
# TODO Manage
# TODO Migrate


db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.urandom(24)
    app.config['SESSION_COOKIE_NAME'] = 'lib-session'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://library:library@119.23.107.61:3306/library'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    db.init_app(app)
    from .user import user_blu  # 要在db创建后引入！
    from .interview import interview_blu
    from .catalog import catalog_blu
    app.register_blueprint(user_blu, url_prefix='/api/user')
    app.register_blueprint(interview_blu, url_prefix='/api/interview')
    app.register_blueprint(catalog_blu, url_prefix='/api/catalog')
    print('router map: \n', app.url_map)
    return app