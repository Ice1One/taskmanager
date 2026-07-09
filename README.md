# 🔥 Crypto Price Tracker

> Real-time cryptocurrency price tracking API built with modern DevOps practices

![Python](https://img.shields.io/badge/Python-3.12-blue?style=flat-square&logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-0.139-green?style=flat-square&logo=fastapi)
![Docker](https://img.shields.io/badge/Docker-ready-blue?style=flat-square&logo=docker)
![AWS](https://img.shields.io/badge/AWS-deployed-orange?style=flat-square&logo=amazonaws)
![CI/CD](https://img.shields.io/badge/CI%2FCD-GitHub%20Actions-black?style=flat-square&logo=githubactions)
![Prometheus](https://img.shields.io/badge/Prometheus-monitoring-red?style=flat-square&logo=prometheus)
![Grafana](https://img.shields.io/badge/Grafana-dashboard-orange?style=flat-square&logo=grafana)

---

## 📌 Overview

Crypto Price Tracker is a production-ready REST API that tracks real-time prices of top 20 cryptocurrencies using CoinGecko API. Built with a full DevOps pipeline — from local Docker development to AWS cloud deployment with Load Balancer, RDS PostgreSQL and Prometheus/Grafana monitoring.

---

## 🏗️ Architecture

Internet
↓
AWS Application Load Balancer
↓
EC2 (FastAPI + Docker)
↓
RDS PostgreSQL (price history)
↓
CoinGecko API (real-time prices)
↓
Prometheus (metrics) → Grafana (dashboards)

---

## 🚀 Features

- 📈 **Real-time prices** — top 20 cryptocurrencies via CoinGecko API
- 🔄 **Auto-update** — prices refresh every 5 minutes via background scheduler
- 📊 **Price history** — stores historical data in PostgreSQL
- 🐳 **Dockerized** — runs anywhere with Docker
- ⚙️ **CI/CD** — auto build & deploy via GitHub Actions
- ☁️ **AWS** — EC2 + RDS + Application Load Balancer
- 🏗️ **IaC** — infrastructure described as Terraform code
- 📡 **Monitoring** — Prometheus metrics + Grafana dashboards

---

## 📡 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/` | API info |
| `GET` | `/health` | Health check |
| `GET` | `/metrics` | Prometheus metrics |
| `GET` | `/prices` | All tracked coin prices |
| `GET` | `/price/{coin_id}` | Single coin price |
| `GET` | `/price/{coin_id}/history` | Price history (last 100) |
| `POST` | `/track/{coin_id}` | Start tracking a coin |
| `DELETE` | `/track/{coin_id}` | Stop tracking a coin |

---

## 💻 Tech Stack

| Category | Technology |
|----------|------------|
| **Backend** | Python 3.12, FastAPI |
| **Database** | PostgreSQL (AWS RDS) |
| **ORM** | SQLAlchemy |
| **Scheduler** | APScheduler |
| **HTTP Client** | httpx |
| **Containerization** | Docker, Docker Compose |
| **CI/CD** | GitHub Actions |
| **Cloud** | AWS (EC2, RDS, ALB, VPC, IAM) |
| **IaC** | Terraform |
| **Monitoring** | Prometheus, Grafana |

---

## 🐳 Local Development

**Prerequisites:** Docker, Docker Compose

```bash
# Clone repo
git clone https://github.com/Ice1One/cryptotracker.git
cd cryptotracker

# Start with Docker Compose
docker-compose up -d

# API available at
http://localhost:8000
```

---

## 🔧 Environment Variables

| Variable | Description | Example |
|----------|-------------|---------|
| `DATABASE_URL` | PostgreSQL connection string | `postgresql://user:pass@host/db` |

---

## ☁️ AWS Infrastructure

---

## 🚀 Features

- 📈 **Real-time prices** — top 20 cryptocurrencies via CoinGecko API
- 🔄 **Auto-update** — prices refresh every 5 minutes via background scheduler
- 📊 **Price history** — stores historical data in PostgreSQL
- 🐳 **Dockerized** — runs anywhere with Docker
- ⚙️ **CI/CD** — auto build & deploy via GitHub Actions
- ☁️ **AWS** — EC2 + RDS + Application Load Balancer
- 🏗️ **IaC** — infrastructure described as Terraform code
- 📡 **Monitoring** — Prometheus metrics + Grafana dashboards

---

## 📡 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/` | API info |
| `GET` | `/health` | Health check |
| `GET` | `/metrics` | Prometheus metrics |
| `GET` | `/prices` | All tracked coin prices |
| `GET` | `/price/{coin_id}` | Single coin price |
| `GET` | `/price/{coin_id}/history` | Price history (last 100) |
| `POST` | `/track/{coin_id}` | Start tracking a coin |
| `DELETE` | `/track/{coin_id}` | Stop tracking a coin |

---

## 💻 Tech Stack

| Category | Technology |
|----------|------------|
| **Backend** | Python 3.12, FastAPI |
| **Database** | PostgreSQL (AWS RDS) |
| **ORM** | SQLAlchemy |
| **Scheduler** | APScheduler |
| **HTTP Client** | httpx |
| **Containerization** | Docker, Docker Compose |
| **CI/CD** | GitHub Actions |
| **Cloud** | AWS (EC2, RDS, ALB, VPC, IAM) |
| **IaC** | Terraform |
| **Monitoring** | Prometheus, Grafana |

---

## 🐳 Local Development

**Prerequisites:** Docker, Docker Compose

```bash
# Clone repo
git clone https://github.com/Ice1One/cryptotracker.git
cd cryptotracker

# Start with Docker Compose
docker-compose up -d

# API available at
http://localhost:8000
```

---

## 🔧 Environment Variables

| Variable | Description | Example |
|----------|-------------|---------|
| `DATABASE_URL` | PostgreSQL connection string | `postgresql://user:pass@host/db` |

---

## ☁️ AWS Infrastructure

---

## 🚀 Features

- 📈 **Real-time prices** — top 20 cryptocurrencies via CoinGecko API
- 🔄 **Auto-update** — prices refresh every 5 minutes via background scheduler
- 📊 **Price history** — stores historical data in PostgreSQL
- 🐳 **Dockerized** — runs anywhere with Docker
- ⚙️ **CI/CD** — auto build & deploy via GitHub Actions
- ☁️ **AWS** — EC2 + RDS + Application Load Balancer
- 🏗️ **IaC** — infrastructure described as Terraform code
- 📡 **Monitoring** — Prometheus metrics + Grafana dashboards

---

## 📡 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/` | API info |
| `GET` | `/health` | Health check |
| `GET` | `/metrics` | Prometheus metrics |
| `GET` | `/prices` | All tracked coin prices |
| `GET` | `/price/{coin_id}` | Single coin price |
| `GET` | `/price/{coin_id}/history` | Price history (last 100) |
| `POST` | `/track/{coin_id}` | Start tracking a coin |
| `DELETE` | `/track/{coin_id}` | Stop tracking a coin |

---

## 💻 Tech Stack

| Category | Technology |
|----------|------------|
| **Backend** | Python 3.12, FastAPI |
| **Database** | PostgreSQL (AWS RDS) |
| **ORM** | SQLAlchemy |
| **Scheduler** | APScheduler |
| **HTTP Client** | httpx |
| **Containerization** | Docker, Docker Compose |
| **CI/CD** | GitHub Actions |
| **Cloud** | AWS (EC2, RDS, ALB, VPC, IAM) |
| **IaC** | Terraform |
| **Monitoring** | Prometheus, Grafana |

---

## 🐳 Local Development

**Prerequisites:** Docker, Docker Compose

```bash
# Clone repo
git clone https://github.com/Ice1One/cryptotracker.git
cd cryptotracker

# Start with Docker Compose
docker-compose up -d

# API available at
http://localhost:8000
```

---

## 🔧 Environment Variables

| Variable | Description | Example |
|----------|-------------|---------|
| `DATABASE_URL` | PostgreSQL connection string | `postgresql://user:pass@host/db` |

---

## ☁️ AWS Infrastructure

VPC (devops-vpc) 10.0.0.0/16
├── Public Subnets (eu-central-1a/b/c)
│   ├── Application Load Balancer
│   └── EC2 (Docker + FastAPI)
└── Private Subnets (eu-central-1a/b/c)
└── RDS PostgreSQL

**Terraform** — all infrastructure is described as code in `/terraform` directory:

```bash
cd terraform
terraform init
terraform plan
terraform apply
```

---

## 🔄 CI/CD Pipeline

git push → GitHub Actions
↓
Build Docker image
↓
Push to Docker Hub
↓
SSH to EC2
↓
Pull & restart container

---

## 📊 Monitoring

Real-time monitoring with **Prometheus** + **Grafana** stack.

### Stack

| Tool | Purpose | Port |
|------|---------|------|
| Prometheus | Metrics collection | 9090 |
| Grafana | Visualization & Dashboards | 3000 |

### Dashboards

- 📈 **Total HTTP Requests** — requests count by endpoint
- ⏱ **Average Response Time** — API response time
- 🚀 **Requests per Second** — real-time load

### Run Monitoring Stack

```bash
docker compose -f monitoring-compose.yml up -d
```

### Access

- Grafana: `http://YOUR_EC2_IP:3000` (admin / admin123)
- Prometheus: `http://YOUR_EC2_IP:9090`
- Metrics endpoint: `GET /metrics`

---

## 📊 Tracked Coins (Top 20)

| # | Name | Symbol |
|---|------|--------|
| 1 | Bitcoin | BTC |
| 2 | Ethereum | ETH |
| 3 | Tether | USDT |
| 4 | BNB | BNB |
| 5 | Solana | SOL |
| 6 | USD Coin | USDC |
| 7 | XRP | XRP |
| 8 | Dogecoin | DOGE |
| 9 | Toncoin | TON |
| 10 | Cardano | ADA |
| 11 | Avalanche | AVAX |
| 12 | Shiba Inu | SHIB |
| 13 | Polkadot | DOT |
| 14 | Chainlink | LINK |
| 15 | Bitcoin Cash | BCH |
| 16 | NEAR Protocol | NEAR |
| 17 | Polygon | MATIC |
| 18 | Litecoin | LTC |
| 19 | Internet Computer | ICP |
| 20 | Uniswap | UNI |

---

## 👨‍💻 Author


GitHub: [@Ice1One](https://github.com/Ice1One)


