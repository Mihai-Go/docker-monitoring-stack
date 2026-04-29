# Flask Monitoring Stack (Dockerized Observability System)

## Overview

This project is a containerized full-stack observability system built using Docker Compose. It demonstrates real-time monitoring of a Flask web application using Prometheus for metrics collection and Grafana for visualization.

The system is designed with production-style architecture including service separation, reverse proxy routing, persistent storage, and automated dashboard provisioning.

---

## Architecture

The system consists of the following components:

- Flask application (instrumented with Prometheus metrics)
- MySQL database (persistent storage layer)
- Nginx (reverse proxy for application routing)
- Prometheus (metrics collection and time-series storage)
- Grafana (visualization and dashboarding)

### Data Flow

Flask App → Prometheus → Grafana  
Flask App → Nginx → External Requests  
Flask App → MySQL → Persistent data storage  

---

## Services

### Flask Application
- Exposes REST API endpoints
- Provides `/metrics` endpoint for Prometheus scraping
- Tracks request counts and latency

### MySQL Database
- Stores application data (notes)
- Persistent Docker volume

### Prometheus
- Scrapes metrics from Flask app
- Stores time-series data
- Provides query engine (PromQL)

### Grafana
- Visualizes system metrics
- Pre-provisioned dashboards
- Connected to Prometheus datasource automatically

### Nginx
- Acts as reverse proxy
- Routes external traffic to Flask application

---

## Metrics Tracked

- Total HTTP requests (`app_requests_total`)
- Requests per second (rate of requests)
- Average response latency
- Requests grouped by endpoint

---

## Grafana Dashboards

Pre-configured dashboards include:

1. Total Requests
2. Requests per Second
3. Average Response Time
4. Requests by Endpoint

Dashboards are automatically provisioned at startup.

---

## How to Run

### 1. Clone repository

```bash
git clone <repo-url>
cd docker-monitoring-stack
2. Start services
docker-compose up -d --build
3. Access services
Application: http://<server-ip>/
Metrics: http://<server-ip>/metrics
Grafana: http://<server-ip>:3000
Prometheus: http://<server-ip>:9090
Grafana Login
Username: admin
Password: admin (or updated at first login)
Key Features
Fully containerized architecture
Infrastructure-as-code deployment (Docker Compose)
Automated Grafana provisioning
Real-time observability pipeline
Production-style service separation
Persistent storage for database and metrics
Technologies Used
Docker / Docker Compose
Flask (Python)
Prometheus
Grafana
MySQL
Nginx
Author

Mihai-Go
