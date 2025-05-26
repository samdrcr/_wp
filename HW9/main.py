import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__))) 

from flask import Flask, session, flash
from flask_sqlalchemy import SQLAlchemy
import secrets

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    
    app.config['SECRET_KEY'] = secrets.token_hex(16)
    
    app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{os.getenv('DB_USERNAME', 'root')}:{os.getenv('DB_PASSWORD', 'password')}@{os.getenv('DB_HOST', 'localhost')}:{os.getenv('DB_PORT', '3306')}/{os.getenv('DB_NAME', 'mydb')}"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    db.init_app(app)
    
    from src.routes.auth import auth_bp
    from src.routes.post import post_bp
    
    app.register_blueprint(auth_bp)
    app.register_blueprint(post_bp)
    
    with app.app_context():
        db.create_all()
    
    return app

app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
