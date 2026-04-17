from .database import SessionLocal
from .models import User, Content, Interaction, UserSkill, ContentSkill


class UserRepo:
    def get(self, user_id):
        db = SessionLocal()
        try:
            return db.query(User).filter(User.id == user_id).first()
        finally:
            db.close()


class ContentRepo:
    def get_all(self):
        db = SessionLocal()
        try:
            return db.query(Content).all()
        finally:
            db.close()


class InteractionRepo:
    def add_feedback(self, user_id, content_id, rating):
        db = SessionLocal()
        try:
            interaction = Interaction(
                user_id=user_id,
                content_id=content_id,
                rating=rating,
                type="rating"
            )
            db.add(interaction)
            db.commit()
        finally:
            db.close()


class SkillRepo:
    def get_user_skills(self, user_id):
        db = SessionLocal()
        try:
            return db.query(UserSkill).filter_by(user_id=user_id).all()
        finally:
            db.close()

    def get_content_skills(self):
        db = SessionLocal()
        try:
            return db.query(ContentSkill).all()
        finally:
            db.close()