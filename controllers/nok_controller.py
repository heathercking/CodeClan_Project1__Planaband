from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.nok import NextOfKin
import repositories.nok_repository as nok_repository

noks_blueprint = Blueprint("noks", __name__)

# @noks_blueprint.route("/noks")
# def noks():

