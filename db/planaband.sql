
DROP TABLE attendances;
DROP TABLE lessons;
DROP TABLE pupils;
DROP TABLE tutors;
DROP TABLE noks;

CREATE TABLE tutors (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    contact_number VARCHAR(255),
    address VARCHAR(255),
    postcode VARCHAR(10)
);

CREATE TABLE noks (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    contact_number VARCHAR(255),
    address VARCHAR(255),
    postcode VARCHAR(10),
    account INT
);

CREATE TABLE pupils (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    dob DATE,
    instrument VARCHAR(255),
    grade VARCHAR(255),
    nok_id INT REFERENCES noks(id) ON DELETE CASCADE,
    notes VARCHAR(255), 
    active BOOLEAN
);

CREATE TABLE lessons (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    date DATE,
    time VARCHAR(255),
    instrument VARCHAR(255),
    tutor_id INT REFERENCES tutors(id) ON DELETE CASCADE,
    max_capacity INT,
    group_status BOOLEAN
);

CREATE TABLE attendances (
    id SERIAL PRIMARY KEY,
    lesson_id INT REFERENCES lessons(id) ON DELETE CASCADE,
    pupil_id INT REFERENCES pupils(id) ON DELETE CASCADE,
    attended BOOLEAN
);


INSERT INTO tutors (name, contact_number, address, postcode) VALUES ('Remus Lupin', '07777 111222', 'Hogwarts School', 'IV11 1AA');
INSERT INTO tutors (name, contact_number, address, postcode) VALUES ('Minerva McGonagall', '07777 111333', 'Hogwarts School', 'IV11 1AA');
INSERT INTO tutors (name, contact_number, address, postcode) VALUES ('Professor Sprout', '07777 111444', 'Hogwarts School', 'IV11 1AA');
INSERT INTO tutors (name, contact_number, address, postcode) VALUES ('Severus Snape', '07777 111555', 'Hogwarts School', 'IV11 1AA');
INSERT INTO tutors (name, contact_number, address, postcode) VALUES ('Sybill Trelawney', '07777 111666', 'Hogwarts School', 'IV11 1AA');

INSERT INTO noks (name, contact_number, address, postcode, account) VALUES ('The Dursleys', '07777 222333', '4 Privet Drive', 'GU1 1AA', 0.00);
INSERT INTO noks (name, contact_number, address, postcode, account) VALUES ('Mrs Granger', '07777 222444', 'Hampstead Green', 'W1A', 0.00);
INSERT INTO noks (name, contact_number, address, postcode, account) VALUES ('Mrs Weasley', '07777 222555', 'The Burrow', 'Surrey', 0.00);
INSERT INTO noks (name, contact_number, address, postcode, account) VALUES ('Mr Malfoy', '07777 222666', 'Malfoy Manor', 'W1A', 0.00);

INSERT INTO pupils (name, dob, instrument, grade, nok_id, notes, active) VALUES ('Harry Potter', '2010-07-31', 'Piano', 4, 1, 'sample notes', true);
INSERT INTO pupils (name, dob, instrument, grade, nok_id, notes, active) VALUES ('Hermione Granger', '2009-09-19', 'Recorder', 8, 2, 'sample notes', true);
INSERT INTO pupils (name, dob, instrument, grade, nok_id, notes, active) VALUES ('Ron Weasley', '2010-03-01', 'Recorder', 2, 3, 'sample notes', true);
INSERT INTO pupils (name, dob, instrument, grade, nok_id, notes, active) VALUES ('Ginny Weasley', '2014-11-11', 'Violin', 1, 3, 'sample notes', true);
INSERT INTO pupils (name, dob, instrument, grade, nok_id, notes, active) VALUES ('Draco Malfoy', '2012-06-05', 'Saxophone', 3, 4, 'sample notes', true);

