# Docker Monitoring Stack (Flask + MySQL + Prometheus + Grafana + Nginx)

## Overview

This project is a containerized multi-service infrastructure stack designed to simulate a Linux-based production environment. It demonstrates system administration, service orchestration, and system monitoring using Docker.

The system includes a web application, database layer, reverse proxy, and full observability stack.

## Architecture

User → Nginx → Flask Application → MySQL  
                     ↓  
             Prometheus → Grafana  

## Tech Stack

- Linux environment (Docker-based)
- Docker & Docker Compose
- Flask (Python web application)
- MySQL (database service)
- Nginx (reverse proxy)
- Prometheus (metrics collection)
- Grafana (metrics visualization)

## Services

### Flask Application
- Simple Python web service
- Exposes `/` endpoint
- Exposes `/metrics` endpoint for Prometheus scraping
- Tracks request metrics

### MySQL Database
- Containerized relational database
- Persistent storage using Docker volumes
- Represents production-style database setup

### Prometheus
- Collects time-series metrics
- Scrapes Flask metrics endpoint

### Grafana
- Visualizes metrics from Prometheus
- Used for monitoring dashboards

### Nginx
- Reverse proxy
- Routes traffic to Flask application

## How to Run

```bash
docker compose up -d --build
```

## Access Services

- Flask App: http://SERVER_IP:5050  
- Metrics Endpoint: http://SERVER_IP:5050/metrics  
- Prometheus: http://SERVER_IP:9090  
- Grafana: http://SERVER_IP:3000  
- Nginx: http://SERVER_IP:80  
## Example Metrics

- app_requests_total (HTTP request counter)
- process_cpu_seconds_total
- process_resident_memory_bytes
- Python runtime metrics

## Purpose

This project demonstrates:

- Linux system administration fundamentals
- Docker container orchestration
- Multi-service networking
- Database service integration (MySQL)
- Monitoring and observability concepts
- Basic DevOps workflow understanding

## Future Improvements

- Connect Flask application to MySQL for persistent data storage
- Add Prometheus alerting rules
- Preconfigure Grafana dashboards
- Deploy to cloud (GCP/AWS)
- Add CI/CD pipeline

## Author

Mihai Go
