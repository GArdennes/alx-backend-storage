-- creates a trigger that resets the attribute valid_email when email has been changed
DROP TRIGGER IF EXISTS reset_email;
CREATE TRIGGER reset_email AFTER UPDATE ON users
FOR EACH ROW
BEGIN
  DECLARE old_email VARCHAR(255);
  
  -- Check if the email has actually changed
  SELECT OLD.email INTO old_email;
  IF NEW.email <> old_email THEN
    UPDATE users
    SET valid_email = 0
    WHERE id = OLD.id;
  END IF;
END;
