from werkzeug.security import generate_password_hash
from datetime import datetime

def create_users(db):
    print ('[*] {0} - Adding users to datbase'.format( datetime.now() ))
    # Create users
    from app.model import User

    # Sally user
    existing_user = User.query.filter_by(email='sally@bank.com').first()
    if existing_user is None:
        user = User(name='Sally',
                            email='sally@bank.com',
                            password=generate_password_hash('password123', method='sha256'),
                            website='google.com',
                            balance=100)
        db.session.add(user)

    # Bob user
    existing_user = User.query.filter_by(email='bob@bank.com').first()
    if existing_user is None: 
        user = User(name='Bob',
                            email='bob@bank.com',
                            password=generate_password_hash('Password123!', method='sha256'),
                            website='google.com',
                            balance=0)
        db.session.add(user)

        # Commit users to database
        db.session.commit()

    # Query all users
    users = User.query.all()
    print (users)
