INSERT INTO USER (username, password, email, phone, role, isStudent, isBanned) VALUES
('kim', '123', 'kim@gmail.com', '123456789', 2, TRUE, FALSE),
('alex', '123', 'alex@gmail.com', '123456789', 1, TRUE, FALSE),
('sindy', '123', 'sindy@gmail.com', '123456789', 1, TRUE, FALSE);


INSERT INTO LISTINGS (renter_id, house_name, price, size, distance, number, street, city, state, zipcode, image_url, isAvailable, create_date) VALUES
(2, 'Foster', 1200, 500, 15.4, 861, 'Sanbarra st', 'Foster City', 'CA', 94404, 'https://photos.zillowstatic.com/cc_ft_1536/ISmmvxzrdz55h91000000000.webp', TRUE, NOW()),
(3, 'South SF', 1000, 300, 2.4, 181, 'Fremont st', 'San Francisco', 'CA', 94105, 'https://djs00nylhf7co.cloudfront.net/assets/img--gallery-interior-52_lg-277eb7b2a425cc901979eb40c134e9b4e3ffe13041dad29d15ec41a4ac35e1b9.jpg', TRUE, NOW());