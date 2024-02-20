import psycopg2
from psycopg2 import sql
import math
import datetime

db_params = {
    "dbname": "postgresft",
    "user": "postgres",
    "password": "password",
    "host": "localhost",
}

# Sine wave parameters
amplitude = 5  # Maximum amplitude of the sine wave
frequency = 60  # Frequency in Hz
sampling_rate = 1000  # Samples per second
duration = 1  # Duration in seconds for which to generate data

# Calculate the number of samples
num_samples = sampling_rate * duration

# Current timestamp
start_timestamp = datetime.datetime.now()

# Connect to your database
conn = psycopg2.connect(**db_params)
cur = conn.cursor()

# Generate and insert the data
for i in range(num_samples):
    # Calculate the timestamp for this sample
    sample_time = start_timestamp + datetime.timedelta(seconds=i/sampling_rate)
    
    # Generate a sine wave value
    voltage = amplitude * math.sin(2 * math.pi * frequency * (i / sampling_rate))
    
    # Insert the data into the database
    cur.execute(
        sql.SQL("INSERT INTO postgresft_public.voltage (timestamp, voltage) VALUES (%s, %s)"),
        [sample_time, voltage]
    )

# Commit the transaction
conn.commit()

# Close the connection
cur.close()
conn.close()

print(f"Inserted {num_samples} rows into the voltage table.")
