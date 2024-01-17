from flask import render_template,request
from app.departments.views import items
from app.home import home_bp
@home_bp.route('/')
def home():
    num_of_items=len(items)
    return render_template('home/home.html',num_of_items=num_of_items)
# onLoading home.html this function is called