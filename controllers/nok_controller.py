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
    account = 0.00
    nok = NextOfKin(name, contact_number, address, postcode, account)
    nok_repository.save(nok)
    return redirect('/pupils')


#SHOW - GET '/noks/<id>'
@noks_blueprint.route("/noks/<id>", methods=['GET'])
def show_nok(id):
    nok = nok_repository.select(id)
    return render_template('noks/show.html', nok=nok)


#EDIT - GET '/noks/<id>/edit'
@noks_blueprint.route("/noks/<id>/edit", methods=['GET'])
def edit_nok(id):
    nok = nok_repository.select(id)
    return render_template('noks/edit.html', nok=nok)


#UPDATE - POST '/noks/<id>'
@noks_blueprint.route("/noks/<id>", methods=['POST'])
def update_nok(id):
    name = request.form['name']
    contact_number = request.form['contact_number']
    address = request.form['address']
    postcode = request.form['postcode']
    account = request.form['account']
    nok = NextOfKin(name, contact_number, address, postcode, account, id)
    nok_repository.update(nok)
    return redirect('/noks')


#DELETE - '/noks/<id>'
@noks_blueprint.route("/noks/<id>/delete", methods=['POST'])
def delete_nok(id):
    nok_repository.delete(id)
    return redirect('/noks')