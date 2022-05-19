select category_title,
       product_title,
       price,
       avg(price) over (partition by category_title order by price desc )
from categories
left join  products p on categories.category_id = p.category_id;



--trigger for product table. Insert and update table.
create or replace function update_price_product()
returns TRIGGER
language plpgsql
as $$
    begin
        if OLD.price != NEW.price then
            raise notice 'New price.';
        end if;
        return NEW;
    end;
$$;

CREATE TRIGGER holidays_price
    BEFORE UPDATE
    ON products
    FOR EACH ROW
    EXECUTE PROCEDURE update_price_product();

UPDATE products
SET price = 120.7
WHERE product_id = 1;


select * from products;


DROP FUNCTION if exists update_price_product();

DROP TRIGGER IF EXISTS holidays_price ON products;


--trigger to check the correctness of the data.
create or replace function validate_info_input()
returns TRIGGER
language plpgsql
AS $$
BEGIN
    if NEW.email IS NULL and length(NEW.email) > 10 then
        raise exception 'You must filled up this cell.';
    end if;
    if NEW.password IS NULL and length(NEW.password) > 8 then
        raise exception 'You must filled up this cell.';
    end if;
    if NEW.first_name IS NULL and length(NEW.first_name) > 2 then
        raise exception 'You must filled up this cell.';
    end if;
    if NEW.last_name IS NULL and length(NEW.last_name) > 3 then
        raise exception 'You must filled up this cell.';
    end if;
    if NEW.middle_name IS NULL and length(NEW.middle_name) > 4 then
        raise exception 'You must filled up this cell.';
    end if;
    if NEW.country IS NULL and length(NEW.country) > 4 then
        raise exception 'You must filled up this cell.';
    end if;
    if NEW.city IS NULL and length(NEW.city) > 2 then
        raise exception 'You must filled up this cell.';
    end if;
    if NEW.address IS NULL and length(NEW.address) > 10 then
        raise exception 'You must filled up this cell.';
    end if;
    return NEW;
end;
$$;

CREATE TRIGGER validate_date_new_user
    BEFORE INSERT
    ON product.public.users
    FOR EACH ROW
    EXECUTE PROCEDURE validate_info_input();


INSERT INTO product.public.users(user_id, email, password, first_name, last_name, middle_name, is_staff, country, city, address, phone_numbers)
values ( 3002, '', '', '', 'oyuuy', 'qw', 0, '', '', '', '');

INSERT INTO users(user_id, email, password, first_name, last_name, middle_name, is_staff, country, city, address, phone_numbers)
VALUES (3003, 'wewrttt', 'cvxcvxv', 'oipgf', 'zxcv', 'lkjhg', 1, 'vjouu', 'sdadasd 12', 'jhgddfgdgra34');

select * from product.public.users;

drop function if exists validate_info_input();

drop trigger if exists validate_date_new_user on product.public.users;

