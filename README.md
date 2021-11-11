**CODECLAND PROJECT 1 - Planaband**

**THE BRIEF**

Build a piece of software for a music school, which will help them administer/manage the school. 


**MVP - the must haves**

- create and edit pupils, including basic details, and next of kin contact details 
- create and edit group lessons - and book pupils into/remove from the lessons
- create and edit tutors
- assign tutors to lessons
- list all lessons offered by the music school
- list pupils booked into lessons
- log pupil attendance


**Extensions - the should haves**

- log pupil attendance from the relevant lesson page
- add a maximum capacity to lessons - and only allow booking if there are spaces
- list all lessons with spaces
- filter lessons offered by the music school, by e.g. instrument type
- create a smooth pupi-enrol journey, combining the creation of a separate next-of-kin contact
- create a lesson and pupil archive


**Advanced Extensions - the could haves**

- list each tutor's lessons on their page (view schedule)
- display number of attendees against each lesson, as displayed on the tutor's page
- add an attendance rate to each pupil


**the wont haves (this time)**

- mark tutors as busy when allocated to a lesson
- show slots when tutors are free - and available for scheduling into lessons
- create and add examinations - graded instrumental exams, including:
    - Adding dates of examinations (date took place)
    - Results - date awarded, grade
- apply discounts for 
    - booking multiple terms
    - more than one child booked in (i.e. a parent has two children taking lessons)
        - (update NOK->Pupil relationship to many>many)



**THE SOLUTION**

Introducing Planaband - the music school admin app.

![Planaband](screenshots/Planaband_home.png)


**THE TECHNOLOGY**

Planaband has been built, so far, using Python, Flask(Jinja), HTML/CSS, and PostgreSQL and the psycopg package


**RUNNING INSTRUCTIONS**

1. set-up the database in command line:
    - run `createdb planaband`
    - run `psql -d planaband -f planaband.sql`

2. run flask from command line with `flask run`

3. in Chrome, go to localhost:5000


**REFERENCES**

- the CSS was informed by Brad Traversy's [repsonsive website build tutorial] (https://github.com/bradtraversy/loruki-website)
- the colour palete was taken from the [Studio Simpatico website] (https://studiosimpati.co/)
 
