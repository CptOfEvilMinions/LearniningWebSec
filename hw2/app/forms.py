from wtforms import Form, StringField, PasswordField, validators, SubmitField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, Length, Optional

class LoginForm(Form):
    """User Login Form."""

    email = StringField('Email', validators=[DataRequired('Please enter a valid email address.'),
                                            Email('Please enter a valid email address.')])
    password = PasswordField('Password', validators=[DataRequired('Uhh, your password tho?')])
    submit = SubmitField('Log In')

class TransferForm(Form):
    """User Money Transfer Form."""
    email = StringField('Email', validators=[DataRequired('Please enter a valid email address.'),
                                            Email('Please enter a valid email address.')])
    amount = StringField('Amount', validators=[DataRequired('Uhh, your password tho?')])
    submit = SubmitField('Transfer')