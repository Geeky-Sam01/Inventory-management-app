from flask import Flask

app = Flask(__name__)

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'secretkey'
    from app.home import home_bp
    from app.departments import departments_bp
    from app.admin import admin_bp
    app.register_blueprint(home_bp,url_prefix='/')
    app.register_blueprint(departments_bp, url_prefix='/departments')
    app.register_blueprint(admin_bp,url_prefix='/admin')
    return app

