import re
from flask import Flask, render_template, request, redirect

from flask import Blueprint
from models.pupil import Pupil
from models.nok import NextOfKin

import repositories.pupil_repository as pupil_repository
import repositories.nok_repository as nok_repository

pupils_blueprint = Blueprint("pupils", __name__)


@pupils_blueprint.route("/pupils")
def pupils():
    pupils = pupil_repository.select_all()
    return render_template("pupils/index.html", all_pupils=pupils)


#NEW - GET '/pupils/new'
@pupils_blueprint.route("/pupils/new", methods=['GET'])
def new_pupil():
    noks = nok_repository.select_all()
    return render_template("pupils/new.html", all_noks=noks)


#CREATE - POST '/pupils'
@pupils_blueprint.route("/pupils", methods=['POST'])
def create_pupil():
    name = request.form['name']
    dob = request.form['dob']
    instrument = request.form['instrument']
    grade = request.form['grade']
    nok = nok_repository.select(request.form['nok_id'])
    notes = request.form['notes']
    active = True
    pupil = Pupil(name, dob, instrument, grade, nok, notes, active)
    pupil_repository.save(pupil)
    return redirect('/pupils')


#SHOW - GET '/pupils/<id>'
@pupils_blueprint.route("/pupils/<id>", methods=['GET'])
def show_pupil(id):
    pupil = pupil_repository.select(id)
    lessons = pupil_repository.lessons(pupil)
    attendances = pupil_repository.attendances(pupil)
    return render_template('pupils/show.html', pupil=pupil, lessons=lessons, attendances=attendances)


#SHOW archive - GET '/pupils/<id>/archive'
@pupils_blueprint.route("/pupils/<id>/archive", methods=['GET'])
def show_pupil_archive(id):
    pupil = pupil_repository.select(id)
    lessons = pupil_repository.lessons(pupil)
    attendances = pupil_repository.attendances(pupil)
    return render_template('pupils/show_archive.html', pupil=pupil, lessons=lessons, attendances=attendances)


#EDIT - GET '/pupils/<id>/edit'
@pupils_blueprint.route("/pupils/<id>/edit", methods=['GET'])
def edit_pupils(id):
    pupil = pupil_repository.select(id)
    noks = nok_repository.select_all()
    return render_template('pupils/edit.html', pupil=pupil, all_noks=noks)


#UPDATE - POST '/pupils/<id>'
@pupils_blueprint.route("/pupils/<id>", methods=['POST'])
def update_pupil(id):
    name = request.form['name']
    dob = request.form['dob']
    instrument = request.form['instrument']
    grade = request.form['grade']
    nok = nok_repository.select(request.form['nok_id'])
    notes = request.form['notes']
    active = request.form['active']
    pupil = Pupil(name, dob, instrument, grade, nok, notes, active, id)
    pupil_repository.update(pupil)
    return redirect('/pupils')


#DELETE - '/pupils/<id>'
@pupils_blueprint.route("/pupils/<id>/delete", methods=['POST'])
def delete_pupil(id):
    pupil_repository.delete(id)
    return redirect('/pupils')