# 🚀 Complete Recommendation System with API

## 📌 Overview

This project implements a complete Recommendation System using Python. It integrates a database, recommendation engine, and REST API to simulate how platforms like Netflix and Amazon provide personalized suggestions.

The system uses collaborative filtering, popularity-based scoring, and evaluation metrics to generate meaningful recommendations.

---

## 🧠 Key Features

* 🔹 Recommendation Engine (Day 29 integration)
* 🔹 SQLite Database (6 tables)
* 🔹 REST API using Flask
* 🔹 Candidate Generation + Scoring + Ranking
* 🔹 Cold Start Handling
* 🔹 Feedback Recording System
* 🔹 Evaluation Metrics (Precision, Recall, NDCG)
* 🔹 Request Logging and Metrics Tracking
* 🔹 Unit Testing (Pytest)

---

## 📂 Project Structure

copy


day30_capstone/
├── data/              # Database layer
├── engine/            # Recommendation engine
├── api/               # Flask API
├── scripts/           # Utilities (seed, evaluate)
├── tests/             # Unit tests
├── requirements.txt
├── README.md
└── evaluation_report.md

---

## ⚙️ Technologies Used

* Python 3.x
* Flask
* SQLite
* Pytest

---

## ▶️ How to Run

### 1. Clone Repository

Bash


git clone <your-repo-url>
cd day30_capstone

---

### 2. Install Dependencies

Bash


pip install -r requirements.txt

---

### 3. Seed Database

Bash


python -m scripts.seed_data

---

### 4. Run API Server

Bash


python -m api.app

---

### 5. Open in Browser (Codespaces)

* Go to PORTS tab
* Open port 5000
* Use endpoints below

---

## 🌐 API Endpoints

| Endpoint               | Method | Description          |
| ---------------------- | ------ | -------------------- |
| /                    | GET    | API status           |
| /health              | GET    | Health check         |
| /recommend/<user_id> | GET    | Get recommendations  |
| /feedback            | POST   | Record user feedback |
| /metrics             | GET    | System metrics       |

---

## 📊 Example Output

### Recommendation

JSON


{
  "user": "u1",
  "recommendations": [
    {
      "item": "c1",
      "reason": "Recommended based on relevance and popularity"
    }
  ]
}

---

## 🧪 Testing

Run all tests:

copy


pytest

Expected:

copy


7 passed

---

## 📈 Evaluation

Run evaluation:

Bash


python -m scripts.evaluate

Example output:

copy


{'precision': 0.66, 'recall': 1.0, 'ndcg': 0.69}

---

## 🎯 Results

* ✔ High Recall (1.0)
* ✔ Good Precision (~0.66)
* ✔ Strong Ranking Performance

---

## 🔮 Future Improvements

* Machine Learning-based recommendations
* Knowledge graph integration
* Real-time personalization
* Frontend dashboard

---

## 👨‍💻 Author

Mehak

---

## 📌 Note

This project demonstrates the core architecture of modern recommendation systems and can be extended for real-world applications.
