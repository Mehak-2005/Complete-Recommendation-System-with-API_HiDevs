from flask import Flask, jsonify, request
from engine.orchestrator import RecommendationOrchestrator
import uuid

app = Flask(__name__)
engine = RecommendationOrchestrator()

@app.before_request
def assign_request_id():
    request.id = str(uuid.uuid4())

@app.route("/recommend/<int:user_id>")
def recommend(user_id):
    recs = engine.get_recommendations(user_id)
    if not recs:
        return jsonify({"error": "User not found"}), 404

    return jsonify({
        "request_id": request.id,
        "recommendations": recs
    })

@app.route("/feedback", methods=["GET", "POST"])
def feedback():
    if request.method == "GET":
        return "Use POST method to send feedback"

    data = request.json

    if not data or "user_id" not in data or "content_id" not in data or "rating" not in data:
        return jsonify({"error": "Invalid input"}), 400

    engine.add_feedback(
        data["user_id"],
        data["content_id"],
        data["rating"]
    )

    return jsonify({"status": "ok"})

@app.route("/health")
def health():
    return jsonify({"status": "ok"})

@app.route("/metrics")
def metrics():
    return jsonify({"cache_size": len(engine.cache)})

if __name__ == "__main__":
    app.run(debug=False)