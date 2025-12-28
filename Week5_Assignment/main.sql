-- Create Students table
CREATE TABLE Students (
    student_id INT PRIMARY KEY,
    name VARCHAR(50),
    age INT,
    city VARCHAR(30),
    marks INT
);

-- Inserting values into Students table
INSERT INTO Students VALUES
(1, 'Suraj Goyal', 21, 'Mumbai', 45),
(2, 'Shyam Pathak', 24, 'Delhi', 74),
(3, 'Amit Kumar', 19, 'Guwahati', 78),
(4, 'Sneha Roy', 22, 'Delhi', 88),
(5, 'Vikash Singh', 20, 'Guwahati', 95);

-- Create Courses table
CREATE TABLE Courses (
    course_id INT PRIMARY KEY,
    course_name VARCHAR(30),
    credits INT
);

-- Inserting values into Courses table
INSERT INTO Courses VALUES
(101, 'DBMS', 4),
(102, 'Data Science', 4),
(103, 'Machine Learning', 3),
(104, 'Web Development', 3);

-- LOGICAL OPERATORS QUERIES:
-- AND: Students from Guwahati AND age > 19
SELECT name, age, city FROM Students 
WHERE city = 'Guwahati' AND age > 19;

-- OR: Students from Delhi OR marks > 80
SELECT name, marks FROM Students 
WHERE city = 'Delhi' OR marks > 80;

-- NOT: Students NOT from Mumbai
SELECT name, city FROM Students 
WHERE NOT city = 'Mumbai';

-- ARITHMETIC OPERATORS:
-- COUNT: Total students
SELECT COUNT(*) as total_students FROM Students;

-- AVG: Average marks
SELECT AVG(marks) as avg_marks FROM Students;

-- SUM: Total credits (fixed from fees since Courses has credits)
SELECT SUM(credits) as total_credits FROM Courses;

-- ORDER BY QUERIES:
-- ORDER BY marks DESC (highest first)
SELECT name, marks FROM Students 
ORDER BY marks DESC;

-- ORDER BY age ASC, marks DESC (two columns) - FIXED semicolon
SELECT name, age, marks FROM Students 
ORDER BY age ASC, marks DESC;
