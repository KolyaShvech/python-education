-- Create table
CREATE TABLE Potential_customers(
    id INT UNIQUE NOT NULL,
    email VARCHAR(255) NOT NULL,
    name VARCHAR(50) NOT NULL,
    surname VARCHAR(50) NOT NULL,
    second_name VARCHAR (50) NOT NULL,
    city VARCHAR(50) NOT NULL
);
-- Filled up table
INSERT INTO potential_customers (id, email, name, surname, second_name, city)
    VALUES ('1', 'alibaba@gmail.com', 'aliba', 'ba', 'semenovich', 'city 1'),
           ('2', 'vasya.tocha@gmail.com', 'vasya', 'tocha', 'nikolaevich', 'city2'),
           ('3', 'senen.vopros@gmail.com', 'semen', 'vopros', 'prohorovich','city3'),
           ('4','tamara.sbazara@gmail.com',	'tamara', 'sbazara', 'larionovna','city4'),
           ('5','stas.unitas@gmail.com', 'stas', 'unitas',	'orestovich', 'city5'),
           ('6','roman.karman@gmail.com',	'roman','karman',' petrovich','city6'),
           ('7','anton.karton@gmail.com','anton','karton','zaharobich','city7'),
           ('8','kolya.volya@gmail.com','kolya','volya','semenovich','city8'),
           ('9','sergey.vorobey@gmail.com',	'sergey','vorobey',	'nikolaevich','city9'),
           ('10','alla.toy@gmail.com','alla','toy','dmitpievna',	'city10'),
           ('11','ira.svet@gmail.com','ira',	'svet',	'vasilevna','city11'),
           ('12','artyr.obuza@gmail.com','artur','obuza','orestovich','city12'),
           ('13','karina.dinamo@gmail.com',	'karina','dinamo',	'petrovna',	'city13'),
           ('14','katya.koala@gmail.com','katya','koala','zaharovna','city14'),
           ('15','julia.kot@gmail.com','julia','kot','leonidivna','city15'),
           ('16','dima.duma@gmail.com','dima',	'duma',	'nikolaevich','city16'),
           ('17','sasha.prostakvasha@gmail.com','sasha','prostakvasha',	'prohorovich','city17'),
           ('18','denis.redis@gmail.com','denis','redis','Ilich','city18'),
           ('19','ilia.karaul@gmail.com','ilia',	'karaul','orestovich','city19'),
           ('20','alina.telega@gmail.com','alina','telega','leonidivna','city20'),
           ('21','pasha.kasha@gmail.com','pasha','kasha','zaharovich','city21'),
           ('22', 'vova.zilvova@gmail.com', 'vova', 'zilvova', 'semenovich', 'city22'),
           ('23','vitya.salo@gmail.com',	'vitya','salo',	'nikolaevich',	'city23'),
           ('24','marina.derevo@gmail.com',	'marina','derevo','prohorovna','city24'),
           ('25','sveta.sever@gmail.com','sveta','sever','lukichna',	'city25'),
           ('26','tolya.kabak@gmail.com','tolya','kabak','orestovich','city26'),
           ('27','joni.cage@gmail.com',	'joni',	'cage',	'petrovich','city27'),
           ('28','tom.holland@gmail.com','tom',	'holland','zaharobich','city28'),
           ('29','makar.vinchester@gmail.com','makar','vinchester','romanovich','city29'),
           ('30','lesha.popovich@gmail.com',	'lesha','popovich',	'grigorevich',	'city30');


--output email and name from potential_user and user from city 17
SELECT first_name, email
FROM product.public.users
WHERE city='city 17'
UNION
SELECT name, email
FROM Potential_customers
WHERE city='city17';

--output email and name order by city and name
SELECT first_name,  email
FROM product.public.users
ORDER BY city, first_name;

--output product groups, total quantity by product group in descending order of quantity
SELECT product_title, sum(in_stock)
FROM products
GROUP BY product_title
ORDER BY sum(in_stock) DESC ;

--products that never made it to the cart
SELECT product_title
FROM products
LEFT JOIN cart_product cp on products.product_id = cp.product_product_id
WHERE cp.product_product_id is null;

--all products that did not get into any order
SELECT product_title
FROM orders, cart_product
RIGHT JOIN products
    on cart_product.product_product_id = product_id
WHERE orders.carts_cart_id = cart_product.carts_cart_id
GROUP BY product_title
ORDER BY product_title;

--top 10 products that were added to carts most often
SELECT product_title top_product, count(product_product_id) best_selling
FROM orders, cart_product
LEFT JOIN products p
    on cart_product.product_product_id = p.product_id
WHERE orders.carts_cart_id=cart_product.carts_cart_id
GROUP BY product_title
ORDER BY count(product_product_id) DESC , p.product_title
LIMIT 10;


--top 10 products that were not only added to carts, but also placed orders most often
SELECT product_title top_product, count(product_product_id) best_selling
FROM orders, cart_product
LEFT JOIN products p
    on cart_product.product_product_id = p.product_id
WHERE (orders.carts_cart_id=cart_product.carts_cart_id) AND (cart_product.product_product_id > 0)
GROUP BY product_title
ORDER BY count(product_product_id) DESC , p.product_title
LIMIT 10;



--top 5 users who spent the most money
SELECT sum(total) spend_money, users_user_id rockefeller
FROM carts
GROUP BY users_user_id
ORDER BY sum(total) DESC
LIMIT 5;


--top 5 users who made the most orders
SELECT u.user_id, count(orders.order_id) AS order_count
FROM orders
LEFT JOIN carts on orders.carts_cart_id = carts.cart_id
LEFT JOIN users u on carts.users_user_id = u.user_id
GROUP BY u.user_id
ORDER BY order_count DESC
LIMIT 5
;

--Top 5 Users Who Created Carts But Never Ordered
SELECT u.user_id, count(carts.cart_id) AS empty_cart_count
FROM orders
RIGHT JOIN carts on orders.carts_cart_id = carts.cart_id
LEFT JOIN users u on carts.users_user_id = u.user_id
WHERE orders.order_id is null
GROUP BY u.user_id
ORDER BY empty_cart_count desc
LIMIT 5;
















