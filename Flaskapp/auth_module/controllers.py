# Import flask dependencies
from flask import Blueprint, request, render_template, \
                  flash, g, session, redirect, url_for

# Import password / encryption helper tools
from werkzeug import *
#check_password_hash, generate_password_hash

# Import the database object from the main app module
from Flaskapp import db

# Import module forms
from Flaskapp.auth_module.forms import LoginForm

# Import module models (i.e. User)
from Flaskapp.auth_module.models import User

# Define the blueprint: 'auth', set its url prefix: app.url/auth
auth_module = Blueprint('auth', __name__, url_prefix='/auth')

# Set the route and accepted methods
@auth_module.route('/signin/', methods=['GET', 'POST'])
def signin():

    # If sign in form is submitted
    form = LoginForm(request.form)

    # Verify the sign in form
    if form.validate_on_submit():

        user = User.query.filter_by(email=form.email.data).first()

        if user and check_password_hash(user.password, form.password.data):

            session['user_id'] = user.id

            flash('Welcome %s' % user.name)

            return redirect(url_for('auth.home'))

        flash('Wrong email or password', 'error-message')

    return render_template("auth_module/signin.html", form=form)