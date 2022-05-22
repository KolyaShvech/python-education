--create triggers for update address customer.
create or replace function update_address()
returns trigger
language plpgsql
as $$
begin
    if NEW.city <> OLD.city and NEW.street <> OLD.street then
        insert into customer
            values (OLD.first_name, OLD.last_name, NEW.city, NEW.street, OLD.phone) ;
        end if;
    return NEW;
end;
$$;

--create trigger new_address
create trigger new_address
    before UPDATE
    on customer
    for each row
    execute procedure update_address();


UPDATE customer
set city = 'New life' and street = 'New home'
where id = 2;


select * from customer;


drop function update_address();

drop trigger if exists new_address on customer;


--create trigger insert after car
create or replace function after_car_insert()
returns trigger
language plpgsql
as $$
begin
    insert into car
    values (NEW.car_id, NEW.make_car, NEW.model_car, NEW.number_car);
    return NEW;
end;
$$;

create trigger insert_car_after
    after insert
    on car
    for each row
    execute procedure after_car_insert();

INSERT INTO car
values (12001, 'nissan', 'skyline', 'erggsgyree');

