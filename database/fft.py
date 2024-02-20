import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sqlalchemy import create_engine

# Database connection parameters
db_params = {
    "dbname": "postgresft",
    "user": "postgres",
    "password": "password",
    "host": "localhost",
    "port": "5432"
}

# SQLAlchemy engine for pandas
engine = create_engine(f"postgresql+psycopg2://{db_params['user']}:{db_params['password']}@{db_params['host']}:{db_params['port']}/{db_params['dbname']}")

# SQL query to select all rows from the voltage table
sql_query = "SELECT * FROM postgresft_public.voltage ORDER BY timestamp ASC;"

# Use pandas to load the query results into a DataFrame
df = pd.read_sql(sql_query, engine)

# Close the database connection
engine.dispose()

# Calculate the sampling rate
time_diffs = np.diff(df['timestamp'].astype('int64') // 10**9)  # Convert to seconds and find differences
sampling_rate = 1 / np.mean(time_diffs)  # Average time difference between samples

# Perform the FFT
voltage_fft = np.fft.fft(df['voltage'])

# Calculate the frequency bins
n = len(df['voltage'])  # Number of samples
frequencies = np.fft.fftfreq(n, d=1/sampling_rate)

# Plot the magnitude of the FFT
plt.figure(figsize=(10, 6))
plt.plot(frequencies, np.abs(voltage_fft), label='Magnitude of FFT')
plt.title('Frequency Components of Voltage Signal')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude')
plt.grid(True)
plt.legend()
plt.xlim(0, sampling_rate / 2)  # Display only the positive frequencies up to the Nyquist frequency
plt.show()
