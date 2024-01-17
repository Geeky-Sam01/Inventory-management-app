from app.admin import admin_bp
@admin_bp.route('/')
def hello():
    return '<h1>This is the admin page, with dashboard</h1>'