-- create trigger
CREATE
TRIGGER trigger_name
AFTER INSERT
ON orders FOR EACH ROW
UPDATE items SET quantity = quantity - NEW.number WHERE items.name = NEW.item_name;
