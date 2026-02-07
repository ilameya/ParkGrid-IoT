import json
import os
import random
import time
from datetime import datetime, timezone

import paho.mqtt.client as mqtt

MQTT_HOST = os.getenv("MQTT_HOST", "mosquitto")
MQTT_PORT = int(os.getenv("MQTT_PORT", "1883"))

PUBLISH_INTERVAL = int(os.getenv("SIM_PUBLISH_INTERVAL_SEC", "60"))

ZONES = os.getenv("SIM_ZONES", "center,residential").split(",")
SLOTS_PER_ZONE = int(os.getenv("SIM_SLOTS_PER_ZONE", "20"))

# Probability that a free slot becomes occupied in a tick
ARRIVAL_PROB = 0.08
# Probability that an occupied slot becomes free in a tick (leaving)
DEPART_PROB = 0.005

def now_iso():
    return datetime.now(timezone.utc).isoformat()

def build_slots():
    slots = {}
    for z in ZONES:
        z = z.strip()
        slots[z] = {}
        for i in range(1, SLOTS_PER_ZONE + 1):
            slot_id = f"slot_{i:02d}"
            slots[z][slot_id] = {"occupied": 0, "parking_duration": 0}
    return slots

def main():
    slots = build_slots()

    client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
    client.connect(MQTT_HOST, MQTT_PORT, 60)
    client.loop_start()

    while True:
        for zone, zone_slots in slots.items():
            for slot_id, st in zone_slots.items():
                # stochastic transitions
                if st["occupied"] == 0:
                    if random.random() < ARRIVAL_PROB:
                        st["occupied"] = 1
                        st["parking_duration"] = 0
                else:
                    # if occupied, time passes
                    st["parking_duration"] += PUBLISH_INTERVAL / 60.0  # minutes
                    # occasionally depart
                    if random.random() < DEPART_PROB:
                        st["occupied"] = 0
                        st["parking_duration"] = 0
                
                slot_uid = f"{zone}-{slot_id}"
                 
                payload = {
                    "slot_uid": slot_uid,
                    "slot_id": slot_id,
                    "zone": zone,
                    "occupied": int(st["occupied"]),
                    "parking_duration": round(st["parking_duration"], 2),
                    "timestamp": now_iso()
                }

                topic = f"/parking/{zone}/{slot_id}/status"
                client.publish(topic, json.dumps(payload), qos=0, retain=False)

        time.sleep(PUBLISH_INTERVAL)

if __name__ == "__main__":
    main()
