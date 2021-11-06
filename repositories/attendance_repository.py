from db.run_sql import run_sql

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