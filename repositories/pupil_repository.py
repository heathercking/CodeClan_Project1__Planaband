from re import S
from db.run_sql import run_sql

from models.pupil import Pupil
import repositories.pupil_repository as pupil_repository

def save(pupil):
    sql = "INSERT INTO pupils (name, dob, instrument, grade, notes, nok_id) VALUES (%s, %s, %s, %s, %s, %s)"
    values = [pupil.name, pupil.dob, pupil.instrument, pupil.grade, pupil.notes, pupil.nok.id]
    results = run_sql(sql, values)
    pupil.id = results[0]['id']
    return pupil

