CREATE SCHEMA postgresft_public;

CREATE TABLE postgresft_public.voltage (
    id SERIAL PRIMARY KEY,
    timestamp TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    voltage FLOAT NOT NULL
);