CREATE DATABASE Product;


CREATE TABLE Users (
    user_id INT UNIQUE ,
    email VARCHAR(255) UNIQUE NOT NULL,
    password VARCHAR(255) UNIQUE NOT NULL,
    first_name VARCHAR (255) NOT NULL,
    last_name VARCHAR (255) NOT NULL,
    middle_name VARCHAR (255) NOT NULL,
    is_staff int,
    country VARCHAR (255) NOT NULL,
    city VARCHAR (255) NOT NULL,
    address text

);
DROP TABLE Users;

CREATE TABLE Products (
    product_id INT UNIQUE ,
    product_title VARCHAR(255) NOT NULL,
    product_description text,
    in_stock INT NOT NULL,
    price FLOAT NOT NULL,
    slug VARCHAR (45) NOT NULL,
    category_id INT references Categories(category_id)

);

CREATE TABLE Carts (
    cart_id INT UNIQUE,
    Users_user_id INT references Users(user_id),
    subtotal DECIMAL NOT NULL,
    total DECIMAL NOT NULL,
    timestamp TIMESTAMP(2)

);

CREATE TABLE Orders (
    order_id INT UNIQUE ,
    Carts_cart_id INT references Carts(cart_id),
    Order_status_order_status_id INT references Order_status(status_id),
    shipping_total DECIMAL NOT NULL,
    total DECIMAL NOT NULL,
    created_timestamp TIMESTAMP(2),
    update_timestamp TIMESTAMP(2)
);

CREATE TABLE Order_status(
    status_id INT UNIQUE ,
    status_name VARCHAR(255)
);

CREATE TABLE Cart_product(
    carts_cart_id INT references Carts(cart_id),
    product_product_id INT references Products(product_id)
);

CREATE TABLE Categories(
    category_id INT UNIQUE ,
    category_title VARCHAR(255),
    category_description TEXT
);

DROP TABLE Categories;

COPY carts FROM '/usr/src/carts.csv' with (format csv);

COPY product.public.users FROM '/usr/src/users.csv' with (format csv);

COPY order_status FROM '/usr/src/order_status.csv' with (format csv);

COPY orders FROM '/usr/src/orders.csv' with (format csv);

COPY categories FROM '/usr/src/categories.csv' with (format csv);

COPY products FROM '/usr/src/product.csv' with (format csv);

COPY cart_product FROM '/usr/src/cart_products.csv' with (format csv);


ALTER TABLE Users
ADD column phone_numbers INT;

ALTER TABLE Users
ALTER COLUMN phone_numbers TYPE VARCHAR(255);

UPDATE Products
SET price=price*2;


