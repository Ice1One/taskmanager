# 🔥 Crypto Price Tracker

> Real-time cryptocurrency price tracking API built with modern DevOps practices

![Python](https://img.shields.io/badge/Python-3.12-blue?style=flat-square&logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-0.139-green?style=flat-square&logo=fastapi)
![Docker](https://img.shields.io/badge/Docker-ready-blue?style=flat-square&logo=docker)
![AWS](https://img.shields.io/badge/AWS-deployed-orange?style=flat-square&logo=amazonaws)
![ECS](https://img.shields.io/badge/ECS-Fargate-orange?style=flat-square&logo=amazonaws)
![CI/CD](https://img.shields.io/badge/CI%2FCD-GitHub%20Actions-black?style=flat-square&logo=githubactions)
![Prometheus](https://img.shields.io/badge/Prometheus-monitoring-red?style=flat-square&logo=prometheus)
![Grafana](https://img.shields.io/badge/Grafana-dashboard-orange?style=flat-square&logo=grafana)
![Terraform](https://img.shields.io/badge/Terraform-IaC-purple?style=flat-square&logo=terraform)

---

## 📌 Overview

Crypto Price Tracker is a production-ready REST API that tracks real-time prices of top 20 cryptocurrencies using CoinGecko API. Built with a full DevOps pipeline — from local Docker development to AWS cloud deployment with ECS Fargate, Load Balancer, RDS PostgreSQL and Prometheus/Grafana monitoring.

---

## 🏗️ Architecture

Internet
↓
AWS Application Load Balancer
↓
ECS Fargate (cryptotracker-service)
↓
RDS PostgreSQL (price history)
↓
CoinGecko API (real-time prices)
↓
Prometheus → Grafana

---

## 🚀 Features

- 📈 **Real-time prices** — top 20 cryptocurrencies via CoinGecko API
- 🔄 **Auto-update** — prices refresh every 5 minutes
- 📊 **Price history** — stores historical data in PostgreSQL
- 🐳 **Dockerized** — runs anywhere with Docker
- ⚙️ **CI/CD** — auto build & deploy via GitHub Actions
- ☁️ **ECS Fargate** — serverless container orchestration
- 🏗️ **IaC** — infrastructure as Terraform code
- 📡 **Monitoring** — Prometheus metrics + Grafana dashboards
- 🔒 **ECR** — private Docker image registry on AWS
- 🌐 **Elastic IP** — static public IP for EC2

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
| **Image Registry** | AWS ECR |
| **Orchestration** | AWS ECS Fargate |
| **CI/CD** | GitHub Actions |
| **Cloud** | AWS (ECS, ECR, RDS, ALB, VPC, IAM) |
| **IaC** | Terraform |
| **Monitoring** | Prometheus, Grafana |

---

## 🐳 Local Development

```bash
git clone https://github.com/Ice1One/cryptotracker.git
cd cryptotracker
docker-compose up -d
```

API: `http://localhost:8000`
Docs: `http://localhost:8000/docs`

---

## 🔧 Environment Variables

| Variable | Description |
|----------|-------------|
| `DATABASE_URL` | PostgreSQL connection string |

---

## ☁️ AWS Infrastructure

VPC (devops-vpc) 10.0.0.0/16
├── Public Subnets (eu-central-1a/b/c)
│   ├── Application Load Balancer
│   └── ECS Fargate (cryptotracker-service)
└── Private Subnets (eu-central-1a/b/c)
└── RDS PostgreSQL

**AWS Services:**
| Service | Purpose |
|---------|---------|
| **ECR** | Private Docker image registry |
| **ECS Fargate** | Serverless container orchestration |
| **ALB** | Application Load Balancer |
| **RDS PostgreSQL** | Managed database |
| **VPC** | Isolated network |
| **IAM** | Access management |
| **Elastic IP** | Static public IP |
| **Secrets Manager** | Secure storage for database credentials |
| **VPC Endpoints** | Private connectivity to AWS services |

```bash
cd terraform
terraform init
terraform apply
```

---

## 🔄 CI/CD Pipeline

git push → GitHub Actions
↓
Build Docker image
↓
Push to AWS ECR
↓
Deploy to ECS Fargate
↓
Zero-downtime deployment

---

## 📊 Monitoring

| Tool | Purpose | Port |
|------|---------|------|
| Prometheus | Metrics collection | 9090 |
| Grafana | Visualization | 3000 |

## 🔒 Security

- **AWS Secrets Manager** — database credentials stored securely, never in code
- **VPC Endpoints** — private connectivity to AWS services without internet:
  - `secretsmanager` — secure secret retrieval
  - `ecr.api` / `ecr.dkr` — private ECR image pulling
  - `cloudwatch logs` — private log streaming
- **IAM Roles** — least privilege access for ECS tasks
- **Private Subnets** — RDS database not exposed to internet


**Dashboards:**
- 📈 Total HTTP Requests
- ⏱ Average Response Time
- 🚀 Requests per Second

```bash
docker compose -f monitoring-compose.yml up -d
```

- Grafana: `http://EC2_IP:3000` (admin / admin123)
- Prometheus: `http://EC2_IP:9090`
- Metrics: `GET /metrics`

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

---


