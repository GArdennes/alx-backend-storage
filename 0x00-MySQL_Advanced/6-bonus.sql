-- creates a stored procedure AddBonus that adds a new correction for a student
DROP PROCEDURE IF EXISTS AddBonus;
CREATE PROCEDURE AddBonus(
  IN user_id INT,
  IN project_name VARCHAR(255),
  IN score INT
)
BEGIN
  DECLARE project_id INT;

  -- Check if project exists, insert if not
  SELECT id INTO project_id
  FROM projects
  WHERE name = project_name;

  IF project_id IS NULL THEN
    INSERT INTO projects (name)
    VALUES (project_name);
    SET project_id = LAST_INSERT_ID();
  END IF;

  -- Insert correction (assuming a corrections table)
  INSERT INTO corrections (user_id, project_id, score)
  VALUES (user_id, project_id, score);
END;
