-- populate pet table
INSERT INTO pet(name, pet_type, birth_date, row_created, OWNER) VALUES ( 'Max', 'Dog', '2018-07-05','{{ params.current_date }}', 'Jane');
INSERT INTO pet(name, pet_type, birth_date, row_created, OWNER) VALUES ( 'Susie', 'Cat', '2019-05-01','{{ params.current_date }}', 'Phil');
INSERT INTO pet(name, pet_type, birth_date, row_created, OWNER) VALUES ( 'Lester', 'Hamster', '2020-06-23','{{ params.current_date }}', 'Lily');
INSERT INTO pet(name, pet_type, birth_date, row_created, OWNER) VALUES ( 'Quincy', 'Parrot', '2013-08-11','{{ params.current_date }}', 'Anne');