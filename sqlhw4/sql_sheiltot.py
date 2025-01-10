# 1
# CREATE TABLE courses (
#     course_id INTEGER PRIMARY KEY AUTOINCREMENT,
#     topic TEXT NOT NULL,
#     hours INTEGER NOT NULL
# );

# CREATE TABLE students (
#     student_id INTEGER PRIMARY KEY AUTOINCREMENT,
#     name TEXT NOT NULL,
#     email TEXT NOT NULL
# );

# CREATE TABLE grades (
#     course_id INTEGER NOT NULL,
#     student_id INTEGER NOT NULL,
#     grade INTEGER NOT NULL,
# 	PRIMARY KEY(course_id, student_id)
# 	FOREIGN KEY (course_id) REFERENCES courses(course_id)
# 	FOREIGN KEY (student_id) REFERENCES students(student_id)
# 	);

# 2
# INSERT INTO courses (topic, hours) VALUES ('history', 4);
# INSERT INTO courses (topic, hours) VALUES ('mathematics', 8);
# INSERT INTO courses (topic, hours) VALUES ('sport', 4);
# INSERT INTO courses (topic, hours) VALUES ('law', 5);

# INSERT INTO students (name, email) VALUES ('Daniel', 'daniilabramov@gmail.com');
# INSERT INTO students (name, email) VALUES ('David', 'davidlard@gmail.com');
# INSERT INTO students (name, email) VALUES ('Adam', 'adamov@gmail.com');
# INSERT INTO students (name, email) VALUES ('Anat', 'anata2@gmail.com');

# INSERT INTO grades (course_id, student_id, grade) VALUES (1, 1, 80);
# INSERT INTO grades (course_id, student_id, grade) VALUES (1, 2, 70);
# INSERT INTO grades (course_id, student_id, grade) VALUES (1, 3, 95);
# INSERT INTO grades (course_id, student_id, grade) VALUES (1, 4, 70);
# INSERT INTO grades (course_id, student_id, grade) VALUES (2, 1, 80);
# INSERT INTO grades (course_id, student_id, grade) VALUES (2, 2, 70);
# INSERT INTO grades (course_id, student_id, grade) VALUES (2, 3, 70);
# INSERT INTO grades (course_id, student_id, grade) VALUES (2, 4, 80);
# INSERT INTO grades (course_id, student_id, grade) VALUES (3, 1, 75);
# INSERT INTO grades (course_id, student_id, grade) VALUES (3, 2, 88);
# INSERT INTO grades (course_id, student_id, grade) VALUES (3, 3, 70);
# INSERT INTO grades (course_id, student_id, grade) VALUES (3, 4, 99);
# INSERT INTO grades (course_id, student_id, grade) VALUES (4, 1, 85);
# INSERT INTO grades (course_id, student_id, grade) VALUES (4, 2, 60);
# INSERT INTO grades (course_id, student_id, grade) VALUES (4, 3, 80);
# INSERT INTO grades (course_id, student_id, grade) VALUES (4, 4, 70);

# 3
# SELECT avg(grade) FROM grades
# GROUP by course_id
