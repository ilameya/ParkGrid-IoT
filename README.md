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
Adjust parameters such as:
- Number of zones and slots
- Publish interval
- Parking duration limits
- Zone occupancy thresholds
- InfluxDB and Grafana credentials

### 3. start the system:

```bash
docker compose up -d --build
```

Verify all services are running:
```bash
docker ps
```

---
## Service Endpoints

| Service  | URL                                            |
| -------- | ---------------------------------------------- |
| Node-RED | [http://localhost:1880](http://localhost:1880) |
| InfluxDB | [http://localhost:8086](http://localhost:8086) |
| Grafana  | [http://localhost:3000](http://localhost:3000) |

---

**Grafana default credentials:**
- Username: admin
- Password: admin12345

---

## Configuration

System parameters can be adjusted via the **.env** file. 

---

## Alerting

ParkGrid generates two types of alerts:
- OVERSTAY – triggered when a vehicle exceeds the allowed parking duration
- ZONE_FULL – triggered when zone occupancy exceeds a defined threshold

Alerts are published to the MQTT topic /parking/alerts and delivered via Telegram.

---

## Notes
- Start with low thresholds to quickly verify alerts.
- Always check data in Node-RED before debugging Grafana or Flux queries.
- Bucket names in InfluxDB are **case-sensitive**.
- Old data may not match updated schemas; use recent time ranges when testing.
