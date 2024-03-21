-- creates a trigger that decreases the quantity
-- of an item after adding a new order
DROP TRIGGER IF EXISTS update_stock;
DELIMITER $$
CREATE TRIGGER update_stock AFTER INSERT ON Orders
FOR EACH ROW
BEGIN
    UPDATE items
    SET quantity = quantity - NEW.number
    WHERE name = NEW.item_name;
END $$
DELIMITER ;
