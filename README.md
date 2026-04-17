# Recommendation System (Flask + SQLite)

## 📌 Overview

This project is a simple recommendation system built using Python, Flask, and SQLite.
It provides content recommendations based on user interests, skills, and content popularity.

---

## ⚙️ Features

* Uses user interests and skills for recommendations
* Ranks content using a simple scoring method
* REST API built with Flask
* Feedback system to store user ratings
* In-memory caching for faster responses
* Basic evaluation metrics:

  * Precision@5
  * Recall@5
  * NDCG@5
* Simple load testing using multiple requests

---

## 🏗️ Project Structure

```
day30_capstone/
│
├── data/              # Database and models
├── engine/            # Recommendation logic
├── api/               # Flask API
├── scripts/           # Seed, evaluation, load test
├── tests/             # Basic test cases
├── requirements.txt
├── README.md
└── reco.db
```

---

## 📦 Requirements

Install dependencies:

```
pip install -r requirements.txt
pip install requests
```

---

## ▶️ How to Run

### 1. Seed the database

```
python -m scripts.seed_data
```

### 2. Start the API

```
python -m api.app
```

Server runs at:

```
http://127.0.0.1:5000
```

---

## 🌐 API Endpoints

### Get Recommendations

```
GET /recommend/<user_id>
```

### Submit Feedback

```
POST /feedback
```

Body (JSON):

```
{
  "user_id": 1,
  "content_id": 2,
  "rating": 5
}
```

### Health Check

```
GET /health
```

### Metrics

```
GET /metrics
```

---

## 📊 Evaluation

Run:

```
python -m scripts.evaluate
```

Output:

* Precision@5
* Recall@5
* NDCG@5

Also generates:

```
evaluation_report.md
```

---

## ⚡ Load Testing

Run:

```
python scripts/load_test.py
```

Simulates multiple users hitting the API.

---
## Youtube Video ##
---
https://youtu.be/Teig1iLt0Uk

---

## 🧠 Notes

* This is a rule-based recommendation system (no machine learning model)
* Evaluation uses simulated relevant data
* Designed for learning and demonstration purposes

---

## 👩‍💻 Author

Mehak