INSERT INTO lessons (name, date, time, instrument, tutor_id, max_capacity, group_status) VALUES ('Recorder Group', '2021-12-05', '10am', 'Recorder', 1, 3, true);
INSERT INTO lessons (name, date, time, instrument, tutor_id, max_capacity, group_status) VALUES ('Recorder Group', '2021-12-12', '10am', 'Recorder', 1, 3, true);
INSERT INTO lessons (name, date, time, instrument, tutor_id, max_capacity, group_status) VALUES ('Recorder Group', '2022-02-06', '10am', 'Recorder', 1, 3, true);
INSERT INTO lessons (name, date, time, instrument, tutor_id, max_capacity, group_status) VALUES ('Recorder Group', '2022-02-13', '10am', 'Recorder', 1, 3, true);
INSERT INTO lessons (name, date, time, instrument, tutor_id, max_capacity, group_status) VALUES ('Recorder Group', '2022-02-20', '10am', 'Recorder', 1, 3, true);
INSERT INTO lessons (name, date, time, instrument, tutor_id, max_capacity, group_status) VALUES ('Piano 1:1', '2021-12-05', '11am', 'Piano', 2, 1, false);
INSERT INTO lessons (name, date, time, instrument, tutor_id, max_capacity, group_status) VALUES ('Piano 1:1', '2021-12-12', '11am', 'Piano', 2, 1, false);
INSERT INTO lessons (name, date, time, instrument, tutor_id, max_capacity, group_status) VALUES ('Piano 1:1', '2022-02-06', '11am', 'Piano', 2, 1, false);
INSERT INTO lessons (name, date, time, instrument, tutor_id, max_capacity, group_status) VALUES ('Piano 1:1', '2022-02-13', '11am', 'Piano', 2, 1, false);
INSERT INTO lessons (name, date, time, instrument, tutor_id, max_capacity, group_status) VALUES ('Piano 1:1', '2022-02-20', '11am', 'Piano', 2, 1, false);
INSERT INTO lessons (name, date, time, instrument, tutor_id, max_capacity, group_status) VALUES ('String Ensemble', '2021-12-05', '12pm', 'Strings', 3, 3, true);
INSERT INTO lessons (name, date, time, instrument, tutor_id, max_capacity, group_status) VALUES ('String Ensemble', '2021-12-12', '12pm', 'Strings', 3, 3, true);
INSERT INTO lessons (name, date, time, instrument, tutor_id, max_capacity, group_status) VALUES ('String Ensemble', '2022-02-06', '12pm', 'Strings', 3, 3, true);
INSERT INTO lessons (name, date, time, instrument, tutor_id, max_capacity, group_status) VALUES ('String Ensemble', '2022-02-13', '12pm', 'Strings', 3, 3, true);
INSERT INTO lessons (name, date, time, instrument, tutor_id, max_capacity, group_status) VALUES ('String Ensemble', '2022-02-20', '12pm', 'Strings', 3, 3, true);
INSERT INTO lessons (name, date, time, instrument, tutor_id, max_capacity, group_status) VALUES ('Saxophone 1:1', '2021-12-05', '9am', 'Saxophone', 5, 1, false);
INSERT INTO lessons (name, date, time, instrument, tutor_id, max_capacity, group_status) VALUES ('Saxophone 1:1', '2021-12-12', '9am', 'Saxophone', 5, 1, false);
INSERT INTO lessons (name, date, time, instrument, tutor_id, max_capacity, group_status) VALUES ('Saxophone 1:1', '2022-02-06', '9am', 'Saxophone', 5, 1, false);
INSERT INTO lessons (name, date, time, instrument, tutor_id, max_capacity, group_status) VALUES ('Saxophone 1:1', '2022-02-13', '9am', 'Saxophone', 5, 1, false);
INSERT INTO lessons (name, date, time, instrument, tutor_id, max_capacity, group_status) VALUES ('Saxophone 1:1', '2022-02-20', '9am', 'Saxophone', 5, 1, false);

INSERT INTO attendances(lesson_id, pupil_id, attended) VALUES (1, 2, true);
INSERT INTO attendances(lesson_id, pupil_id, attended) VALUES (1, 3, true);
INSERT INTO attendances(lesson_id, pupil_id, attended) VALUES (2, 2, true);
INSERT INTO attendances(lesson_id, pupil_id, attended) VALUES (2, 3, true);
INSERT INTO attendances(lesson_id, pupil_id, attended) VALUES (3, 2, false);
INSERT INTO attendances(lesson_id, pupil_id, attended) VALUES (3, 3, false);
-- INSERT INTO attendances(lesson_id, pupil_id, attended) VALUES (3, 1, false);
INSERT INTO attendances(lesson_id, pupil_id, attended) VALUES (4, 2, false);
INSERT INTO attendances(lesson_id, pupil_id, attended) VALUES (4, 3, false);
INSERT INTO attendances(lesson_id, pupil_id, attended) VALUES (5, 2, false);
INSERT INTO attendances(lesson_id, pupil_id, attended) VALUES (5, 3, false);
INSERT INTO attendances(lesson_id, pupil_id, attended) VALUES (6, 1, true);
INSERT INTO attendances(lesson_id, pupil_id, attended) VALUES (7, 1, true);
INSERT INTO attendances(lesson_id, pupil_id, attended) VALUES (8, 1, false);
INSERT INTO attendances(lesson_id, pupil_id, attended) VALUES (9, 1, false);
INSERT INTO attendances(lesson_id, pupil_id, attended) VALUES (10, 1, false);
INSERT INTO attendances(lesson_id, pupil_id, attended) VALUES (11, 2, true);
INSERT INTO attendances(lesson_id, pupil_id, attended) VALUES (11, 4, true);
INSERT INTO attendances(lesson_id, pupil_id, attended) VALUES (12, 2, true);
INSERT INTO attendances(lesson_id, pupil_id, attended) VALUES (12, 4, true);
INSERT INTO attendances(lesson_id, pupil_id, attended) VALUES (13, 2, false);
INSERT INTO attendances(lesson_id, pupil_id, attended) VALUES (13, 4, false);
INSERT INTO attendances(lesson_id, pupil_id, attended) VALUES (13, 1, false);
INSERT INTO attendances(lesson_id, pupil_id, attended) VALUES (14, 2, false);
INSERT INTO attendances(lesson_id, pupil_id, attended) VALUES (14, 4, false);
INSERT INTO attendances(lesson_id, pupil_id, attended) VALUES (14, 1, false);
INSERT INTO attendances(lesson_id, pupil_id, attended) VALUES (15, 2, false);
INSERT INTO attendances(lesson_id, pupil_id, attended) VALUES (15, 4, false);
INSERT INTO attendances(lesson_id, pupil_id, attended) VALUES (16, 5, false);
INSERT INTO attendances(lesson_id, pupil_id, attended) VALUES (17, 5, false);
INSERT INTO attendances(lesson_id, pupil_id, attended) VALUES (18, 5, false);
INSERT INTO attendances(lesson_id, pupil_id, attended) VALUES (19, 5, false);
INSERT INTO attendances(lesson_id, pupil_id, attended) VALUES (20, 5, false);



