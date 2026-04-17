from data.database import Base, engine, SessionLocal
from data.models import User, Content, Skill, UserSkill, ContentSkill
import random

Base.metadata.create_all(engine)
db = SessionLocal()

# ✅ CLEAR OLD DATA (important)
db.query(ContentSkill).delete()
db.query(UserSkill).delete()
db.query(Content).delete()
db.query(User).delete()
db.query(Skill).delete()
db.commit()

# Skills
skills = [
    Skill(id=1, name="python"),
    Skill(id=2, name="ml")
]

# Users
users = [
    User(id=i, name=f"User{i}", interests=random.choice(["python", "ml"]))
    for i in range(1, 11)
]

# Content
content = [
    Content(
        id=i,
        title=f"Course {i}",
        category=random.choice(["python", "ml"]),
        difficulty="medium",
        popularity=random.randint(1, 10)
    )
    for i in range(1, 21)
]

# User Skills
user_skills = [
    UserSkill(user_id=u.id, skill_id=random.randint(1, 2), proficiency=1)
    for u in users
]

# Content Skills
content_skills = [
    ContentSkill(content_id=c.id, skill_id=random.randint(1, 2))
    for c in content
]

# Insert all
db.add_all(skills + users + content + user_skills + content_skills)
db.commit()

print("Database seeded successfully!")