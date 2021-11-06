from db.run_sql import run_sql
from models.tutor import Tutor


def save(tutor):
    sql = "INSERT INTO tutors (name, contact_number, address, postcode) VALUES (%s, %s, %s, %s) RETURNING id"
    values = [tutor.name, tutor.contact_number, tutor.address, tutor.postcode]
    results = run_sql(sql, values)
    tutor.id = results[0]['id']
    return tutor
