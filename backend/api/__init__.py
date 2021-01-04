# @Author  : Edlison
# @Date    : 12/28/20 18:06
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config


db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    from .circulation import cir_blu
    app.register_blueprint(cir_blu, url_prefix='/api/cir')
    from .user import user_blu  # 要在db创建后引入！
    app.register_blueprint(user_blu, url_prefix='/api/user')
    from .interview import interview_blu
    app.register_blueprint(interview_blu, url_prefix='/api/interview')
    from .catalog import catalog_blu
    app.register_blueprint(catalog_blu, url_prefix='/api/catalog')

    return app
