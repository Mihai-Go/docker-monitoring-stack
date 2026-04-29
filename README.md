# Flask Monitoring Stack (Dockerized Observability System)

## Overview

This project is a fully containerized observability stack built using Docker Compose. It demonstrates real-time monitoring of a Flask web application using Prometheus for metrics collection and Grafana for visualization.

The system follows production-style architecture principles including service separation, reverse proxy routing, persistent storage, and automated dashboard provisioning.

---

## Architecture

The system consists of the following components:

- Flask application (instrumented with Prometheus metrics)
- MySQL database (persistent storage layer)
- Nginx (reverse proxy for routing traffic)
- Prometheus (metrics collection and time-series storage)
- Grafana (visualization and dashboards)

### Data Flow

Flask App → Prometheus → Grafana  
Flask App → Nginx → External Requests  
Flask App → MySQL → Persistent Storage  

---

## Services

### Flask Application
- REST API built with Flask
- Exposes `/metrics` endpoint for Prometheus scraping
- Tracks HTTP request counts and latency

### MySQL Database
- Stores application data (notes)
- Uses Docker volume for persistence

### Prometheus
- Scrapes metrics from Flask application
- Stores time-series data
- Provides PromQL query engine≈

### Grafana
- Visualizes system metrics
- Pre-provisioned dashboards
- Automatically connected to Prometheus

### Nginx
- Reverse proxy for Flask application
- Handles external HTTP routing

---

## Setup Instructions

### Clone repository

```bash
## Setup Instructions

### Clone repository

```bash
git clone <repo-url>
cd docker-monitoring-stack
Start services
docker-compose up -d --build
Access Services
Application: http://<server-ip>/
Metrics: http://<server-ip>/metrics
Grafana: http://<server-ip>:3000
Prometheus: http://<server-ip>:9090
Grafana Login
Username: admin
Password: admin (or updated after first login)
Key Features
Fully containerized microservices architecture
Infrastructure-as-code with Docker Compose
Automated Grafana provisioning (no manual setup required)
Real-time observability pipeline
Persistent storage for database and metrics
Production-style reverse proxy setup with Nginx
Metrics Tracked
Total HTTP requests (app_requests_total)
Requests per second (rate of requests)
Average response latency
Requests grouped by endpoint
Grafana Dashboards

Pre-configured dashboards include:

Total Requests
Requests per Second
Average Response Time
Requests by Endpoint

Dashboards are automatically loaded at startup.

Technologies Used
Docker / Docker Compose
Flask (Python)
Prometheus
Grafana
MySQL
Nginx
Author

Mihai-Go

Notes

This project is designed as a DevOps / Backend Engineering portfolio demonstration showcasing observability, container orchestration, and production-style system design principles.
