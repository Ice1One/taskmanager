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
![WAF](https://img.shields.io/badge/AWS_WAF-protected-red?style=flat-square&logo=amazonaws)

---

## 📌 Overview

Crypto Price Tracker is a production-ready REST API that tracks real-time prices of top 20 cryptocurrencies using CoinGecko API. Built with a full DevOps pipeline — from local Docker development to AWS cloud deployment with ECS Fargate, Load Balancer, RDS PostgreSQL, Prometheus/Grafana monitoring, AWS WAF protection and Auto Scaling.

---

## 📸 Screenshots

### Grafana Monitoring Dashboard
![Grafana](screenshots/grafana.png)

### AWS WAF Protection
![WAF](screenshots/waf.png)

### ECS Cluster
![ECS Cluster](screenshots/ecs-cluster.png)

### ECS Auto Scaling
![Auto Scaling](screenshots/ecs-autoscaling.png)

### CloudWatch Alarm
![CloudWatch](screenshots/cloudwatch-alarm.png)

### ECR Images
![ECR](screenshots/ecr-images.png)

---

## 🏗️ Architecture

Internet
↓
AWS WAF (DDoS, SQL injection protection)
↓
AWS Application Load Balancer
↓
ECS Fargate (Auto Scaling 1-5 tasks)
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
- ⚙️ **CI/CD** — auto build & deploy via GitHub Actions + pytest
- ☁️ **ECS Fargate** — serverless container orchestration
- 📈 **Auto Scaling** — 1 to 5 tasks based on CPU utilization
- 🛡️ **AWS WAF** — protection from DDoS, SQL injection, XSS
- 🔒 **Secrets Manager** — secure credentials storage
- 📡 **Monitoring** — Prometheus metrics + Grafana dashboards
- 🚨 **CloudWatch Alarms** — email alerts when CPU > 80%
- 🏗️ **IaC** — infrastructure as Terraform code
- 🌐 **Elastic IP** — static public IP

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
| **CI/CD** | GitHub Actions + pytest |
| **Cloud** | AWS (ECS, ECR, RDS, ALB, VPC, IAM, WAF) |
| **IaC** | Terraform |
| **Monitoring** | Prometheus, Grafana |
| **Security** | AWS Secrets Manager, VPC Endpoints, WAF |
| **Alerting** | CloudWatch Alarms + SNS |

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
| `DATABASE_URL` | PostgreSQL connection string or AWS Secrets Manager ARN |

---

## ☁️ AWS Infrastructure

VPC (devops-vpc) 10.0.0.0/16
├── Public Subnets (eu-central-1a/b/c)
│   ├── AWS WAF
│   ├── Application Load Balancer
│   └── ECS Fargate (cryptotracker-service)
└── Private Subnets (eu-central-1a/b/c)
└── RDS PostgreSQL

**AWS Services:**

| Service | Purpose |
|---------|---------|
| **ECR** | Private Docker image registry |
| **ECS Fargate** | Serverless container orchestration |
| **ALB** | Application Load Balancer (L7) |
| **RDS PostgreSQL** | Managed database |
| **VPC** | Isolated network |
| **IAM** | Access management |
| **Elastic IP** | Static public IP |
| **Secrets Manager** | Secure credentials storage |
| **VPC Endpoints** | Private connectivity to AWS services |
| **WAF** | DDoS, SQL injection, XSS protection |
| **CloudWatch** | Monitoring and alerting |
| **SNS** | Email notifications |

```bash
cd terraform
terraform init
terraform apply
```

---

## 🔄 CI/CD Pipeline

git push
↓
GitHub Actions
↓
pytest tests (fail = stop)
↓
docker build
↓
ECR login + docker push
↓
ECS pulls image from ECR
↓
ECS pulls DATABASE_URL from Secrets Manager
↓
ECS Fargate starts new container
↓
ALB health check → /health
↓
Traffic routed to new container
↓
Zero-downtime deployment

---

## 🛡️ Security

- **AWS WAF** — blocks DDoS, SQL injection, XSS attacks
  - Core rule set
  - Known bad inputs
  - SQL database protection
- **AWS Secrets Manager** — database credentials stored securely, never in code
- **VPC Endpoints** — private connectivity without internet:
  - `secretsmanager` — secure secret retrieval
  - `ecr.api` / `ecr.dkr` — private ECR image pulling
  - `cloudwatch logs` — private log streaming
- **IAM Roles** — least privilege access for ECS tasks
- **Private Subnets** — RDS not exposed to internet

---

## 📈 Auto Scaling

ECS Service automatically scales based on CPU utilization:

CPU < 70%  → 1 task (minimum)
CPU > 70%  → scales up to 5 tasks
CPU drops  → scales back down

- **Minimum tasks:** 1
- **Maximum tasks:** 5
- **Metric:** ECSServiceAverageCPUUtilization
- **Target:** 70%
- **Scale-out cooldown:** 60 seconds
- **Scale-in cooldown:** 120 seconds

---

## 🚨 Monitoring & Alerting

| Tool | Purpose | Port |
|------|---------|------|
| Prometheus | Metrics collection | 9090 |
| Grafana | Visualization | 3000 |
| CloudWatch | AWS metrics & alarms | - |
| SNS | Email notifications | - |

**CloudWatch Alarms:**
- 🔴 CPU > 80% → email alert via SNS

**Grafana Dashboards:**
- 📈 Total HTTP Requests
- ⏱ Average Response Time
- 🚀 Requests per Second

```bash
docker compose -f monitoring-compose.yml up -d
```

- Grafana: `http://EC2_IP:3000` (admin / admin123)
- Prometheus: `http://EC2_IP:9090`

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

**Ice1One** — Junior DevOps Engineer
GitHub: [@Ice1One](https://github.com/Ice1One)

---

