--Transaction for potential_customers table.
BEGIN;
SAVEPOINT add_id34;
INSERT INTO potential_customers (id, email, name, surname, second_name, city)
VALUES (34, 'soroka@gmail.com', 'soryuu', 'okaqq', 'samsonovich', 'city 33');
DELETE FROM potential_customers
    WHERE id=31;
INSERT INTO potential_customers (id, email, name, surname, second_name, city)
VALUES (32, 'soroka@gmail.com', 'sorqw', 'oka', 'samsonovich', 'city 32');
UPDATE potential_customers
    SET email='pomenyala@gmail.com'
WHERE id= 29;
SAVEPOINT add_some;
DELETE FROM potential_customers
WHERE id=1;
SAVEPOINT del_id1;
DELETE FROM potential_customers
WHERE id=26;
SAVEPOINT del_26;
DELETE FROM potential_customers
WHERE id=28;
UPDATE potential_customers
    SET name='valera'
WHERE id=12;
SAVEPOINT up_some;
ROLLBACK TO SAVEPOINT add_id34;
COMMIT;


SELECT * FROM potential_customers;

--Transaction for categories table.
BEGIN ;
INSERT INTO categories(category_id, category_title, category_description)
VALUES (21, 'category 21', 'category 21 description');
SAVEPOINT del_21;
DELETE FROM categories
    WHERE category_id=21;
SAVEPOINT upd_3id;
UPDATE categories
    SET category_description='description 11.'
WHERE category_id=11;
ROLLBACK TO SAVEPOINT del_21;
COMMIT ;
ROLLBACK;


SELECT * FROM categories

--Transaction for cart table.
BEGIN;
INSERT INTO carts(cart_id, users_user_id, subtotal, total, timestamp)
VALUES (2005, 2005, 397.13, 397.13, '2021/10/11');
SAVEPOINT add_new;
UPDATE carts
SET total=1000
    WHERE cart_id=2;
SAVEPOINT upd_total;
DELETE FROM carts
    WHERE cart_id=2005;
SAVEPOINT del_subt;
ROLLBACK To SAVEPOINT upd_total;
ROLLBACK ;
COMMIT ;


SELECT * FROM carts;













