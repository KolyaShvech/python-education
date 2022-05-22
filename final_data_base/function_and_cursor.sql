--create function which return table which output table with a cheap car rental price.
create or replace function get_min_price_car ()
returns table (make_car_id integer, model_car_name varchar, cost integer, year_of_issue integer)
language plpgsql
as $$
    begin
        return query
        select make_car, model_car, price, year
        FROM model_car
        WHERE price < 200
        ORDER BY price;
    end;
$$;

drop function get_min_price_car();

select * from get_min_price_car();


--create function which displays a table of customers who rented a car at a specified time.
create or replace function get_date_about_renting_period(first_date integer, second_date integer)
returns table (client integer, car_rent_id integer, rent_price integer)
language plpgsql
as $$
declare date_per record;
      begin
    --iteration in the required columns
    for date_per in (SELECT customer_id, car_id, price
                     FROM payment
                     WHERE period in (first_date, second_date)
                     ORDER BY price) loop
        --write data to variables
        client := date_per.customer_id;
        car_rent_id := date_per.car_id;
        rent_price := date_per.price;
        return next ;
        end loop;
end;
$$;

select * from get_date_about_renting_period(7, 14);

drop function if exists get_date_about_renting_period(first_date integer, second_date integer);


--create function using cursor. This function output result in table by year of request needing cars.
create or replace function get_car_year(search_year integer)
returns table (make_car_id integer, mileage_in_car integer)
language plpgsql
as $$
declare
    rec_car record;
    cur_car cursor(search_year integer) for
        select make_car, year, mileage
        from model_car
        where year = search_year;
begin
    -- open the cursor
    open cur_car(search_year);
    loop
        --fetch row into car record
        fetch cur_car into rec_car;
        exit when not found;
        --output result in table
        make_car_id:= rec_car.make_car;
        mileage_in_car:= rec_car.mileage;
        return next ;
    end loop;
    close cur_car;
    return next;

end;
$$;

select * from get_car_year(2022);

drop function get_car_year(search_year integer);

