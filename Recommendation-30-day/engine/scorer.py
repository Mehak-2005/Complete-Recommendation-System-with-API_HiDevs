class Scorer:
    def score(self, user, content, user_skill_ids, content_skills):
        score = content.popularity

        # interest match
        if user.interests in content.category:
            score += 2

        # skill match
        for cs in content_skills:
            if cs.content_id == content.id and cs.skill_id in user_skill_ids:
                score += 1

        return score