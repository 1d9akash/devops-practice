
---
### 4. `Ambassador Edge Stack`
---
### What is Ambassador Edge Stack, and how does it act as an API Gateway for Kubernetes?
- Ambassador is an Ingress + API Gateway built on Envoy.
- Manages external traffic, TLS, routing, and rate-limiting for microservices.
---
### How does Ambassador handle traffic routing and load balancing for microservices?
- It uses annotations or CRDs to define routes.
- Routes based on path, header, host.
- Performs load balancing across Kubernetes services.
---
### What is the difference between an Ingress Controller and an API Gateway like Ambassador?
- Ingress Controller: Basic routing.
- API Gateway: Rich features like rate-limiting, auth, observability.
---
### How does Ambassador integrate with observability tools like Prometheus and Grafana?
- Exposes metrics via '/metrics' endpoint.
- Scrape with Prometheus.
- Visualize with Grafana dashboards.
---