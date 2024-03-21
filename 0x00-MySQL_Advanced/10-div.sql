-- Creates a function that divides the first by the second number and returns the result
DROP FUNCTION IF EXISTS SafeDiv;
CREATE FUNCTION SafeDiv (
  a INT,
  b INT
)
RETURNS FLOAT DETERMINISTIC
BEGIN
  DECLARE result FLOAT;
  IF b <= 0 THEN
    RETURN 0;
  ELSE
    SET result = a / b;
  END IF;
  RETURN result;
END;
