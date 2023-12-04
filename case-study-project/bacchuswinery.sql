DROP DATABASE IF EXISTS bacchus;
CREATE DATABASE bacchus;

USE bacchus;

CREATE TABLE suppliers (
    id int auto_increment primary key,
    name varchar(100)
);

CREATE TABLE supply(
    id int auto_increment primary key,
    name varchar(100),
    quantity int
);

CREATE TABLE shipments(
    id int auto_increment primary key,
    purchase_number int,
    supply_id int,
    supply_quantity int,
    expected_date date,
    actual_date date,
    supplier_id int,
    CONSTRAINT FOREIGN KEY (supply_id) REFERENCES supply(id),
    CONSTRAINT FOREIGN KEY (supplier_id) REFERENCES suppliers(id)
);

CREATE TABLE employees
(
    id         int auto_increment primary key,
    l_name     varchar(100),
    f_name     varchar(100),
    position   varchar(100),
    manager_id int,
    CONSTRAINT FOREIGN KEY (manager_id) REFERENCES employees (id)
);

CREATE TABLE hours (
    id int auto_increment primary key,
    employee_id int,
    hours int,
    fiscal_week int,
    CONSTRAINT FOREIGN KEY (employee_id) REFERENCES employees(id)
);

CREATE TABLE wines(
    id int auto_increment primary key,
    name varchar(100),
    onhand int,
    price DECIMAL(19,2)
);

CREATE TABLE distributer(
    id int auto_increment primary key,
    name varchar(100)
);
CREATE TABLE receipts(
  receipt_number int primary key,
  tracking_number varchar(100),
  expected_date date,
  actual_date date
);
CREATE TABLE sales(
    id int primary key auto_increment,
    receipt_number int,
    wine_id int,
    quantity int,
    distributer_id int,
    CONSTRAINT FOREIGN KEY (wine_id) REFERENCES wines(id),
    CONSTRAINT FOREIGN KEY (distributer_id) REFERENCES distributer(id),
    CONSTRAINT FOREIGN KEY (receipt_number) REFERENCES receipts(receipt_number)
);

CREATE USER IF NOT EXISTS bacchusWinery IDENTIFIED BY 'password';
GRANT ALL PRIVILEGES ON TABLE * TO bacchusWinery;

INSERT INTO suppliers (name) values ('BottleAndCork');
INSERT INTO suppliers (name) values ('BoxAndLabels');
INSERT INTO suppliers (name) values ('VatsAndTubing');

INSERT INTO supply (name, quantity) VALUES ('Bottles', 100);
INSERT INTO supply (name, quantity) VALUES ('Cork', 100);
INSERT INTO supply (name, quantity) VALUES ('Boxes', 100);
INSERT INTO supply (name, quantity) VALUES ('Labels', 100);
INSERT INTO supply (name, quantity) VALUES ('Tubing', 100);
INSERT INTO supply (name, quantity) VALUES ('Vats', 100);

INSERT INTO shipments (purchase_number, supply_id, supply_quantity, expected_date, actual_date, supplier_id) VALUES (981758, 1,100, '2023-11-25', '2023-11-25',1);
INSERT INTO shipments (purchase_number, supply_id, supply_quantity, expected_date, actual_date, supplier_id) VALUES (981513, 2,100, '2023-11-25', '2023-11-25',1);
INSERT INTO shipments (purchase_number, supply_id, supply_quantity, expected_date, actual_date, supplier_id) VALUES (981780, 3,100, '2023-11-10', '2023-11-10',2);
INSERT INTO shipments (purchase_number, supply_id, supply_quantity, expected_date, actual_date, supplier_id) VALUES (981791, 4,100, '2023-11-25', '2023-11-25',2);
INSERT INTO shipments (purchase_number, supply_id, supply_quantity, expected_date, actual_date, supplier_id) VALUES (981850, 5,100, '2023-11-25', '2023-11-25',3);
INSERT INTO shipments (purchase_number, supply_id, supply_quantity, expected_date, actual_date, supplier_id) VALUES (981458, 6,100, '2023-11-25', '2023-11-25',3);

