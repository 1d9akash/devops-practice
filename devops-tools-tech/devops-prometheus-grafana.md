
---
### 5. `Prometheus & Grafana`
---
### What is Prometheus, and how does it collect and store time-series data?
- Prometheus: It is an open-source monitoring tool designed to collect, store and query metrics data. Especially time-series metrics.
- It pulls data from targets like apps, exporters by making HTTP requests. These targets expose a '/metrics' endpoint where prometheus scrape metrics at regular intervals.
- The data is stored in a TSDB: time-series database with labels to filter and group.
---
### How does Grafana visualize Prometheus metrics, and what are the key dashboard components?
- Grafana is a visualization tool that connects to a data-source like prometheus, elasticsearch, loki etc. and helps ous create dashboards.
- We've to add prometheus as a data-source in the Grafana.
- Grafana then uses PromQL to query the data in the prometheus time-series database and display the metrics
- Key dashboard components are Variables, Panels, Rows etc.
---
### What is the role of Prometheus exporters, and how do they help in monitoring external systems?
- Exporters are of small programs that expose metrics in prometheus format / understandable way. They make it easy to monitor things.
- Node Exporter, Windows Exporter, Blackbox Exporter etc.
- ex: node-exporter runs on 9100 port and exposes metrics of CPU, Memory, Disk.. at '/metrics' endpoint. Prometheus scrapes the metrics from these endpoints at regular intervals.
---
### How can you set up alerts in Prometheus using Alertmanager?
- Prometheus uses the concept of 'rules' to define alert conditions. Same can be done via Alertmanager as well along with handling of what to do when an alert fires? like sending an email, notification to slack etc.
---