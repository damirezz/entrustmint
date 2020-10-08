from flask import Blueprint, url_for, redirect, render_template, request, flash
from entrust.models import AccountDetails
from flask_login import login_required
account = Blueprint('account', __name__)

@account.route('/add-account')
@login_required
def add_account():
    title = 'Add Account'
    
    return render_template('add_account.html', title = title)