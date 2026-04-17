def skill_overlap(user_skill_ids, content_skill_ids):
    if not user_skill_ids or not content_skill_ids:
        return 0

    common = set(user_skill_ids) & set(content_skill_ids)
    return len(common)