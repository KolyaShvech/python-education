CREATE DATABASE Rental_cars;
--Create table Customer
CREATE TABLE Customer (
    id serial PRIMARY KEY ,
    first_name varchar (255) NOT NULL ,
    last_name varchar (255) NOT NULL ,
    city varchar (255),
    street varchar(255),
    phone integer
);

DROP TABLE Customer ;

--insert data for table Customer
do $$
    BEGIN
        for i in 1..12000 loop
            INSERT INTO Customer (first_name, last_name, city, street, phone)
            VALUES (('first_name ' || i :: varchar),
                    ('last_name ' || i :: varchar),
                    ('City ' || i :: varchar),
                    ('Street ' || i :: varchar),
                    807800000 + i);
            end loop;
    end;
$$;

--create table Address
CREATE TABLE Address (
    customer_id INT references Customer(id),
    city_name varchar (255) NOT NULL ,
    street_name varchar(255),
    phone_number int
);

DROP TABLE Address;
--insert data in table address
do $$
begin
    for i in 1..12000 loop
        INSERT INTO Address(customer_id, city_name, street_name, phone_number)
        VALUES (i, ('City_name ' || i :: varchar),
                ('Street_name ' || i :: varchar),
                80900000 + i);
        end loop;
end;
$$;

--create table City
CREATE TABLE City (
    city_id SERIAL PRIMARY KEY ,
    city_name varchar (255)
);

DROP TABLE City ;

--insert data for table City
do $$
    BEGIN
        for i in 1..12000 loop
            INSERT INTO City (city_name, city_id) VALUES ('City ' || i :: varchar, i);
            end loop;
    end;

$$;

--create table Street
CREATE TABLE Street (
    street_id SERIAL PRIMARY KEY ,
    street_name varchar(255)
);

DROP TABLE Street ;

--insert data for table Street
do $$
    BEGIN
        for i in 1..12000 loop
            INSERT INTO Street (street_name, street_id) VALUES ('Street  ' || i :: varchar, i);
            end loop;
    end;

$$;

CREATE TABLE Renting (
    car_id SERIAL PRIMARY KEY ,
    branch_id INT ,
    price int ,
    day_of_rent timestamp(6),
    days int,
    phone int
);

DROP TABLE Renting  ;

--insert data for table Renting
do $$
BEGIN
    for i in 1..12000 loop
        INSERT INTO Renting (branch_id, price, day_of_rent, days, phone)
        values (i, random()* (1000 - 100) + 100, now(), random()* (30 - 7) + 7, 809000 + i);
        end loop;
end;
$$;

--create table branch
CREATE TABLE Branch (
    branch_id SERIAL PRIMARY KEY ,
    city_id int references City(city_id),
    car_id int references Renting(car_id),
    street_id int references Street(street_id)
);

DROP TABLE Branch  ;

--insert data for Branch table
do $$
BEGIN
    for i in 1..12000 loop
        INSERT INTO Branch (city_id, car_id, street_id)
        values (i, i, i);
        end loop;
end;
$$;


--create table Payment
CREATE TABLE Payment (
    customer_id int references Customer(id),
    car_id int references Renting(car_id),
    price int,
    period int
);

DROP TABLE Payment;

--insert data to Payment table.
do $$
BEGIN
    for i in 1..12000 loop
        INSERT INTO Payment (customer_id, car_id, price, period)
        values (i, i, random()* (1000 - 100) + 100, random()* (30 - 7) + 7);
        end loop;
end;
$$;

--create table Car.
CREATE TABLE Car (
    car_id int references Renting(car_id),
    make_car varchar (255),
    model_car varchar (255),
    number_car text
);

DROP TABLE Car;

--insert data to Car table.
do $$
BEGIN
    for i in 1..12000 loop
        INSERT INTO Car (car_id, make_car, model_car, number_car)
        values (i, ('make_car '|| i :: varchar), ('model_car '|| i :: varchar), md5(random():: text));
        end loop;
end;
$$;

--create table Model_car.
CREATE TABLE Model_car (
    car_id int references Renting(car_id),
    make_car SERIAL PRIMARY KEY ,
    model_car varchar (255),
    price int,
    year int,
    mileage int
);

DROP TABLE Model_car  ;

--insert data to Model_car table.
do $$
BEGIN
    for i in 1..12000 loop
        INSERT INTO Model_car (car_id, model_car, price, year, mileage)
        values (i, ('model_car '|| i :: varchar), random()* (1000 - 100) + 100,
                random()*(2022 - 2017) + 2017, random()* (100000 - 10000) + 10000);
        end loop;
end;
$$;

--create table Manufacturer.
CREATE TABLE Manufacturer (
    make_id int references Model_car(make_car),
    year int
);

DROP TABLE Manufacturer;

--insert data to Manufacturer table.
do $$
BEGIN
    for i in 1..12000 loop
        INSERT INTO Manufacturer (make_id, year)
        values (i, random()*(2022 - 2017) + 2017);
        end loop;
end;
$$;
