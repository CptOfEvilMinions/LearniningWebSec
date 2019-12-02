from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from . import db

class User(UserMixin, db.Model):
    """Model for user accounts."""

    __tablename__ = 'flasklogin-users'

    # ID of entry in table
    id = db.Column(db.Integer, primary_key=True)
    # Name of user
    name = db.Column(db.String, nullable=False, unique=False)
    # E-mail for user
    email = db.Column(db.String(40), unique=True, nullable=False)
    # Password for user
    password = db.Column(db.String(200), primary_key=False, unique=False, nullable=False)
    # Balance in user account
    balance = db.Column(db.Integer, primary_key=False, unique=False, nullable=False)
    website = db.Column(db.String(60), index=False, unique=False, nullable=True)
    created_on = db.Column(db.DateTime, index=False, unique=False, nullable=True)
    last_login = db.Column(db.DateTime, index=False, unique=False, nullable=True)

    def set_password(self, password):
        """Create hashed password."""
        self.password = generate_password_hash(password, method='sha256')

    def check_password(self, password):
        """Check hashed password."""
        return check_password_hash(self.password, password)

    def __repr__(self):
        return '<User {}>'.format(self.email)