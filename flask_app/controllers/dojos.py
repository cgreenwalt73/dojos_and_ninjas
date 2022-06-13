from flask_app import app
from flask import redirect, render_template, request, Flask
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja

@app.route('/')
def dojos():
    all_dojos=Dojo.get_all_dojos()
    return render_template('all_dojos.html', dojos=all_dojos)

@app.route('/add_dojo', methods=['POST'])
def add_dojo():
    data={
        'name':request.form['new_dojo']
    }
    Dojo.save(data)
    return redirect('/')

@app.route('/dojo_show/<int:id>')
def show_dojo(id):
    this_dojo=Dojo.get_one_dojo(id)
    these_ninjas= Ninja.get_ninjas_for_one_dojo(id)
    return render_template('dojo_show.html', this_dojo=this_dojo, these_ninjas=these_ninjas)