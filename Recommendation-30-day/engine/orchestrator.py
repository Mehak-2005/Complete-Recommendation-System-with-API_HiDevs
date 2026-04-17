from .candidate_gen import CandidateGenerator
from .scorer import Scorer
from data.repositories import UserRepo, ContentRepo, SkillRepo, InteractionRepo

class RecommendationOrchestrator:
    def __init__(self):
        self.user_repo = UserRepo()
        self.content_repo = ContentRepo()
        self.skill_repo = SkillRepo()
        self.interaction_repo = InteractionRepo()

        self.generator = CandidateGenerator()
        self.scorer = Scorer()

        self.cache = {}

    def get_recommendations(self, user_id, limit=5):
        if user_id in self.cache:
            return self.cache[user_id]

        user = self.user_repo.get(user_id)
        if not user:
            return []

        content = self.content_repo.get_all()

        user_skills = self.skill_repo.get_user_skills(user_id)
        content_skills = self.skill_repo.get_content_skills()

        user_skill_ids = [us.skill_id for us in user_skills]

        candidates = self.generator.generate(content)

        scored = [
            (c, self.scorer.score(user, c, user_skill_ids, content_skills))
            for c in candidates
        ]

        ranked = sorted(scored, key=lambda x: x[1], reverse=True)

        results = [
            {
                "id": c.id,
                "title": c.title,
                "explanation": f"Recommended because it matches your interest '{user.interests}' and related skills"
                
            }
            for c, _ in ranked[:limit]
        ]

        self.cache[user_id] = results
        return results

    def add_feedback(self, user_id, content_id, rating):
        self.interaction_repo.add_feedback(user_id, content_id, rating)

        if user_id in self.cache:
            del self.cache[user_id]