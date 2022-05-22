--create procedure action with customers
create or replace procedure action_with_customers(
                                                act_first varchar (255),
                                                act_last varchar (255),
                                                act_city varchar (255),
                                                act_street varchar (255),
                                                act_phone integer)
language plpgsql
as $$
begin
    insert into customer (first_name, last_name, city, street, phone)
    values (act_first, act_last, act_city, act_street, act_phone);
    if not FOUND then
        rollback ;
    else
        raise notice 'Insert into table new column.';
        commit ;
    end if;
end;
$$;

call action_with_customers('Sorry', 'Mercy', 'LA', 'baker', 34412444);

drop procedure action_with_customers(act_first varchar(255), act_last varchar(255), act_city varchar(255), act_street varchar(255), act_phone integer);

select * from customer;



create or replace procedure del_customer(del_cust_id integer)
language plpgsql
as $$
BEGIN
    DELETE FROM customer
    WHERE del_cust_id = customer.id;
    if not FOUND then
        raise notice 'Customer this ID have not in table.';
        rollback ;
    else
        raise notice 'Deleted customer this ID %', del_cust_id;
        commit ;
    end if;

end;
$$;

call del_customer(12001);

drop procedure del_customer(del_cust_id integer);


--create procedure expected rent car at more period.
create or replace procedure expected_car_rent(num_car_id integer, new_period integer)
language plpgsql
as $$
declare result integer;
    begin
    --update days
    update renting
    set days = renting.days + new_period
    where num_car_id = car_id
    returning days
    --save into result
    into result;
    if result < 30 then
        raise notice 'You expected car on % days', result;
        commit ;
    else
        raise notice 'You can not rent car so for many days %', result;
        rollback ;
    end if;
end ;
$$;

call expected_car_rent(4, 10);

drop procedure expected_car_rent(num_car_id integer, new_period integer);


select *
from renting;