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

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(df['timestamp'], df['voltage'], label='Voltage')
plt.title('Voltage Over Time')
plt.xlabel('Time')
plt.ylabel('Voltage (V)')
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)  # Rotate date labels for better readability
plt.tight_layout()  # Adjust layout to not cut off labels
plt.show()
