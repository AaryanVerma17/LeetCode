# Write your MySQL query statement below
SELECT email from Person AS Email
GROUP BY Email
HAVING COUNT(email) > 1;