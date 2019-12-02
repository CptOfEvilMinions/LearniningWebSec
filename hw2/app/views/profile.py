from flask import redirect, render_template, flash, Blueprint, request, session, url_for
from flask_login import login_required, logout_user, current_user, login_user
from werkzeug.security import generate_password_hash, check_password_hash
from flask import current_app as app
from datetime import datetime
from app.forms import LoginForm
from app.model import db, User
from app import login_manager
from app import csrf


# Add blueprints
profile = Blueprint('profile', __name__, url_prefix="/profile", template_folder='templates')

@login_required
@profile.route('/', methods=['GET'])
def user_profile():
    return render_template('profile/user_profile.html')