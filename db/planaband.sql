DROP TABLE lessons;
DROP TABLE pupils;
DROP TABLE tutors;
DROP TABLE nok;

CREATE TABLE tutors (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    contact_number VARCHAR(255),
    address VARCHAR(255),
    postcode VARCHAR(10)
);

CREATE TABLE nok (
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
    notes VARCHAR(255),
    nok_id INT REFERENCES nok(id)
);

CREATE TABLE lessons (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    date DATE,
    instrument VARCHAR(255),
    group_status BOOLEAN,
    tutor_id INT REFERENCES tutors(id)
);