from db.run_sql import run_sql

from models.tutor import Tutor
import repositories.tutor_repository as tutor_repository



def save(tutor):
    sql = "INSERT INTO tutors (name, contact_number, address, postcode) VALUES (%s, %s, %s, %s) RETURNING id"
    values = [tutor.name, tutor.contact_number, tutor.address, tutor.postcode]
    results = run_sql(sql, values)
    tutor.id = results[0]['id']
    return tutor

def select_all():
    tutors = []

    sql = "SELECT * FROM tutors"
    results = run_sql(sql)

    for row in results:
        tutor = Tutor(row['name'], row['contact_number'], row['address'], row['postcode'], row['id'])
        tutors.append(tutor)
    return tutors

def select(id):
    tutor = None
    sql = "SELECT * FROM tutors WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        tutor = Tutor(result['name'], result['contact_number'], result['address'], result['postcode'], result['id'])
    return tutor