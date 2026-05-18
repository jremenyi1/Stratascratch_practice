-- Platform: StrataScratch
-- Difficulty: Easy
-- Question ID: 2002
-- Problem:
-- Return user IDs of users who created
-- at least one 'Refinance' submission, 
-- and at least one 'InSchool' submission.
--
-- Table: loans
-- Columns: created_at, id, status, type, user_id

SELECT user_id
FROM loans
WHERE type IN ('Refinance', 'InSchool')
GROUP BY user_id
HAVING COUNT(DISTINCT type) = 2;