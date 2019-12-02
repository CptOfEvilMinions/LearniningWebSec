from flask import request, Blueprint, render_template, make_response, flash, redirect, url_for
from app import csrf, db
from datetime import datetime
from app.forms import TransferForm
from flask_login import login_required, current_user
from app.model import User

# Add blueprints
secure = Blueprint('secure', __name__, url_prefix="/secure",template_folder='templates')

@secure.route('/transfer_money', methods=['GET', 'POST'])
@login_required
def secure_transfer_money():
    """
    Implement vulnerable transfer money function
    """
    transfer_form = TransferForm(request.form)

    if request.method == 'POST':
        print ( request.form )
        print (current_user)
        if transfer_form.validate():

            print ( request.form )
            email = request.form.get('email')
            amount = int(request.form.get('amount'))

            # User balance is being subtracted from
            user_withdrawl = User.query.filter_by(email=current_user.email).first()
            user_withdrawl.balance = user_withdrawl.balance - amount
            print (user_withdrawl)
            db.session.add(user_withdrawl)
            db.session.commit()


            # User balance is being added too
            user_deposit = User.query.filter_by(email=email).first()
            user_deposit.balance = user_deposit.balance + amount
            print (user_deposit)
            db.session.add(user_deposit)
            db.session.commit()

            return redirect(url_for('profile.user_profile'))
        

        flash('Invalid user e-mail or balance')
        return redirect(url_for('secure.secure_transfer_money'))

    # GET: Serve transfer money page
    return render_template('secure/transfer_money.html',
                           form=TransferForm(),
                           title='Secure money transfer',
                           template='login-page',
                           body="Log in with your User account.")