
SELECT user_id, first_name, last_name, middle_name
FROM product.public.users;

SELECT product_id, product_description, product_title
FROM products;

SELECT * FROM order_status;

SELECT * FROM orders
WHERE order_status_order_status_id in (3, 4);


SELECT product_id, price
FROM products
WHERE price>80 and price<=150;

SELECT * FROM orders
WHERE created_timestamp>'2020/10/01';

SELECT * FROM orders
WHERE created_timestamp BETWEEN '2020/01/01' and '2020/06/01';

SELECT * FROM products
WHERE category_id in (7, 11, 18);

SELECT * FROM orders
WHERE order_status_order_status_id=2 and created_timestamp='2020/12/31';

SELECT * FROM orders
WHERE order_status_order_status_id=5;

SELECT avg(total) AS avg_count_all_orders FROM orders
WHERE order_status_order_status_id=1;

SELECT max(total) AS max_count_in_3th_period_2020
FROM orders
WHERE created_timestamp BETWEEN '2020/06/01' and '2020/09/30';

















