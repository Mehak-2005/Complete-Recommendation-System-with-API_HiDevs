from engine.orchestrator import RecommendationOrchestrator

def test_recommendations():
    engine = RecommendationOrchestrator()
    recs = engine.get_recommendations(1)
    assert isinstance(recs, list)