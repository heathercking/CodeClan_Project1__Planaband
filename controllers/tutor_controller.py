from flask import Flask, render_template
from flask import Blueprint
from models.tutor import Tutor
import repositories.tutor_repository as tutor_repository

tutors_blueprint = Blueprint("tutors", __name__)

