from flask import Flask, render_template, request, redirect

from flask import Blueprint
from models.lesson import Lesson
from models.pupil import Pupil

import repositories.lesson_repository as lesson_repository
import repositories.pupil_repository as pupil_repository

attendances_blueprint = Blueprint("attendances", __name__)


