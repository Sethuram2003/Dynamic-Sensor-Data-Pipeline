# 🔄 Kafka Sensor Data Pipeline

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Kafka](https://img.shields.io/badge/Apache_Kafka-231F20?style=flat&logo=apache-kafka&logoColor=white)](https://kafka.apache.org/)
[![MySQL](https://img.shields.io/badge/MySQL-005C84?style=flat&logo=mysql&logoColor=white)](https://www.mysql.com/)
[![Grafana](https://img.shields.io/badge/Grafana-F2F4F9?style=flat&logo=grafana&logoColor=orange&labelColor=F2F4F9)](https://grafana.com/)

A real-time data pipeline built using Apache Kafka for processing and monitoring sensor data from diesel generators. The system collects sensor readings through a Kafka producer, processes them via a Kafka consumer, stores them in MySQL, and visualizes the data using Grafana dashboards.

## 📊 Dashboard Preview

![Grafana Dashboard](Screenshot from 2024-11-06 17-01-29.png)
*Real-time monitoring of generator metrics including voltage, current, temperature, fuel level, and RPM*

## 🏗️ System Architecture

```mermaid
graph LR
    A[Sensor Data Generator] -->|Produces| B[Kafka Producer]
    B -->|Sends to Topic| C[Kafka Broker]
    C -->|Consumes| D[Kafka Consumer]
    D -->|Stores| E[MySQL Database]
    E -->|Visualizes| F[Grafana Dashboard]
```

## 🚀 Features

- **Real-time Data Generation**: Simulates sensor data including voltage, current, temperature, fuel level, and RPM
- **Kafka Streaming**: Reliable message streaming using Apache Kafka
- **Persistent Storage**: MySQL database for historical data storage
- **Visual Monitoring**: Real-time Grafana dashboards for data visualization
- **Scalable Architecture**: Easy to extend for multiple sensors and data types

## 📋 Prerequisites

- Python 3.8+
- Apache Kafka
- MySQL Server
- Grafana
- Required Python packages:
  ```
  kafka-python
  mysql-connector-python
  ```

## 🛠️ Installation & Setup

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/Kafka-Sensor-DataPipeline.git
   cd Kafka-Sensor-DataPipeline
   ```

2. **Install Dependencies**
   ```bash
   pip install kafka-python mysql-connector-python
   ```

3. **Configure MySQL Database**
   ```sql
   CREATE DATABASE sensor_data;
   USE sensor_data;
   
   CREATE TABLE generator_data (
       timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
       voltage FLOAT,
       current FLOAT,
       temperature FLOAT,
       fuel_level FLOAT,
       rpm FLOAT
   );
   ```

4. **Update Configuration**
   - In `producer.py` and `consumer.py`, update:
     - Kafka broker address
     - MySQL connection details
     - Topic name if needed

## 💻 Usage

1. **Start the Kafka Producer**
   ```bash
   python producer.py
   ```
   This will start generating simulated sensor data.

2. **Start the Kafka Consumer**
   ```bash
   python consumer.py
   ```
   This will begin consuming messages and storing them in MySQL.

3. **Configure Grafana Dashboard**
   - Add MySQL as a data source in Grafana
   - Import the provided dashboard JSON
   - Access the dashboard at `http://localhost:3000`

## 📊 Data Format

The sensor data is transmitted in JSON format:
```json
{
    "voltage": 230.45,      // Voltage in volts
    "current": 25.67,       // Current in amps
    "temperature": 75.89,   // Temperature in Celsius
    "fuel_level": 85.43,    // Fuel level percentage
    "rpm": 2500            // Rotations per minute
}
```

## 🔍 Monitoring

The Grafana dashboard provides real-time visualization of:
- Voltage trends
- Current consumption
- Temperature variations
- Fuel level monitoring
- RPM statistics

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Apache Kafka documentation
- Grafana community
- MySQL documentation
- Python Kafka client developers

## 📞 Support

For support:
- Open an issue in the GitHub repository
- Contact the maintainers
- Check the documentation

---

Made with ❤️ by [Your Name](https://github.com/yourusername)
