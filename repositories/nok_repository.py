from db.run_sql import run_sql

from models.nok import NextOfKin
import repositories.nok_repository as nok_repository


def save(nok):
    sql = "INSERT INTO noks (name, contact_number, address, postcode, account) VALUES (%s, %s, %s, %s, %s) RETURNING id"
    values = [nok.name, nok.contact_number, nok.address, nok.postcode, nok.account]
    results = run_sql(sql, values)
    nok.id = results[0]['id']
    return nok


def select_all():
    noks = []

    sql = "SELECT * FROM noks"
    results = run_sql(sql)

    for row in results:
        nok = NextOfKin(row['name'], row['contact_number'], row['address'], row['postcode'], row['account'], row['id'])
        noks.append(nok)
    return noks


def select(id):
    nok = None
    sql = "SELECT * FROM noks WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        nok = NextOfKin(result['name'], result['contact_number'], result['address'], result['postcode'], result['account'], result['id'])
    return nok


def update(nok):
    sql = "UPDATE noks SET (name, contact_number, address, postcode, account) = (%s, %s, %s, %s, %s) WHERE id = %s"
    values = [nok.name, nok.contact_number, nok.address, nok.postcode, nok.account, nok.id]
    run_sql(sql, values)


def delete(id):
    sql = "DELETE FROM noks WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def delete_all():
    sql = "DELETE FROM noks"
    run_sql(sql)