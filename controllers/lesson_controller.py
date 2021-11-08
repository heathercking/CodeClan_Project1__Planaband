from flask import Flask, render_template, request, redirect

from flask import Blueprint
from models.lesson import Lesson
from models.tutor import Tutor

import repositories.lesson_repository as lesson_repository
import repositories.tutor_repository as tutor_repository

lessons_blueprint = Blueprint("lessons", __name__)


@lessons_blueprint.route("/lessons")
def lessons():
    lessons = lesson_repository.select_all()
    return render_template("lessons/index.html", all_lessons=lessons)


# displays all lessons with spaces - on filter button click
@lessons_blueprint.route("/lessons/spaces")
def lessons_spaces():
    lessons = lesson_repository.select_all()
    return render_template("lessons/spaces.html", all_lessons=lessons)


#NEW - GET '/lessons/new'
@lessons_blueprint.route("/lessons/new", methods=['GET'])
def new_lesson():
    tutors = tutor_repository.select_all()
    return render_template("lessons/new.html", all_tutors=tutors)


#CREATE - POST '/lessons'
@lessons_blueprint.route("/lessons", methods=['POST'])
def create_lesson():
    name = request.form['name']
    date = request.form['date']
    time = request.form['time']
    instrument = request.form['instrument']
    tutor = tutor_repository.select(request.form['tutor_id'])
    max_capacity = request.form['max_capacity']
    group_status = request.form['group_status']
    lesson = Lesson(name, date, time, instrument, tutor, max_capacity, group_status)
    lesson_repository.save(lesson)
    return redirect('/lessons')


#SHOW - GET '/lessons/<id>'
@lessons_blueprint.route("/lessons/<id>", methods=['GET'])
def show_lesson(id):
    lesson = lesson_repository.select(id)
    lesson.attendees = lesson_repository.attendances(lesson)
    pupils = lesson_repository.pupils(lesson)
    attendances = lesson_repository.attendances(lesson)
    return render_template('lessons/show.html', lesson=lesson, pupils=pupils, attendances=attendances)


#EDIT - GET '/lessons/<id>/edit'
@lessons_blueprint.route("/lessons/<id>/edit", methods=['GET'])
def edit_lessons(id):
    lesson = lesson_repository.select(id)
    tutors = tutor_repository.select_all()
    return render_template('lessons/edit.html', lesson=lesson, all_tutors=tutors)


#UPDATE - POST '/lessons/<id>'
@lessons_blueprint.route("/lessons/<id>", methods=['POST'])
def update_lesson(id):
    name = request.form['name']
    date = request.form['date']
    time = request.form['time']
    instrument = request.form['instrument']
    tutor = tutor_repository.select(request.form['tutor_id'])
    max_capacity = request.form['max_capacity']
    group_status = request.form['group_status']
    lesson = Lesson(name, date, time, instrument, tutor, max_capacity, group_status, id)
    lesson_repository.update(lesson)
    return redirect('/lessons')


#DELETE - '/lessons/<id>'
@lessons_blueprint.route("/lessons/<id>/delete", methods=['POST'])
def delete_lesson(id):
    lesson_repository.delete(id)
    return redirect('/lessons')