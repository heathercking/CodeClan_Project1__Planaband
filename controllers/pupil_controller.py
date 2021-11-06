from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.pupil import Pupil
import repositories.pupil_repository as pupil_repository

pupils_blueprint = Blueprint("pupils", __name__)


@pupils_blueprint.route("/pupils")
def pupils():
    pupils = pupil_repository.select_all()
    return render_template("pupils/index.html", all_pupils=pupils)
