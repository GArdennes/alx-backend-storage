-- Create an index on the first letter of name on the table names
CREATE INDEX idx_name_first ON names(LEFT(name, 1));
