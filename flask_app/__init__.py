from flask import Flask
from flask_cors import CORS

def create_app():
    """
    Create and configure the Flask application.
    """
    app = Flask(__name__)
    
    # Load configurations (you can replace with your own config file/module)
    app.config['SECRET_KEY'] = 'your-secret-key'
    app.config['CORS_HEADERS'] = 'Content-Type'
    
    # Enable CORS
    CORS(app)
    
    # Register blueprints (if you have them, replace `your_blueprint` with actual blueprints)
    # from .your_blueprint import your_blueprint
    # app.register_blueprint(your_blueprint)
    
    # Example route
    @app.route('/')
    def index():
        return {"message": "Welcome to the Social Network API!"}, 200

    return app

# Create the app instance
app = create_app()

if __name__ == "__main__":
    # Run the application
    app.run(host="0.0.0.0", port=5000, debug=True)
