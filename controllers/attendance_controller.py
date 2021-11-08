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


#CREATE - POST '/attendances'
@attendances_blueprint.route("/attendances", methods=['POST'])
def create_attendance():
    lesson = lesson_repository.select(request.form['lesson_id'])
    pupil = pupil_repository.select(request.form['pupil_id'])
    attended = request.form['attended']
    attendance = Attendance(lesson, pupil, attended)
    attendance_repository.save(attendance)
    return redirect('/attendances')


#EDIT - GET '/attendances/<id>/edit'
@attendances_blueprint.route("/attendances/<id>/edit", methods=['GET'])
def edit_attendances(id):
    attendance = attendance_repository.select(id)
    lessons = lesson_repository.select_all()
    pupils = pupil_repository.select_all()
    return render_template('attendances/edit.html', attendance=attendance, all_lessons=lessons, all_pupils=pupils)


#UPDATE - POST '/attendances/<id>'
@attendances_blueprint.route("/attendances/<id>", methods=['POST'])
def update_attendances(id):
    lesson = lesson_repository.select(request.form['lesson_id'])
    pupil = pupil_repository.select(request.form['pupil_id'])
    attended = request.form['attended']
    attendance = Attendance(lesson, pupil, attended, id)
    attendance_repository.update(attendance)
    return redirect('/attendances')


#DELETE - '/attendances/<id>/delete'
@attendances_blueprint.route("/attendances/<id>/delete", methods=['POST'])
def delete_attendance(id):
    attendance_repository.delete(id)
    return redirect('/attendances')

#UPDATE - POST - MARK ATTENDED 'attendances/<id>/attended'
@attendances_blueprint.route("/attendances/<id>/attended", methods=['POST'])
def mark_attended(id):
    attendance = attendance_repository.select(id)
    attendance.mark_attended()
    attendance_repository.update(attendance)
    return redirect('/attendances')