from db.run_sql import run_sql

from models.lesson import Lesson
from models.tutor import Tutor
import repositories.lesson_repository as lesson_repository
import repositories.tutor_repository as tutor_repository


def save(lesson):
    sql = "INSERT INTO lessons (name, date, instrument, tutor_id, group_status) VALUES (%s, %s, %s, %s, %s) RETURNING id"
    values = [lesson.name, lesson.date, lesson.instrument, lesson.tutor.id, lesson.group_status]
    results = run_sql(sql, values)
    id = results[0]['id']
    lesson.id = id
    return lesson


def select_all():
    lessons = []

    sql = "SELECT * FROM lessons"
    results = run_sql(sql)

    for row in results:
        tutor = tutor_repository.select(row['tutor_id'])
        lesson = Lesson(row['name'], row['date'], row['instrument'], tutor, row['group_status'], row['id'])
        lessons.append(lesson)
    return lessons


def select(id):
    lesson = None
    sql = "SELECT * FROM lessons WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        tutor = tutor_repository.select(result['tutor_id'])
        lesson = Lesson(result['name'], result['date'], result['instrument'], tutor, result['group_status'], result['id'])
    return lesson


def update(lesson):
    sql = "UPDATE lessons SET (name, date, instrument, tutor_id, group_status) = (%s, %s, %s, %s, %s) WHERE id = %s"
    values = [lesson.name, lesson.date, lesson.instrument, lesson.tutor.id, lesson.group_status, lesson.id]
    run_sql(sql, values)


def delete(id):
    sql = "DELETE FROM lessons WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def delete_all():
    sql = "DELETE FROM lessons"
    run_sql(sql)