## Usage

Ceate the local database:
`createdb postgresft`

To run migrations:
`npx db-migrate up`

Create migrations with:
`npx db-migrate create`

Execute migrations with:
`npx db-migrate up` & `npx db-migrate down`

Seed database with:
`poetry run python seed_db.py`

Visualzie data:
`poetry run python visualize.py`

Run python FFT:
`poetry run python fft.py`
