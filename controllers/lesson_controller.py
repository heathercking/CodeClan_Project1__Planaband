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
    instrument = request.form['instrument']
    tutor = tutor_repository.select(request.form['tutor_id'])
    group_status = request.form['group_status']
    lesson = Lesson(name, date, instrument, tutor, group_status)
    lesson_repository.save(lesson)
    return redirect('/lessons')