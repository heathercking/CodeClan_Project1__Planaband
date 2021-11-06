from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.nok import NextOfKin
import repositories.nok_repository as nok_repository

noks_blueprint = Blueprint("noks", __name__)


@noks_blueprint.route("/noks")
def noks():
    noks = nok_repository.select_all()
    return render_template("noks/index.html", all_noks=noks)


# NEW - GET '/noks/new'
@noks_blueprint.route("/noks/new", methods=['GET'])
def new_nok():
    noks = nok_repository.select_all()
    return render_template("noks/new.html", all_noks=noks)


#CREATE - POST '/noks'


#SHOW - GET '/noks/<id>'


#EDIT - GET '/noks/<id>/edit'


#UPDATE - POST '/noks/<id>'


#DELETE - '/noks/<id>'