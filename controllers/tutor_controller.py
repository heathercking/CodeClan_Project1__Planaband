from flask import Flask, render_template
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
