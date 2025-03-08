CREATE DATABASE amusement_park;
USE DATABASE amusement_park;

CREATE TABLE visitors (
    visitor_id INT AUTOINCREMENT PRIMARY KEY,
    name STRING,
    age INT
);

CREATE TABLE financial_transactions (
    transaction_id INT AUTOINCREMENT PRIMARY KEY,
    visitor_id INT,
    transaction_type STRING,
    amount FLOAT,
    transaction_date DATE,
    FOREIGN KEY (visitor_id) REFERENCES visitors(visitor_id) ON DELETE CASCADE
);

CREATE TABLE attractions (
    attraction_id INT AUTOINCREMENT PRIMARY KEY,
    name STRING,
    status STRING,
    capacity INT
);

CREATE TABLE visits (
    visit_id INT AUTOINCREMENT PRIMARY KEY,
    visitor_id INT,
    attraction_id INT,
    visit_date DATE,
    FOREIGN KEY (visitor_id) REFERENCES visitors(visitor_id) ON DELETE CASCADE,
    FOREIGN KEY (attraction_id) REFERENCES attractions(attraction_id) ON DELETE CASCADE
);

CREATE TABLE employees (
    employee_id INT AUTOINCREMENT PRIMARY KEY,
    name STRING,
    role STRING,
    salary FLOAT,
    shift_start TIME,
    shift_end TIME
);

ALTER TABLE attractions ADD COLUMN employee_id INT;
ALTER TABLE attractions ADD FOREIGN KEY (employee_id) REFERENCES employees(employee_id) ON DELETE SET NULL;

CREATE TABLE food_sales (
    sale_id INT AUTOINCREMENT PRIMARY KEY,
    visitor_id INT,
    food_item STRING,
    quantity INT,
    price FLOAT,
    sale_date DATE,
    FOREIGN KEY (visitor_id) REFERENCES visitors(visitor_id) ON DELETE CASCADE
);

