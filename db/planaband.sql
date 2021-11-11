
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