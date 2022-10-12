from flask import Flask, render_template, request, redirect
from flask_app import app

from flask_app.models.dojos import Dojo
from flask_app.models.ninjas import Ninja

@app.route('/')
def index():
    return redirect('/dojos')

@app.route('/dojos')
def dojos():
    dojos = Dojo.get_all()
    return render_template('index.html', dojos=dojos)

@app.route('/create/dojo', methods=['POST'])
def create_dojo():
    Dojo.save(request.form)
    return redirect('/dojos')

@app.route('/new/ninja')
def new_ninja():
    dojos = Dojo.get_all()
    return render_template('new.html', dojos=dojos)

@app.route('/create/ninja', methods=['POST'])
def create_ninja():
    Ninja.save(request.form)
    return redirect('/dojos')

@app.route('/dojos/<int:id>')
def show_dojo(id):
    data = {'id': id}
    dojo = Dojo.get_dojo_with_ninjas(data)
    return render_template('show.html', dojo=dojo)