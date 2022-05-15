--optimization total for orders table and carts total tables.
EXPLAIN SELECT order_id, carts.total
FROM orders
inner join carts
ON orders.total=carts.total
ORDER BY carts.total;


EXPLAIN (ANALYSE ) SELECT order_id, carts_cart_id, orders.total
FROM orders
inner join carts
ON orders.total=carts.total
ORDER BY orders.total;


SET enable_seqscan TO On;
SET enable_seqscan TO off;


CREATE INDEX ON orders(total);
CREATE INDEX ON carts(total);

--join tables users, potential_customers, carts and cart_product. Create index
-- for city in user and potential_customers
EXPLAIN SELECT user_id, cart_id, carts_cart_id, users.city
FROM product.public.users
left join potential_customers pc on users.city = pc.city
left join carts c on users.user_id = c.users_user_id
left join cart_product cp on c.cart_id = cp.carts_cart_id
ORDER BY users.city;


EXPLAIN (ANALYSE ) SELECT user_id, cart_id, carts_cart_id, users.city
FROM product.public.users
left join potential_customers pc on users.city = pc.city
left join carts c on users.user_id = c.users_user_id
left join cart_product cp on c.cart_id = cp.carts_cart_id
ORDER BY users.city;

CREATE INDEX ON product.public.users(city);
CREATE INDEX ON potential_customers(city);

DROP INDEX users_city_idx;
DROP INDEX potential_customers_city_idx;

--join cart_product, orders and product. 
EXPLAIN (ANALYSE )SELECT  sum(o.carts_cart_id), product_product_id, price
FROM cart_product
left outer join orders o on cart_product.carts_cart_id = o.carts_cart_id
left outer join products p on p.product_id = cart_product.product_product_id
GROUP BY price, product_product_id
ORDER BY sum(o.carts_cart_id), product_product_id;


EXPLAIN SELECT  sum(o.carts_cart_id), product_product_id, price
FROM cart_product
left outer join orders o on cart_product.carts_cart_id = o.carts_cart_id
left outer join products p on p.product_id = cart_product.product_product_id
GROUP BY price, product_product_id
ORDER BY sum(o.carts_cart_id), product_product_id;




SET enable_seqscan TO On;
-- Sort  (cost=1495.87..1523.36 rows=10995 width=20)
-- "  Sort Key: (sum(o.carts_cart_id)), cart_product.product_product_id"
--   ->  HashAggregate  (cost=647.90..757.85 rows=10995 width=20)
-- "        Group Key: p.price, cart_product.product_product_id"
--         ->  Hash Left Join  (cost=253.80..565.44 rows=10995 width=16)
--               Hash Cond: (cart_product.product_product_id = p.product_id)
--               ->  Hash Left Join  (cost=58.80..341.55 rows=10995 width=8)
--                     Hash Cond: (cart_product.carts_cart_id = o.carts_cart_id)
--                     ->  Seq Scan on cart_product  (cost=0.00..158.95 rows=10995 width=8)
--                     ->  Hash  (cost=40.02..40.02 rows=1502 width=4)
--                           ->  Seq Scan on orders o  (cost=0.00..40.02 rows=1502 width=4)
--               ->  Hash  (cost=145.00..145.00 rows=4000 width=12)
--                     ->  Seq Scan on products p  (cost=0.00..145.00 rows=4000 width=12)
SET enable_seqscan TO off;

-- Sort  (cost=20000002384.65..20000002412.14 rows=10995 width=20)
-- "  Sort Key: (sum(o.carts_cart_id)), cart_product.product_product_id"
--   ->  GroupAggregate  (cost=20000001426.74..20000001646.64 rows=10995 width=20)
-- "        Group Key: p.price, cart_product.product_product_id"
--         ->  Sort  (cost=20000001426.74..20000001454.22 rows=10995 width=16)
-- "              Sort Key: p.price, cart_product.product_product_id"
--               ->  Hash Left Join  (cost=20000000377.08..20000000688.72 rows=10995 width=16)
--                     Hash Cond: (cart_product.product_product_id = p.product_id)
--                     ->  Hash Left Join  (cost=20000000058.80..20000000341.55 rows=10995 width=8)
--                           Hash Cond: (cart_product.carts_cart_id = o.carts_cart_id)
--                           ->  Seq Scan on cart_product  (cost=10000000000.00..10000000158.95 rows=10995 width=8)
--                           ->  Hash  (cost=10000000040.02..10000000040.02 rows=1502 width=4)
--                                 ->  Seq Scan on orders o  (cost=10000000000.00..10000000040.02 rows=1502 width=4)
--                     ->  Hash  (cost=268.28..268.28 rows=4000 width=12)
--                           ->  Index Scan using products_product_id_key on products p  (cost=0.28..268.28 rows=4000 width=12)
-- JIT:
--   Functions: 24
-- "  Options: Inlining true, Optimization true, Expressions true, Deforming true"














