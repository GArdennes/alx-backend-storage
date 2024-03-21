-- ComputeAverageScoreForUser that computes and stores the average score for a student.
DROP PROCEDURE IF EXISTS ComputeAverageScoreForUser;
CREATE PROCEDURE ComputeAverageScoreForUser(
  IN user_id INT,
)
BEGIN
   -- Calculate total score and number of scores for the user
  SELECT SUM(score), COUNT(*)
  INTO total_score, num_scores
  FROM student_scores  -- Assuming a table with student scores
  WHERE user_id = user_id;

  -- Calculate average score (handle division by zero)
  IF num_scores > 0 THEN
    SET average_score = total_score / num_scores;
  ELSE
    SET average_score = NULL;  -- Set NULL for no scores
  END IF;

  -- Update student record with average score
  UPDATE students
  SET average_score = average_score
  WHERE id = user_id;
END;
