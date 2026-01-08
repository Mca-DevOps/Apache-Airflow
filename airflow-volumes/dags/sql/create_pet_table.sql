--- SQL script to create the 'pet' table if it does not already exist

CREATE TABLE IF NOT EXISTS pet (
            pet_id SERIAL PRIMARY KEY,
            name VARCHAR NOT NULL,
            pet_type VARCHAR NOT NULL,
            birth_date DATE NOT NULL,
            row_created VARCHAR NOT NULL,
            OWNER VARCHAR NOT NULL);