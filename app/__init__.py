from flask import Flask
from .config import Config
from .models import db
from .routes import routes, mail

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    mail.init_app(app)

    app.register_blueprint(routes)

    return app
