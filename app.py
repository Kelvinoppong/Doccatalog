from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config
import os

# Initialize Flask extensions
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    
    # Load configuration
    app.config.from_object(Config)
    Config.init_app(app)

    # Ensure upload folder exists
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

    # Initialize extensions with app
    db.init_app(app)

    # Create database tables
    with app.app_context():
        db.create_all()

    # Register blueprints here (we'll add these later)
    # from routes import main_bp
    # app.register_blueprint(main_bp)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=app.config['FLASK_DEBUG'] == '1') 