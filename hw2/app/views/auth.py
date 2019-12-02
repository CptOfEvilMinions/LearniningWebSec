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
auth = Blueprint('auth', __name__, url_prefix="/auth", template_folder='templates')

# Create login route
@app.route('/', methods=['GET', 'POST'])
@auth.route('/login', methods=['GET', 'POST'])
@csrf.exempt
def user_login():
    """User login page."""
    # Bypass Login screen if user is logged in
    if current_user.is_authenticated:
        return redirect(url_for('profile.user_profile'))
    login_form = LoginForm(request.form)

    # POST: Create user and redirect them to the app
    if request.method == 'POST':
        if login_form.validate():
            # Get Form Fields
            email = request.form.get('email')
            password = request.form.get('password')
            # Validate Login Attempt
            user = User.query.filter_by(email=email).first()
            if user:
                if user.check_password(password=password):
                    login_user(user)
                    next = request.args.get('next')
                    return redirect(next or url_for('profile.user_profile'))
        flash('Invalid username/password combination')
        return redirect(url_for('auth.user_login'))
    # GET: Serve Log-in page
    return render_template('auth/user_login.html',
                           form=LoginForm(),
                           title='Log in | Flask-Login Tutorial.',
                           template='login-page',
                           body="Log in with your User account.")
        

@auth.route("/logout")
@login_required
def logout_page():
    """User log-out logic."""
    logout_user()
    return redirect(url_for('auth.user_login'))


@login_manager.user_loader
def load_user(user_id):
    """Check if user is logged-in on every page load."""
    if user_id is not None:
        return User.query.get(user_id)
    return None

@login_manager.unauthorized_handler
def unauthorized():
    """Redirect unauthorized users to Login page."""
    flash('You must be logged in to view that page.')
    return redirect(url_for('auth.user_login'))
