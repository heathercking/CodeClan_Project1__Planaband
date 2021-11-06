from flask import Flask, render_template, request, redirect

from flask import Blueprint
from models.lesson import Lesson
from models.tutor import Tutor

import repositories.lesson_repository as lesson_repository
import repositories.tutor_repository as tutor_repository

lessons_blueprint = Blueprint("lessons", __name__)

