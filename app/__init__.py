from flask import Flask
from app.routes.praticantes import praticante_bp
from app.routes.pagamentos import pagamentos_bp
from app.routes.planos import planos_bp

from app.config import Config
from app.extensions import db

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    app.register_blueprint(praticante_bp)
    app.register_blueprint(pagamentos_bp)
    app.register_blueprint(planos_bp)

    return app
