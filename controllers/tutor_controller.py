from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.tutor import Tutor
import repositories.tutor_repository as tutor_repository

tutors_blueprint = Blueprint("tutors", __name__)

@tutors_blueprint.route("/tutors")
def tutors():
    tutors = tutor_repository.select_all()
    return render_template("tutors/index.html", all_tutors=tutors)


# NEW - GET '/tutors/new'
@tutors_blueprint.route("/tutors/new", methods=['GET'])
def new_tutor():
    tutors = tutor_repository.select_all()
    return render_template("tutors/new.html", all_tutors=tutors)

#CREATE - POST '/tutors'
@tutors_blueprint.route("/tutors", methods=['POST'])
def create_tutor():
    name = request.form['name']
    contact_number = request.form['contact_number']
    address = request.form['address']
    postcode = request.form['postcode']
    tutor = Tutor(name, contact_number, address, postcode)
    tutor_repository.save(tutor)
    return redirect('/tutors')

#SHOW - GET '/tutors/<id>'
@tutors_blueprint.route("/tutors/<id>", methods=['GET'])
def show_tutor(id):
    tutor = tutor_repository.select(id)
    return render_template('tutors/show.html', tutor=tutor)

#EDIT - GET '/tutors/<id>/edit'
@tutors_blueprint.route("/tutors/<id>/edit", methods=['GET'])
def edit_tutor(id):
    tutor = tutor_repository.select(id)
    return render_template('tutors/edit.html', tutor=tutor)

#UPDATE - POST '/tutors/<id>'
@tutors_blueprint.route("/tutors/<id>", methods=['POST'])
def update_tutor(id):
    name = request.form['name']
    contact_number = request.form['contact_number']
    address = request.form['address']
    postcode = request.form['postcode']
    tutor = Tutor(name, contact_number, address, postcode, id)
    tutor_repository.update(tutor)
    return redirect('/tutors')

#DELETE - 