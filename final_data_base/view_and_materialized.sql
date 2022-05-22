--create view about about new cars and low mileage.
CREATE VIEW info_about_new_car AS
    SELECT mc.car_id, make_car, model_car, m.year, min(mileage)
FROM renting
LEFT JOIN branch b on renting.branch_id = b.branch_id
LEFT JOIN model_car mc on renting.car_id = mc.car_id
LEFT JOIN manufacturer m on mc.make_car = m.make_id
LEFT OUTER JOIN manufacturer m2 on mc.make_car = m2.make_id
WHERE m.year in (2021, 2022) and mileage between 10000 and 50000
GROUP BY mc.car_id, make_car, m.year
ORDER BY min(mileage);

DROP VIEW IF EXISTS info_about_new_car;


--create view about branch in which there was the highest price for
-- a period of more than 20 days.
CREATE VIEW reach_branch AS
    SELECT branch_id, city_id, p.car_id, sum(price)
FROM branch
LEFT JOIN car c on branch.car_id = c.car_id
LEFT OUTER JOIN payment p on c.car_id = p.car_id
LEFT OUTER JOIN car c2 on branch.car_id = c2.car_id
WHERE period > 20
GROUP BY branch_id, city_id, p.car_id
ORDER BY sum(price) desc ;

DROP VIEW IF EXISTS reach_branch;


--create materialized view
CREATE MATERIALIZED VIEW long_rent_car AS
    SELECT id, first_name, last_name, period, b.car_id
FROM customer
LEFT JOIN payment p on customer.id = p.customer_id
LEFT JOIN model_car mc on p.price = mc.price
LEFT OUTER JOIN car c on mc.car_id = c.car_id
LEFT JOIN branch b on c.car_id = b.car_id
WHERE p.price > 800 and period BETWEEN 25 and 30
GROUP BY id, first_name, last_name, p.period, b.car_id
ORDER BY p.period DESC
LIMIT 100;

DROP MATERIALIZED VIEW long_rent_car;
