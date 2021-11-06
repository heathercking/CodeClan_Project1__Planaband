from db.run_sql import run_sql

from models.attendance import Attendance
from models.lesson import Lesson
from models.pupil import Pupil
import repositories.lesson_repository as lesson_repository
import repositories.pupil_repository as pupil_repository


def save(attendance):
    sql = "INSERT INTO attendances (lesson_id, pupil_id, attended) VALUES (%s, %s, %s) RETURNING id"
    values = [attendance.lesson.id, attendance.pupil.id, attendance.attended]
    results = run_sql(sql, values)
    id = results[0]['id']
    attendance.id = id
    return attendance


def select_all():
    attendances = []

    sql = "SELECT * FROM attendances"
    results = run_sql(sql)

    for row in results:
        lesson = lesson_repository.select(row['lesson_id'])
        pupil = pupil_repository.select(row['pupil_id'])
        attendance = Attendance(lesson, pupil, row['attended'], row['id'])
        attendances.append(attendance)
    return attendances


def select(id):
    attendance = None
    sql = "SELECT * FROM attendances WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        lesson = lesson_repository.select(result['lesson_id'])
        pupil = pupil_repository.select(result['pupil_id'])
        attendance = Attendance(lesson, pupil, result['attended'], result['id'])
    return attendance


def update(attendance):
    sql = "UPDATE attendances SET (lesson_id, pupil_id, attended) = (%s, %s, %s) WHERE id = %s"
    values = [attendance.lesson.id, attendance.pupil.id, attendance.attended, attendance.id]
    run_sql(sql, values)


def delete(id):
    sql = "DELETE FROM attendances WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def delete_all():
    sql = "DELETE FROM attendances"
    run_sql(sql)
