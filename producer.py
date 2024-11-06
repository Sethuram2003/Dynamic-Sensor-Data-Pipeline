import random
import time
import json
from kafka import KafkaProducer

# Initialize Kafka producer
producer = KafkaProducer(bootstrap_servers='<kafka cluster public ip address>', value_serializer=lambda v: json.dumps(v).encode('utf-8'))

# Function to generate random sensor data
def generate_diesel_generator_data():
    data = {
        "voltage": round(random.uniform(220, 240), 2),      # Voltage in volts
        "current": round(random.uniform(10, 50), 2),        # Current in amps
        "temperature": round(random.uniform(50, 100), 2),   # Temperature in Celsius
        "fuel_level": round(random.uniform(0, 100), 2),     # Fuel level in %
        "rpm": random.randint(1500, 3000)                   # RPM
    }
    return data

try:
    while True:
        # Generate random diesel generator data
        data = generate_diesel_generator_data()
        print(f"Sending data: {data}")
        
        # Send data to Kafka topic 'testing'
        producer.send('testing', value=data)
        
        # Wait a short time before sending the next message
        time.sleep(1)

except KeyboardInterrupt:
    print("Stopped sending messages.")
finally:
    producer.close()
