from flask import Blueprint, render_template, request, redirect, url_for, flash, session, abort
from src.models.post import Post
from src.models.user import User
from src.main import db

post_bp = Blueprint('post', __name__)

@post_bp.route('/')
def index():
    posts = Post.query.order_by(Post.created_at.desc()).all()
    user_id = session.get('user_id')
    user = None
    if user_id:
        user = User.query.get(user_id)
    return render_template('index.html', posts=posts, user=user)

@post_bp.route('/post/new', methods=['GET', 'POST'])
def new_post():
    # Check if user is logged in
    user_id = session.get('user_id')
    if not user_id:
        flash('You must be logged in to create a post.', 'error')
        return redirect(url_for('auth.login'))
    
    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')
        
        # Validate input
        if not title or not content:
            flash('Title and content are required.', 'error')
            return render_template('new_post.html')
        
        # Create new post
        new_post = Post(
            title=title,
            content=content,
            user_id=user_id
        )
        
        # Add to database
        db.session.add(new_post)
        db.session.commit()
        
        flash('Post created successfully!', 'success')
        return redirect(url_for('post.index'))
    
    return render_template('new_post.html')

@post_bp.route('/post/<int:post_id>/delete', methods=['POST'])
def delete_post(post_id):

    user_id = session.get('user_id')
    if not user_id:
        flash('You must be logged in to delete a post.', 'error')
        return redirect(url_for('auth.login'))
    
    post = Post.query.get_or_404(post_id)
    
    if post.user_id != user_id:
        abort(403, description="You can only delete your own posts")
    
    db.session.delete(post)
    db.session.commit()
    
    flash('Post deleted successfully!', 'success')
    return redirect(url_for('post.index'))
