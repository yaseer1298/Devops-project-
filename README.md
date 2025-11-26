# 🚨 Incident Management API (Flask + Docker)

A simple Incident Management REST API built using **Python Flask**, containerized using **Docker**, and published on **Docker Hub**.

---

## 📌 Features
- Create, read, update, delete (CRUD) incidents  
- REST API using Flask  
- JSON-based responses  
- Fully containerized using Docker  
- Lightweight image (304MB optimized)  
- Ready for Kubernetes, CI/CD, AWS EC2 deployments  

---

## 📁 Project Structure

incident-management/
│── app.py  
│── requirements.txt  
│── Dockerfile  
│── instance/  
│── app/  
│── venv/  

---

## 🚀 How to Run Locally (Without Docker)

```bash
pip install -r requirements.txt
python app.py
