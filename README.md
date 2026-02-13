# ParkGrid
A real-time IoT-based parking monitoring system designed for smart-city environments.

ParkGrid provides a lightweight, event-driven platform to monitor parking slot occupancy, detect illegal parking behavior, and generate real-time insights and alerts.

The system is fully containerized and can be deployed locally using Docker.

---

## Key Features

- Real-time parking slot occupancy monitoring  
- Zone-level congestion analysis  
- Illegal parking (overstay) detection  
- Interactive dashboards with Grafana  
- Alert notifications via MQTT and Telegram  
- Fully Dockerized and portable deployment  

---

## System Architecture

Sensor Simulator → MQTT Broker → Node-RED → InfluxDB → Grafana → Alerts (MQTT / Telegram)

---

## Technology Stack

- **Messaging:** MQTT (Eclipse Mosquitto)  
- **Processing:** Node-RED  
- **Database:** InfluxDB 2.x  
- **Visualization:** Grafana  
- **Simulation:** Python (paho-mqtt)  
- **Deployment:** Docker, Docker Compose  

---

## Prerequisites

- Docker  
- Docker Compose  

No additional installations are required.

---

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/ilameya/ParkGrid-IoT.git
cd ParkGrid-IoT
```
### 2. Configure Environment Variables
```bash
cp .env.example .env
```
### 3. Start Services:

```bash
docker compose up -d --build
```

Verify all services are running:
```bash
docker ps
```

### 4. Configure InfluxDB:
- Go to InfluxDB  [http://localhost:8086](http://localhost:8086) 
- Use credentianls from .env to create account
- Use Organization and Bucket names from .env 
- Copy the InfluxDB token and use it in your .env INFLUXDB_ADMIN_TOKEN


### 5. Alert Message (Telegram)
- Create a Bot in Telegram using @BotFather. Following this [Tutorial](https://core.telegram.org/bots/features#creating-a-new-bot)
- Copy the token and paste it in the Bot node in Node-RED

### 6. Configure Node-Red
- Go to Node-RED [http://localhost:1880](http://localhost:1880)
- Use your InfluxDB token in the "Write to InfluxDB (parking_status)" node and Deploy
- Use your token for Bot in the Bot node and Deploy 

### 7. Visualization and Monitoring
- Go to Grafana [http://localhost:3000](http://localhost:3000)
- Use credentials from .env if needed


### 8. Stop all services:
```bash
docker compose down
```
---

## Notes
You can Adjust parameters such as:
- Number of zones and slots
- Publish interval
- Parking duration limits
- Zone occupancy thresholds
- InfluxDB and Grafana credentials

Keep in Mind:
- Start with low thresholds to quickly verify alerts.
- Always check data in Node-RED before debugging Grafana or Flux queries.
- Bucket names in InfluxDB are **case-sensitive**.
- Old data may not match updated schemas; use recent time ranges when testing.
