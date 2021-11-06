from flask import Flask, render_template, request, redirect

from flask import Blueprint
from models.attendance import Attendance
from models.lesson import Lesson
from models.pupil import Pupil

import repositories.attendance_repository as attendance_repository
import repositories.lesson_repository as lesson_repository
import repositories.pupil_repository as pupil_repository

attendances_blueprint = Blueprint("attendances", __name__)


@attendances_blueprint.route("/attendances")
def attendances():
    attendances = attendance_repository.select_all()
    return render_template("attendances/index.html", all_attendances=attendances)


#NEW - GET '/attendances/new'
@attendances_blueprint.route("/attendances/new", methods=['GET'])
def new_attendance():
    lessons = lesson_repository.select_all()
    pupils = pupil_repository.select_all()
    return render_template("attendances/new.html", all_lessons=lessons, all_pupils=pupils)
    