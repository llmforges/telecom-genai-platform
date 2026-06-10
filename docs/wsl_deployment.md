# WSL Deployment Guide

## Tested Environment

The Telecom GenAI Deployment Intelligence Platform has been tested on:

* Windows 11
* WSL2
* Ubuntu 22.04 LTS (Jammy)

---

## Verify WSL

Check WSL version:

```bash
wsl --version
```

Verify Ubuntu version:

```bash
lsb_release -a
```

Expected:

```text
for wsl
WSL version: 2.6.3.0
-
Ubuntu 22.04 LTS
Codename: noble
```

---

## Verify Git

```bash
git --version
```
git version 2.43.0
---

## Verify Docker

```bash
$ docker --version
Docker version 29.1.3, build 29.1.3-0ubuntu3~24.04.2```

---

## Verify Docker Compose

```bash
~$ docker compose version
Docker Compose version v5.1.4
~$
```

---

## Clone Repository

```bash
git clone https://github.com/llmforges/telecom-genai-platform.git

cd telecom-genai-platform
```

---

## Verify Project Structure

```bash
ls
```

Expected:

```text
README.md
docker-compose.yml
backend/
docs/
```

---

## Build Application

```bash
docker compose build
```

---

## Start Application

```bash
docker compose up -d
```

---

## Verify Containers

```bash
docker ps
```

Expected:

```text
telecom-api
```

---

## Access Swagger UI

Open:

http://localhost:8000/docs

---

## Stop Application

```bash
docker compose down
```

---

## Troubleshooting

### Docker Not Found

Verify Docker Desktop is installed and WSL integration is enabled.

### Port 8000 Already In Use

Check:

```bash
sudo lsof -i :8000
```

### Container Failed To Start

Check logs:

```bash
docker compose logs
```

### Rebuild Containers

```bash
docker compose down

docker compose build --no-cache

docker compose up -d
```
