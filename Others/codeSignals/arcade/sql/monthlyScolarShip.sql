CREATE PROCEDURE monthlyScholarships()
BEGIN
	/* Write your SQL here. Terminate each statement with a semicolon. */
    SELECT id,(scholarship/12)  FROM scholarships ORDER BY id;
END