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
@noks_blueprint.route("/noks", methods=['POST'])
def create_nok():
    name = request.form['name']
    contact_number = request.form['contact_number']
    address = request.form['address']
    postcode = request.form['postcode']
    nok = NextOfKin(name, contact_number, address, postcode)
    nok_repository.save(nok)
    return redirect('/noks')


#SHOW - GET '/noks/<id>'
@noks_blueprint.route("/noks/<id>", methods=['GET'])
def show_nok(id):
    nok = nok_repository.select(id)
    return render_template('noks/show.html', nok=nok)


#EDIT - GET '/noks/<id>/edit'


#UPDATE - POST '/noks/<id>'


#DELETE - '/noks/<id>'