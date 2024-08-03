from flask import Flask
from routes.user_routes import user_bp
from routes.feature_routes import feature_bp
from routes.designer_routes import designer_bp
from create_app import app


if __name__ == '__main__':
    app.register_blueprint(user_bp, url_prefix='/user')
    app.register_blueprint(feature_bp,url_prefix='/feature')
    #app.register_blueprint(designer_bp,url_prefix='/designer')
    app.run(host='0.0.0.0', port=5000, debug=True)