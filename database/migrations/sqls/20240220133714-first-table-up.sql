CREATE TABLE voltage (
    id SERIAL PRIMARY KEY,
    timestamp TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    voltage FLOAT NOT NULL
);