from flask import Flask, render_template

from controllers.tutor_controller import tutors_blueprint
from controllers.nok_controller import noks_blueprint
from controllers.pupil_controller import pupils_blueprint
from controllers.lesson_controller import lessons_blueprint
from controllers.attendance_controller import attendances_blueprint

app = Flask(__name__)

app.register_blueprint(tutors_blueprint)
app.register_blueprint(noks_blueprint)
app.register_blueprint(pupils_blueprint)
app.register_blueprint(lessons_blueprint)
app.register_blueprint(attendances_blueprint)


@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)