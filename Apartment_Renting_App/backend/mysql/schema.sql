DROP DATABASE IF EXISTS CSC648;
CREATE DATABASE CSC648;
USE CSC648;

CREATE TABLE USER
(
  user_id     INT PRIMARY KEY AUTO_INCREMENT,
  username    VARCHAR(20) UNIQUE NOT NULL,
  password    VARCHAR(100) NOT NULL,
  email       VARCHAR(50),
  phone       CHAR(15),
  role        INTEGER NOT NULL DEFAULT 1,
  isStudent   BOOLEAN,
  isBanned    BOOLEAN
);

CREATE TABLE  LISTINGS
(
  house_id    INT PRIMARY KEY AUTO_INCREMENT,
  renter_id   INT NOT NULL REFERENCES USER(user_id),
  house_name  VARCHAR(100),
  price       INT,
  size        INT,
  distance    FLOAT,
  number      INT,
  street      VARCHAR(100),
  city        VARCHAR(30),
  state       CHAR(2),
  zipcode     CHAR(5),
  image_url   VARCHAR(500),
  isAvailable BOOLEAN,
  customer_id INT DEFAULT NULL,
  create_date DATE
);

CREATE TABLE MESSAGE
(
  renter_id   INT NOT NULL REFERENCES USER(user_id),
  customer_id INT NOT NULL REFERENCES USER(user_id),
  message     VARCHAR(500),
  date        DATE
);


INSERT INTO USER (username, password, email, phone, role, isStudent, isBanned) VALUES
('kim', '123', 'kim@gmail.com', '123456789', 2, TRUE, FALSE),
('alex', '123', 'alex@gmail.com', '123456789', 1, TRUE, FALSE),
('sindy', '123', 'sindy@gmail.com', '123456789', 1, TRUE, FALSE);


INSERT INTO LISTINGS (renter_id, house_name, price, size, distance, number, street, city, state, zipcode, image_url, isAvailable, create_date) VALUES
(2, 'Foster', 1200, 500, 15.4, 861, 'Sanbarra st', 'Foster City', 'CA', 94404, 'https://photos.zillowstatic.com/cc_ft_1536/ISmmvxzrdz55h91000000000.webp', TRUE, NOW()),
(3, 'South SF', 1000, 300, 2.4, 181, 'Fremont st', 'San Francisco', 'CA', 94105, 'https://djs00nylhf7co.cloudfront.net/assets/img--gallery-interior-52_lg-277eb7b2a425cc901979eb40c134e9b4e3ffe13041dad29d15ec41a4ac35e1b9.jpg', TRUE, NOW());