INSERT INTO employees (l_name, f_name, position, manager_id) VALUES ('Collins', 'Janet', 'Finance and Payroll', null);
INSERT INTO employees (l_name, f_name, position, manager_id) VALUES ('Murphy', 'Roz', 'Marketing', null);
INSERT INTO employees (l_name, f_name, position, manager_id) VALUES ('Ulrich', 'Bob', 'Marketing', 2);
INSERT INTO employees (l_name, f_name, position, manager_id) VALUES ('Doyle', 'Henry', 'Production', null);
INSERT INTO employees (l_name, f_name, position, manager_id) VALUES ('Costanza', 'Maria', 'Distribution', null);
INSERT INTO employees (l_name, f_name, position, manager_id) VALUES ('Bacchus', 'Davis', 'Owner', null);
INSERT INTO employees (l_name, f_name, position, manager_id) VALUES ('Bacchus', 'Stan', 'Owner', null);

INSERT INTO hours (employee_id, hours, fiscal_week) VALUES (1, 40 ,1);
INSERT INTO hours (employee_id, hours, fiscal_week) VALUES (2, 54 ,1);
INSERT INTO hours (employee_id, hours, fiscal_week) VALUES (3, 45 ,1);
INSERT INTO hours (employee_id, hours, fiscal_week) VALUES (4, 56 ,1);
INSERT INTO hours (employee_id, hours, fiscal_week) VALUES (5, 48 ,1);
INSERT INTO hours (employee_id, hours, fiscal_week) VALUES (6, 59 ,1);
INSERT INTO hours (employee_id, hours, fiscal_week) VALUES (7, 62 ,1);

INSERT INTO wines (name, onhand, price) VALUES ('Merlot', 16, 16.99);
INSERT INTO wines (name, onhand, price) VALUES ('Cabernet', 14, 14.99);
INSERT INTO wines (name, onhand, price) VALUES ('Chablis', 20, 17.99);
INSERT INTO wines (name, onhand, price) VALUES ('Chardonnay', 31, 19.99);

INSERT INTO distributer (name) VALUES ('Great Value Wine Sales');
INSERT INTO distributer (name) VALUES ('WineMart');
INSERT INTO distributer (name) VALUES ('Great Value Wine Sales');
INSERT INTO distributer (name) VALUES ('Wine Sale');
INSERT INTO distributer (name) VALUES ('Wine and More');
INSERT INTO distributer (name) VALUES ('Wineys');

INSERT INTO receipts (receipt_number, tracking_number, expected_date,
                      actual_date) values (156945, '123456','2023-12-5', null);

INSERT INTO receipts (receipt_number, tracking_number, expected_date,
                      actual_date) values (156992, '5389725','2023-12-5', null);
INSERT INTO receipts (receipt_number, tracking_number, expected_date,
                      actual_date) values (156989, '156327235','2023-12-5', null);
INSERT INTO receipts (receipt_number, tracking_number, expected_date,
                      actual_date) values (151582, '235489348','2023-12-5', '2023-12-2');
INSERT INTO receipts (receipt_number, tracking_number, expected_date,
                      actual_date) values (156789, '682235789','2023-12-5', null);
INSERT INTO receipts (receipt_number, tracking_number, expected_date,
                      actual_date) values (159872, '2053687','2023-12-5', '2023-12-3');

INSERT INTO sales (receipt_number, wine_id, quantity,
                   distributer_id) VALUES (156945, 1, 15, 2);
INSERT INTO sales (receipt_number, wine_id, quantity,
                   distributer_id) VALUES (156992, 1, 1, 6);
INSERT INTO sales (receipt_number, wine_id, quantity,
                   distributer_id) VALUES (156989, 4, 30, 5);
INSERT INTO sales (receipt_number, wine_id, quantity,
                   distributer_id) VALUES (151582, 3, 15, 4);
INSERT INTO sales (receipt_number, wine_id, quantity,
                   distributer_id) VALUES (156789, 2, 9, 3);
INSERT INTO sales (receipt_number, wine_id, quantity,
                   distributer_id) VALUES (159872, 1, 30, 2);
