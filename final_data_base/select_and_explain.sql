
--select customer which doing most expensive payment.
EXPLAIN SELECT Customer.first_name, Customer.last_name, P.price
FROM Customer
LEFT JOIN Payment P on Customer.id = P.customer_id
LEFT JOIN Car C on P.car_id = C.car_id
LEFT JOIN renting r on C.car_id = r.car_id
GROUP BY first_name, last_name, P.price
ORDER BY P.price DESC ;

SET enable_seqscan TO On;
--explain without index.
-- Group  (cost=2021.56..2141.56 rows=12000 width=35)
-- "  Group Key: p.price, customer.first_name, customer.last_name"
--   ->  Sort  (cost=2021.56..2051.56 rows=12000 width=35)
-- "        Sort Key: p.price DESC, customer.first_name, customer.last_name"
--         ->  Hash Right Join  (cost=744.00..1208.51 rows=12000 width=35)
--               Hash Cond: (p.customer_id = customer.id)
--               ->  Hash Right Join  (cost=335.00..768.00 rows=12000 width=8)
--                     Hash Cond: (c.car_id = p.car_id)
--                     ->  Seq Scan on car c  (cost=0.00..268.00 rows=12000 width=4)
--                     ->  Hash  (cost=185.00..185.00 rows=12000 width=12)
--                           ->  Seq Scan on payment p  (cost=0.00..185.00 rows=12000 width=12)
--               ->  Hash  (cost=259.00..259.00 rows=12000 width=35)
--                     ->  Seq Scan on customer  (cost=0.00..259.00 rows=12000 width=35)

CREATE UNIQUE INDEX On Customer(first_name);

SET enable_seqscan TO off;
-- Group  (cost=20000002224.84..20000002344.84 rows=12000 width=35)
-- "  Group Key: p.price, customer.first_name, customer.last_name"
--   ->  Sort  (cost=20000002224.84..20000002254.84 rows=12000 width=35)
-- "        Sort Key: p.price DESC, customer.first_name, customer.last_name"
--         ->  Hash Right Join  (cost=20000000947.28..20000001411.80 rows=12000 width=35)
--               Hash Cond: (p.customer_id = customer.id)
--               ->  Hash Right Join  (cost=20000000335.00..20000000768.00 rows=12000 width=8)
--                     Hash Cond: (c.car_id = p.car_id)
--                     ->  Seq Scan on car c  (cost=10000000000.00..10000000268.00 rows=12000 width=4)
--                     ->  Hash  (cost=10000000185.00..10000000185.00 rows=12000 width=12)
--                           ->  Seq Scan on payment p  (cost=10000000000.00..10000000185.00 rows=12000 width=12)
--               ->  Hash  (cost=462.29..462.29 rows=12000 width=35)
--                     ->  Index Scan using customer_pkey on customer  (cost=0.29..462.29 rows=12000 width=35)
-- JIT:
--   Functions: 21
-- "  Options: Inlining true, Optimization true, Expressions true, Deforming true"



DROP INDEX customer_first_name_idx;

-- the most popular car that was rented for a long period
EXPLAIN SELECT c.car_id, number_car, p.price, sum(period)
FROM renting
LEFT JOIN car c on renting.car_id = c.car_id
LEFT JOIN payment p on c.car_id = p.car_id
LEFT JOIN model_car mc on p.price = mc.price
GROUP BY c.car_id, p.price, number_car
ORDER BY sum(period) DESC ;


SET enable_seqscan TO On;
--explain without index.
-- Sort  (cost=43044.19..43441.52 rows=158931 width=49)
--   Sort Key: (sum(p.period)) DESC
--   ->  HashAggregate  (cost=19495.59..23878.61 rows=158931 width=49)
-- "        Group Key: c.car_id, p.price, c.number_car"
--         Planned Partitions: 8
--         ->  Hash Left Join  (cost=1064.00..3552.82 rows=158931 width=45)
--               Hash Cond: (p.price = mc.price)
--               ->  Hash Left Join  (cost=694.00..1158.51 rows=12000 width=45)
--                     Hash Cond: (c.car_id = p.car_id)
--                     ->  Hash Right Join  (cost=359.00..658.51 rows=12000 width=37)
--                           Hash Cond: (c.car_id = renting.car_id)
--                           ->  Seq Scan on car c  (cost=0.00..268.00 rows=12000 width=37)
--                           ->  Hash  (cost=209.00..209.00 rows=12000 width=4)
--                                 ->  Seq Scan on renting  (cost=0.00..209.00 rows=12000 width=4)
--                     ->  Hash  (cost=185.00..185.00 rows=12000 width=12)
--                           ->  Seq Scan on payment p  (cost=0.00..185.00 rows=12000 width=12)
--               ->  Hash  (cost=220.00..220.00 rows=12000 width=4)
--                     ->  Seq Scan on model_car mc  (cost=0.00..220.00 rows=12000 width=4)

CREATE UNIQUE INDEX ON car(number_car);

DROP INDEX customer_first_name_idx;

