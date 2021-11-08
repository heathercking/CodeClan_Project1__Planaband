
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
    postcode VARCHAR(10)
);

CREATE TABLE pupils (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    dob DATE,
    instrument VARCHAR(255),
    grade VARCHAR(255),
    nok_id INT REFERENCES noks(id) ON DELETE CASCADE,
    notes VARCHAR(255)
);

CREATE TABLE lessons (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    date DATE,
    time VARCHAR(255),
    instrument VARCHAR(255),
    tutor_id INT REFERENCES tutors(id) ON DELETE CASCADE,
    group_status BOOLEAN
);

CREATE TABLE attendances (
    id SERIAL PRIMARY KEY,
    lesson_id INT REFERENCES lessons(id) ON DELETE CASCADE,
    pupil_id INT REFERENCES pupils(id) ON DELETE CASCADE,
    attended BOOLEAN
);


-- INSERT INTO tutors (name, contact_number, address, postcode) VALUES ('Rubeus Hagrid', '07999 777888', 'Hagrids Hut, Hogwarts School', 'EH42 2DD');

-- INSERT INTO noks (name, contact_number, address, postcode) VALUES ('Lily Potter', '07777 888999', 'The Potter Cottage, Godrics Hollow', 'EH53 9AZ');

-- INSERT INTO pupils (name, dob, instrument, grade, nok_id, notes) VALUES ('Harry Potter', DATE '2010-7-31', 'Piano', '4', 1, 'Sat grade 4 exam in April');

-- INSERT INTO lessons (name, date, instrument, group_status, tutor_id) VALUES ('Beginner Recorder', DATE '2021-11-27', 'Recorder', True, 1);

-- INSERT INTO attendances (lesson_id, pupil_id, attended) VALUES (1, 1, True);