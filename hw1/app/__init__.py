from flask import Flask

# Init flask
app = Flask(__name__)
app.config['SECRET_KEY'] = 'super secret'


from app.views.main import main
app.register_blueprint(main)