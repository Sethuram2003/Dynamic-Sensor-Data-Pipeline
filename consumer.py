from kafka import KafkaConsumer
import json
import mysql.connector
from datetime import datetime

# MySQL database connection details
db_config = {
    'host': 'localhost',             # Your MySQL server
    'user': 'database_username',                  # Your MySQL username
    'password': 'user_password',     # Your MySQL password
    'database': 'sensor_data'     # Your database name
}

# Initialize Kafka consumer
consumer = KafkaConsumer(
    'testing',                      # Topic name
    bootstrap_servers='<Kafka cluster public ip address>',  # Kafka broker address
    auto_offset_reset='earliest',       # Start from the earliest message
    group_id='my-consumer-group',       # Consumer group ID
    enable_auto_commit=True,            # Auto-commit offsets
    value_deserializer=lambda x: x.decode('utf-8')  # Decode message as a UTF-8 string
)

# Function to connect to MySQL database
def connect_to_db():
    return mysql.connector.connect(**db_config)

# Function to create table if it doesn't exist
def create_table(cursor):
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS generator_data (
            timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            voltage FLOAT,
            current FLOAT,
            temperature FLOAT,
            fuel_level FLOAT,
            rpm FLOAT
        )
    """)

# Function to insert data into the MySQL database
def insert_data(cursor, voltage, current, temperature, fuel_level, rpm):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    cursor.execute("""
        INSERT INTO generator_data (timestamp, voltage, current, temperature, fuel_level, rpm)
        VALUES (%s, %s, %s, %s, %s, %s)
    """, (timestamp, voltage, current, temperature, fuel_level, rpm))

# Connect to the MySQL database
db_connection = connect_to_db()
cursor = db_connection.cursor()

# Create the table if it doesn't exist
create_table(cursor)

# Commit the changes to the database
db_connection.commit()

print("Waiting for messages...")

# Consume messages
try:
    for message in consumer:
        # Attempt to parse the message as JSON
        try:
            data = json.loads(message.value)  # Convert JSON string to dictionary
            
            # Extract parameters
            voltage = data.get("voltage")
            current = data.get("current")
            temperature = data.get("temperature")
            fuel_level = data.get("fuel_level")
            rpm = data.get("rpm")

            # Insert the data into the MySQL database
            insert_data(cursor, voltage, current, temperature, fuel_level, rpm)
            db_connection.commit()

            # Print each parameter
            print("Received data:")
            print(f"  Voltage: {voltage} V")
            print(f"  Current: {current} A")
            print(f"  Temperature: {temperature} °C")
            print(f"  Fuel Level: {fuel_level} %")
            print(f"  RPM: {rpm}")

        except json.JSONDecodeError:
            print("Received a non-JSON message or empty message, skipping...")

except KeyboardInterrupt:
    print("Stopped receiving messages.")

finally:
    # Close the database connection and consumer
    cursor.close()
    db_connection.close()
    consumer.close()
