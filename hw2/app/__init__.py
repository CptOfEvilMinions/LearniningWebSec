from app.helpers.create_db_users import create_users
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from flask_login import LoginManager
from flask_cors import CORS
from flask import Flask

# Init CSRF protection
csrf = CSRFProtect()

# init SQLAlchemy
db = SQLAlchemy()

# Init LoginManager
login_manager = LoginManager()

# Init CORS
cors = CORS()

def create_app(config_object):
    # Init flask
    app = Flask(__name__)
    app.config.from_object(config_object)

    with app.app_context(): 
        # Init DB
        db.init_app(app)

        # REMOVE CORs protection
        cors.init_app(app)
        app.config['CORS_ALLOW_HEADERS'] = "Content-Type"
        app.config['CORS_RESOURCES'] = {r"/vulnerable/*": {"origins": "*"}}

        # Add CSRF protection
        csrf.init_app(app)

        # Add LoginManager
        login_manager.init_app(app)

        # Import blueprints
        from app.views.secure import secure
        from app.views.auth import auth
        from app.views.profile import profile
        from app.views.status import status
        from app.views.vulnerable import vulnerable

        # Register blueprints
        app.register_blueprint(secure)
        app.register_blueprint(profile)
        app.register_blueprint(auth)
        app.register_blueprint(status)
        app.register_blueprint(vulnerable)

        # Initialize Global db
        db.create_all()

        # Create users
        create_users(db)

        return app