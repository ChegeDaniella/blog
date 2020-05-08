from flask import Blueprint,Flask
main = Blueprint('main',__name__)
from app.main import views

def create_app(config_name):
    app = Flask(__name__)


    # Registering the blueprint
    from main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app