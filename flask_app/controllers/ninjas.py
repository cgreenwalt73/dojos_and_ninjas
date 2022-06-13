from flask_app import app
from flask import redirect, render_template, request, Flask
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo

@app.route('/new_ninja', methods=['POST', 'GET'])
def add_ninja():
    if request.method== 'GET':
        dojo_locations=Dojo.get_all_dojos()
        return render_template('add_ninja.html', dojo_locations=dojo_locations)
    else:
        data={
            'first_name' : request.form['first_name'],
            'last_name' : request.form['last_name'],
            'age' : request.form['age'],
            'dojo_id' : request.form['dojo_id']
        }
        Ninja.save(data)
        return redirect('/dojo_show/' + data['dojo_id'])