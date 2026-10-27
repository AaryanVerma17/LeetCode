# Write your MySQL query statement below
SELECT class
FROM Courses
Group by class
Having Count(*) >= 5;