from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.pupil import Pupil
import repositories.pupil_repository as pupil_repository

pupils_blueprint = Blueprint("pupils", __name__)

