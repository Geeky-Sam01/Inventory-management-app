from datetime import date,datetime
from flask import render_template,request,flash
from app.departments import departments_bp
from wtforms import IntegerField,validators,SubmitField,StringField
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm
items={}


class GroceryInputs(FlaskForm):
    product_id = StringField('Product_ID', validators=[DataRequired(),validators.length(min=1,max=50)])
    quantity = IntegerField('Quantity', validators=[DataRequired(),validators.NumberRange(min=1,max=999)])
    price = IntegerField('Price', validators=[DataRequired(),validators.NumberRange(min=1,max=999)])
    submit=SubmitField('Submit')


class GroceryUpdateInputs(FlaskForm):
    product_id = StringField('Product_ID', validators=[DataRequired(),validators.length(min=1,max=50)])
    quantity = IntegerField('Quantity', validators=[DataRequired(),validators.NumberRange(min=1,max=999)])
    price = IntegerField('Price', validators=[DataRequired(),validators.NumberRange(min=1,max=999)])
    submit=SubmitField('Submit')

@departments_bp.route('/')
def home():
    return render_template('departments/home.html')

@departments_bp.route('/grocery' , methods=['GET','POST'])
def grocery():
    id,qty,price=[None,None,None]
    form = GroceryInputs()
    if request.method == 'POST' and form.validate_on_submit():
            time =datetime.now().strftime('%H:%M:%S') + " " + date.today().strftime("%b-%d-%Y")
            id = form.product_id.data
            qty=form.quantity.data
            price=form.price.data
            global items
            items.update({id:{'Price':price,'Quantity':qty,'Time':time}})
            form.product_id.data = ''
            form.quantity.data =''
            form.price.data =''
            flash('Succesfully added items from Grocery','success')
    if request.method: # ToDo : get endpoint for admin dashboard
        pass #USAGE : Admin dashboard
    return render_template('departments/grocery.html',items=items,form=form,num_of_items=len(items))

@departments_bp.route('/grocery_update',methods=['POST'])
def grocery_update():
    global items
    id,qty,price=[None,None,None]
    form = GroceryUpdateInputs() #form validation for update
    if request.method == 'POST' and form.validate_on_submit():
            id = form.product_id.data
            if items.__contains__(id):
                time =datetime.now().strftime('%H:%M:%S') + " " + date.today().strftime("%b-%d-%Y")
                qty=form.quantity.data
                price=form.price.data
                items.update({id:{'Price':price,'Quantity':qty,'Time':time}})
                form.product_id.data = ''
                form.quantity.data =''
                form.price.data =''
                flash('Succesfully updated items from Grocery_update','success')
            else:
                flash('Item not found in the stock!!','danger')
    return render_template('departments/grocery.html',items=items,form=form,num_of_items=len(items))

@departments_bp.route('/grocery_delete',methods=['POST'])
def grocery_delete():
    form=GroceryInputs()
    flash('Succesfully deleted items from Grocery_delete','delete')
    if request.method=='POST':
        id = request.args['product_id']
        if items.__contains__(id):
            items.pop(id)
    return render_template('departments/grocery.html',items=items,form=form,num_of_items=len(items))







@departments_bp.route('/electronics')
def electronics():
    return render_template('departments/electronics.html')
@departments_bp.route('/electronics_update')
def electronics_update():
    pass


@departments_bp.route('/clothing')
def clothing():
    return render_template('departments/clothing.html')