
--function set shipping total for user in city.
create or replace function set_shipping_total(city_x varchar)
returns integer
language plpgsql
as $$
DECLARE result_shipping integer;
    begin
    select sum(shipping_total)
    -- get value
    from get_statement_from_city(city_x )
        into result_shipping;
    if result_shipping !=0 then
        call shipping_zero(city_x);
    end if;
    return result_shipping;
end;
$$;

select from set_shipping_total('city 1');

drop function set_shipping_total(city_x varchar);

--procedure update shipping total in city and set value 0.
create or replace procedure shipping_zero(city_x varchar)
language plpgsql
as $$
begin
    UPDATE orders
    set shipping_total = 0
    where orders.carts_cart_id=(select cart_id from get_statement_from_city(city_x));
end;
$$;


drop procedure shipping_zero(city_x varchar);

--function get statement from city. Join shipping_total and cart_id in output.
create or replace function get_statement_from_city(city_x varchar)
returns table(shipping_total decimal, cart_id integer)
language plpgsql
as $$
    begin
        return query
        select orders.shipping_total, c.cart_id
        from orders join carts c on c.cart_id = orders.carts_cart_id
        join users u on c.users_user_id = u.user_id and city = city_x;

    end;
$$;

select * from get_statement_from_city('city 12');

drop function get_statement_from_city(city_x varchar);



--procedure bulk_purchase_products.
create or replace procedure bulk_purchase_products(number_product int, amount int)
language plpgsql
as $$
DECLARE remainder int;
    begin
    --update in_stock
    update products
    set in_stock = products.in_stock - amount
    where number_product = products.product_id
    returning remainder
    --save in remainder
    into remainder;
    if remainder = 0 then
        raise notice 'You have bought all products';
        commit ;
    elseif remainder > 0 then
        raise notice 'In stock product left in quantity %', remainder;
        commit ;
    else
        raise notice 'You can not buy this amount of product.';
        rollback ;
    end if;
end ;
$$;


call bulk_purchase_products(9, 15);

select * from products;

drop procedure bulk_purchase_products(number_product int, amount int);

--procedure insert new category to categories table.
create or replace procedure insert_new_category(new_cat_id int, new_cat_tit varchar, new_cat_desc text)
language plpgsql
as $$
begin
    insert into categories(category_id, category_title, category_description)
    values (new_cat_id, new_cat_tit, new_cat_desc);

end;
$$;

call insert_new_category(22, 'category 22', 'some text about products1');


select * from categories;

drop procedure insert_new_category(new_cat_id int, new_cat_tit varchar, new_cat_desc text);

--create procedure make markdown for later product.
create or replace procedure make_markdown_for_later_product()
language plpgsql
as $$
    declare p record;
begin
    --iteration by price and product_id
    for p in select price, product_id
                    from products
                    where in_stock between 1 and 5 loop
        --update price, make a discount
        update products
        set price = p.price * 0.75
        where product_id = p.product_id;
        end loop;
end;

$$;

call make_markdown_for_later_product();

select * from products
order by in_stock
    limit 100;

rollback ;


drop procedure make_markdown_for_later_product();