FROM nodered/node-red:4.0.5

RUN npm install --unsafe-perm --no-update-notifier --no-fund --only=production \
    node-red-contrib-influxdb \
    node-red-contrib-telegrambot

COPY flows.json /data/flows.json
