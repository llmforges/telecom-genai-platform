# Azure Deployment Guide

## Telecom GenAI Deployment Intelligence Platform

---

# 1. Purpose

This document describes the complete deployment procedure for deploying the Telecom GenAI Deployment Intelligence Platform to Microsoft Azure using an Ubuntu Virtual Machine and Docker.

This deployment guide has been validated on:

* Microsoft Azure
* Ubuntu Server 24.04 LTS
* Docker
* Docker Compose

---

# 2. Deployment Architecture

```
Developer
    │
    ▼
GitHub Repository
    │
    ▼
Azure Virtual Machine
(Ubuntu 24.04 LTS)
    │
    ▼
Docker Engine
    │
    ▼
Docker Compose
    │
    ▼
Telecom GenAI Platform
(FastAPI)
    │
    ▼
Public Internet

http://<Public-IP>:8000/docs
```

---

# 3. Azure Resources Used

The following Azure resources were created during deployment.

| Resource               | Purpose                             |
| ---------------------- | ----------------------------------- |
| Resource Group         | Logical container for all resources |
| Virtual Machine        | Hosts the application               |
| Virtual Network        | Internal networking                 |
| Network Security Group | Firewall configuration              |
| Network Interface      | VM networking                       |
| Public IP              | Public access to application        |
| Managed Disk           | Operating system disk               |

---

# 4. Environment Details

Operating System

```
Ubuntu Server 24.04 LTS
```

VM Size

```
Standard B2s

2 vCPUs
4 GB RAM
```

Region

```
South India
```

---

# 5. Create Resource Group

Navigate to

Azure Portal

↓

Resource Groups

↓

Create

Configuration

```
Name

rg-telecom-genai-dev
```

```
Region

South India
```

Create the Resource Group.

---

# 6. Create Virtual Machine

Navigate

Azure Portal

↓

Virtual Machines

↓

Create

Configuration

VM Name

```
telecom-genai-vm
```

Image

```
Ubuntu Server 24.04 LTS
```

VM Size

```
Standard B2s
```

Authentication

```
SSH Public Key
```

Username

```
<username>
```

Paste your SSH Public Key generated from WSL.

---

# 7. Generate SSH Keys

On local WSL

```
ssh-keygen -t ed25519
```

Display public key

```
cat ~/.ssh/id_ed25519.pub
```

Copy the public key and paste it into Azure while creating the VM.

---

# 8. Connect to Azure VM

From Azure Portal

VM

↓

Connect

↓

Native SSH

Example

```
ssh azureuser@<Public-IP>
```

Accept host key

```
yes
```

---

# 9. Verify Virtual Machine

Execute

```
lsb_release -a

whoami

hostname

free -h

df -h
```

Verify

* Ubuntu Version
* Logged in User
* Available Memory
* Disk Space

---

# 10. Install Docker

Update packages

```
sudo apt update
```

Install Docker

```
sudo apt install docker.io docker-compose-v2 git -y
```

If docker-compose-v2 is unavailable

```
sudo apt install docker-compose-plugin -y
```

Allow current user to execute Docker commands

```
sudo usermod -aG docker $USER
```

Logout

```
exit
```

Reconnect using SSH.

---

# 11. Verify Installation

```
docker --version

docker compose version

git --version
```

Expected

Docker Engine installed

Docker Compose available

Git available

---

# 12. Clone Repository

```
git clone https://github.com/llmforges/telecom-genai-platform.git
```

Navigate

```
cd telecom-genai-platform
```

---

# 13. Verify Repository

Expected structure

```
telecom-genai-platform/

backend/

docs/

samples/

README.md

docker-compose.yml
```

---

# 14. Build Application

```
docker compose build
```

Docker downloads

* Python Image
* Dependencies

Builds

Telecom GenAI Platform Docker Image

---

# 15. Start Application

```
docker compose up -d
```

Verify

```
docker ps
```

Expected

```
telecom-api
```

Container status should be

```
Up
```

---

# 16. Configure Network Security Group

Navigate

Azure Portal

↓

Virtual Machine

↓

Networking

↓

Add Inbound Rule

Configuration

Source

```
Any
```

Protocol

```
TCP
```

Destination Port

```
8000
```

Action

```
Allow
```

Priority

```
310
```

Rule Name

```
allow-fastapi-8000
```

Save.

---

# 17. Verify Deployment

Open browser

```
http://<Public-IP>:8000/docs
```

Expected

FastAPI Swagger UI should open successfully.

Verify APIs

* GET /
* POST /documents/upload
* GET /documents
* GET /documents/{id}

---

# 18. Upload Sample PDF

Open

POST /documents/upload

Upload

```
samples/ims_deployment_architecture_guide.pdf
```

Verify

* Upload successful
* JSON generated
* Metadata stored

---

# 19. Runtime Commands

Check running containers

```
docker ps
```

View logs

```
docker compose logs
```

Follow logs

```
docker compose logs -f
```

Restart

```
docker compose restart
```

Stop

```
docker compose down
```

Rebuild

```
docker compose up --build
```

---

# 20. Troubleshooting

## Docker not found

```
docker --version
```

If unavailable

```
sudo apt install docker.io
```

---

## Permission denied while running Docker

```
sudo usermod -aG docker $USER
```

Logout and login again.

---

## Port 8000 inaccessible

Verify

* NSG rule exists
* Docker container is running
* FastAPI is listening on port 8000

Check

```
docker ps
```

---

## Container exited

Inspect logs

```
docker compose logs
```

---

# 21. Cleanup

After testing, remove all Azure resources to avoid unnecessary charges.

Recommended method

Delete the Resource Group.

Navigate

Azure Portal

↓

Resource Groups

↓

rg-telecom-genai-dev

↓

Delete Resource Group

This removes

* Virtual Machine
* Network Interface
* Public IP
* Virtual Network
* Network Security Group
* Managed Disk

Note:

Azure-managed resource groups such as

```
NetworkWatcherRG
```

do not need to be deleted.

---

# 22. Deployment Summary

Deployment Status

| Component      | Status |
| -------------- | ------ |
| Azure VM       | ✅      |
| Ubuntu 24.04   | ✅      |
| Docker         | ✅      |
| Docker Compose | ✅      |
| GitHub Clone   | ✅      |
| FastAPI        | ✅      |
| Swagger UI     | ✅      |
| Public Access  | ✅      |

---

# 23. Future Enhancements

The Azure deployment will be extended in future releases to include

* Azure Blob Storage
* Azure Container Registry (ACR)
* Azure Kubernetes Service (AKS)
* Azure AI Foundry Integration
* Azure Key Vault
* Azure Monitor
* Application Insights
* GPU-enabled Virtual Machines for LLM inference
* CI/CD deployment using GitHub Actions
* Production deployment architecture

These enhancements are planned for subsequent project phases beyond MVP 1.0.

