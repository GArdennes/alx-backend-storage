-- Create a view that lists all students that meet the criteria
DROP VIEW IF EXISTS need_meeting;
CREATE VIEW need_meeting AS
SELECT name, score, last_meeting
FROM students
WHERE score < 80  -- Score strictly less than 80
AND (last_meeting IS NULL OR last_meeting < DATE_SUB(CURDATE(), INTERVAL 1 MONTH));
