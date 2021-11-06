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

#CREATE - POST '/pupil'


#SHOW - GET '/pupils/<id>'


#EDIT - GET '/pupils/<id>/edit'


#UPDATE - POST '/pupils/<id>'


#DELETE - '/pupils/<id>'