SET enable_seqscan TO off;
-- Sort  (cost=30000053332.66..30000053729.99 rows=158931 width=49)
--   Sort Key: (sum(p.period)) DESC
--   ->  GroupAggregate  (cost=30000020582.40..30000034167.08 rows=158931 width=49)
-- "        Group Key: c.car_id, p.price, c.number_car"
--         ->  Incremental Sort  (cost=30000020582.40..30000030988.46 rows=158931 width=45)
-- "              Sort Key: c.car_id, p.price, c.number_car"
--               Presorted Key: c.car_id
--               ->  Merge Left Join  (cost=30000020581.73..30000023423.03 rows=158931 width=45)
--                     Merge Cond: (c.car_id = p.car_id)
--                     ->  Sort  (cost=10000001582.84..10000001612.84 rows=12000 width=37)
--                           Sort Key: c.car_id
--                           ->  Hash Right Join  (cost=10000000470.28..10000000769.80 rows=12000 width=37)
--                                 Hash Cond: (c.car_id = renting.car_id)
--                                 ->  Seq Scan on car c  (cost=10000000000.00..10000000268.00 rows=12000 width=37)
--                                 ->  Hash  (cost=320.29..320.29 rows=12000 width=4)
--                                       ->  Index Only Scan using renting_pkey on renting  (cost=0.29..320.29 rows=12000 width=4)
--                     ->  Materialize  (cost=20000018998.89..20000019793.55 rows=158931 width=12)
--                           ->  Sort  (cost=20000018998.89..20000019396.22 rows=158931 width=12)
--                                 Sort Key: p.car_id
--                                 ->  Hash Right Join  (cost=20000000335.00..20000002549.31 rows=158931 width=12)
--                                       Hash Cond: (mc.price = p.price)
--                                       ->  Seq Scan on model_car mc  (cost=10000000000.00..10000000220.00 rows=12000 width=4)
--                                       ->  Hash  (cost=10000000185.00..10000000185.00 rows=12000 width=12)
--                                             ->  Seq Scan on payment p  (cost=10000000000.00..10000000185.00 rows=12000 width=12)
-- JIT:
--   Functions: 30
-- "  Options: Inlining true, Optimization true, Expressions true, Deforming true"


DROP INDEX car_number_car_idx;

--select which car has the most mileage
EXPLAIN SELECT p.car_id, model_car, mileage
FROM customer
LEFT JOIN payment p on customer.id = p.customer_id
LEFT JOIN model_car mc on p.car_id = mc.car_id
LEFT JOIN manufacturer m on mc.make_car = m.make_id
ORDER BY mileage DESC ;


SET enable_seqscan TO On;
-- Sort  (cost=2329.07..2359.07 rows=12000 width=23)
--   Sort Key: mc.mileage DESC
--   ->  Hash Right Join  (cost=1114.00..1516.02 rows=12000 width=23)
--         Hash Cond: (p.customer_id = customer.id)
--         ->  Hash Right Join  (cost=705.00..1075.51 rows=12000 width=27)
--               Hash Cond: (mc.car_id = p.car_id)
--               ->  Hash Right Join  (cost=370.00..575.51 rows=12000 width=23)
--                     Hash Cond: (m.make_id = mc.make_car)
--                     ->  Seq Scan on manufacturer m  (cost=0.00..174.00 rows=12000 width=4)
--                     ->  Hash  (cost=220.00..220.00 rows=12000 width=27)
--                           ->  Seq Scan on model_car mc  (cost=0.00..220.00 rows=12000 width=27)
--               ->  Hash  (cost=185.00..185.00 rows=12000 width=8)
--                     ->  Seq Scan on payment p  (cost=0.00..185.00 rows=12000 width=8)
--         ->  Hash  (cost=259.00..259.00 rows=12000 width=4)
--               ->  Seq Scan on customer  (cost=0.00..259.00 rows=12000 width=4)


SET enable_seqscan TO off;
-- Sort  (cost=20000002593.64..20000002623.64 rows=12000 width=23)
--   Sort Key: mc.mileage DESC
--   ->  Hash Right Join  (cost=20000001378.57..20000001780.59 rows=12000 width=23)
--         Hash Cond: (p.customer_id = customer.id)
--         ->  Hash Right Join  (cost=20000000908.28..20000001278.80 rows=12000 width=27)
--               Hash Cond: (mc.car_id = p.car_id)
--               ->  Hash Right Join  (cost=10000000573.28..10000000778.80 rows=12000 width=23)
--                     Hash Cond: (m.make_id = mc.make_car)
--                     ->  Seq Scan on manufacturer m  (cost=10000000000.00..10000000174.00 rows=12000 width=4)
--                     ->  Hash  (cost=423.29..423.29 rows=12000 width=27)
--                           ->  Index Scan using model_car_pkey on model_car mc  (cost=0.29..423.29 rows=12000 width=27)
--               ->  Hash  (cost=10000000185.00..10000000185.00 rows=12000 width=8)
--                     ->  Seq Scan on payment p  (cost=10000000000.00..10000000185.00 rows=12000 width=8)
--         ->  Hash  (cost=320.29..320.29 rows=12000 width=4)
--               ->  Index Only Scan using customer_pkey on customer  (cost=0.29..320.29 rows=12000 width=4)
-- JIT:
--   Functions: 23
-- "  Options: Inlining true, Optimization true, Expressions true, Deforming true"
