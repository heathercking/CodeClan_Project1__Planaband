from db.run_sql import run_sql

from models.nok import NextOfKin
import repositories.nok_repository as nok_repository


def save(nok):
    sql = "INSERT INTO noks (name, contact_number, address, postcode) VALUES (%s, %s, %s, %s) RETURNING id"
    values = [nok.name, nok.contact_number, nok.address, nok.postcode]
    results = run_sql(sql, values)
    nok.id = results[0]['id']
    return nok

