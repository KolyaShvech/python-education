--create view to products table.
CREATE VIEW product_status AS
    SELECT product_id,
           product_title,
           price,
           in_stock
FROM products
WHERE in_stock > 20
ORDER  by in_stock DESC ;

SELECT * FROM product_status
WHERE price BETWEEN 200 AND 300
ORDER BY price DESC ;

DROP VIEW product_status;

--create view for order and orders_status tables.
CREATE VIEW orders_in_year AS
    SELECT order_id,
           status_id,
           sum(total),
           update_timestamp
FROM orders
INNER JOIN order_status os on os.status_id = orders.order_status_order_status_id
WHERE status_id IN (3,4) and update_timestamp BETWEEN '2018/01/01' and '2019/01/01'
GROUP BY os.status_id, orders.order_id, orders.update_timestamp
ORDER BY sum(total) DESC ;

SELECT * FROM orders_in_year
WHERE update_timestamp BETWEEN '2018/04/01' and '2018/05/01'
ORDER BY order_id;


DROP VIEW orders_in_year;

--create view for products and categories tables.
CREATE VIEW prod_cater AS
    SELECT product_id,
           product_title,
           category_title,
           price
FROM products
    INNER JOIN categories c on c.category_id = products.category_id
WHERE price BETWEEN 100 and 150
GROUP BY product_id, product_title, category_title, price
ORDER BY price;


SELECT * FROM prod_cater
    WHERE category_title='Category 7';


DROP VIEW prod_cater;


--create materialized view for select most populars products.
CREATE MATERIALIZED VIEW most_popular_product AS
    SELECT product_id AS number_product,
           sum(price) AS top
FROM products
JOIN categories c on c.category_id = products.category_id
JOIN cart_product cp on products.product_id = cp.product_product_id
JOIN carts c2 on cp.carts_cart_id = c2.cart_id
JOIN orders o on cp.carts_cart_id = o.carts_cart_id
GROUP BY number_product
ORDER BY top DESC
WiTH NO DATA;

SELECT * FROM most_popular_product
WHERE number_product=348;


REFRESH MATERIALIZED VIEW most_popular_product;

REFRESH MATERIALIZED VIEW CONCURRENTLY most_popular_product;

DROP MATERIALIZED VIEW most_popular_product;

