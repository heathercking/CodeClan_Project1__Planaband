DROP TABLE attendances;
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

CREATE TABLE attendances (
    id SERIAL PRIMARY KEY,
    lesson_id INT REFERENCES lessons(id) ON DELETE CASCADE,
    pupil_id INT REFERENCES pupils(id) ON DELETE CASCADE,
    attended BOOLEAN
);


-- INSERT INTO tutors (name, contact_number, address, postcode) VALUES ("Rubeus Hagrid", "07999 777888", "Hagrid's Hut, Hogwarts School", "EH42 2DD")

-- INSERT INTO nok (name, contact_number, address, postcode) VALUES ("Lily Potter", "07777 888999", "The Potter Cottage, Godric's Hollow", "EH53 9AZ")

-- INSERT INTO pupils (name, dob, instrument, grade, notes)