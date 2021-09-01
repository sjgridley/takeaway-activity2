from flask import render_template

from app import app

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title = 'Home')
@app.route('/menu')
def menu():
    return render_template('menu.html', title = 'Menu')
@app.route('/orders')
def orders():
    return render_template('orders.html', title = 'Orders')