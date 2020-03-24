USE tp;

CREATE TABLE products
(
id INT unsigned NOT NULL AUTO_INCREMENT,
brand VARCHAR(255),
title VARCHAR(255),
price NUMERIC(4, 2),
url VARCHAR(255),
rating NUMERIC(3, 2),
availability VARCHAR(255),
collection_date DATE,
PRIMARY KEY (id)
);

INSERT INTO products (brand, title, price, url, rating, availability, collection_date) VALUES
	('Charmin', 'Charmin 3-Ply', '44.45', 'charmin.com', '4.5', 'Available', '2020-03-22'),
	('Kirkland', 'Kirkland 2-Ply', '9.99','costco.com', '3.7', 'Check In Store', '2020-03-21');

ALTER TABLE products ADD COLUMN count_reviews INTEGER;
ALTER TABLE products MODIFY price NUMERIC(5, 2);
SELECT * FROM products;