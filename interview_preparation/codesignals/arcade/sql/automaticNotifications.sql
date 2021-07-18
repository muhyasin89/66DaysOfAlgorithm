CREATE PROCEDURE automaticNotifications()
    SELECT email
    FROM users
    WHERE ROLE NOT IN ("admin", "premium")

    ORDER BY email;
