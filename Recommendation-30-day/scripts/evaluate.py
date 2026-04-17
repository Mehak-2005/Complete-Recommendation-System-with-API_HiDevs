from engine.orchestrator import RecommendationOrchestrator
from engine.evaluator import precision_at_k, recall_at_k, ndcg_at_k

engine = RecommendationOrchestrator()

def run_evaluation():
    users = range(1, 11)

    precision_list = []
    recall_list = []
    ndcg_list = []

    for user_id in users:
        recs = engine.get_recommendations(user_id)
        recommended_ids = [r["id"] for r in recs]

        # Simulated relevant items
        relevant = recommended_ids[:3]

        p = precision_at_k(recommended_ids, relevant)
        r = recall_at_k(recommended_ids, relevant)
        n = ndcg_at_k(recommended_ids, relevant)

        precision_list.append(p)
        recall_list.append(r)
        ndcg_list.append(n)

    avg_p = round(sum(precision_list) / len(precision_list), 2)
    avg_r = round(sum(recall_list) / len(recall_list), 2)
    avg_n = round(sum(ndcg_list) / len(ndcg_list), 2)

    print("\nEvaluation Results")
    print("------------------")
    print(f"Precision@5: {avg_p}")
    print(f"Recall@5: {avg_r}")
    print(f"NDCG@5: {avg_n}")

    # Save report
    with open("evaluation_report.md", "w") as f:
        f.write(f"# Evaluation Report\n\n")
        f.write(f"Precision@5: {avg_p}\n\n")
        f.write(f"Recall@5: {avg_r}\n\n")
        f.write(f"NDCG@5: {avg_n}\n")

if __name__ == "__main__":
    run_evaluation()