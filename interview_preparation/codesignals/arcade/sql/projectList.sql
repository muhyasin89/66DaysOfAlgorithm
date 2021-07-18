/*
    My answer is split existing table into two part
*/

-- CREATE PROCEDURE projectList()
-- BEGIN
-- 	/* Write your SQL here. Terminate each statement with a semicolon. */
--     CREATE TABLE ProjectsDetail (
--         internal_id int PRIMARY KEY,
--         project_name varchar(75),
--         team_size int
--     );
    
--     INSERT INTO ProjectsDetail (internal_id, project_name, team_size)
--     SELECT DISTINCT internal_id, project_name, team_size;
    
--     ALTER TABLE Projects DROP COLUMN internal_id, 
--     DROP COLUMN project_name, DROP COLUMN team_size;
-- END


/**
Real Answer:
 -- you only need to select not split them into 2 table
**/
CREATE PROCEDURE projectList()
BEGIN
    SELECT project_name, team_lead, income FROM Projects;
END