from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from werkzeug.security import generate_password_hash, check_password_hash
from src.models.user import User
from src.main import db

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            flash('Username already exists. Please choose a different one.', 'error')
            return render_template('signup.html')
        
        new_user = User(
            username=username,
            password=generate_password_hash(password)
        )
        
        db.session.add(new_user)
        db.session.commit()
        
        session['user_id'] = new_user.id
        
        flash('Account created successfully!', 'success')
        return redirect(url_for('post.index'))
    
    return render_template('signup.html')

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        user = User.query.filter_by(username=username).first()
        
      
        if not user or not check_password_hash(user.password, password):
            flash('Invalid username or password. Please try again.', 'error')
            return render_template('login.html')
        
        session['user_id'] = user.id
        
        flash('Logged in successfully!', 'success')
        return redirect(url_for('post.index'))
    
    return render_template('login.html')

@auth_bp.route('/logout')
def logout():

    session.pop('user_id', None)
    flash('Logged out successfully!', 'success')
    return redirect(url_for('post.index'))
