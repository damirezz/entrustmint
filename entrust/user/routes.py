#This folder contains pages that uses the User Model/Database
from flask import Blueprint, render_template, url_for, redirect, request, flash, request
from entrust.models import User, AccountDetails
from .forms import RegistrationForm, LoginForm, UpdateAccountInfo
from werkzeug.security import generate_password_hash, check_password_hash
from entrust import db, login_manager
from flask_login import login_user, logout_user, login_required, current_user

user = Blueprint('user', __name__)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


@user.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('idle.home'))


def signin():
    title = 'Sign In'
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email = form.email.data).first()
        print(form.email.data)
        if user: 
            if check_password_hash(user.password, form.password.data):
                login_user(user, remember=True)
                next = request.args.get('next')
                flash(f'Welcome back {current_user.fname}','success')
                return redirect(next or url_for('user.profile'))
            else:
                flash('The password you entered is not correct','danger')
        else:
            flash('There is no user with this email','danger')

    return render_template('signin.html', title=title, form=form)


    def signup():
    form = RegistrationForm()
    title = 'Sign Up'
    
    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.confirm_password.data)
        user = User(
            fname = form.fname.data, 
            lname = form.lname.data,
            email = form.email.data,
            phone = form.phone.data,
            password = hashed_password
            )
        
        db.session.add(user)
        db.session.commit()

        login_user(user)

        flash(f'Welcome {form.fname.data}! Your Account Has Been Created Successfully','success')

        return redirect(url_for("idle.welcome"))
    
    return render_template('signup.html', title = title, form=form)


@user.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    title = 'Profile'
    form = UpdateAccountInfo()
    if request.method == "POST" and form.validate_on_submit:
        current_user.fname = form.fname.data
        current_user.lname = form.lname.data
        current_user.phone = form.phone.data
        db.session.commit()
        flash('You have successfully updated your account information','success')
        return redirect(url_for('user.profile'))
    form.fname.data = current_user.fname
    form.lname.data = current_user.lname
    form.phone.data = current_user.phone
    return render_template('profile.html', form=form)


@user.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    title = 'Dashboard'
    return render_template('dashboard.html')




@app.route("/contact", methods=["GET", "POST"])
def contact_us():
    return render_template('contact.html', title="Naira Stream")
