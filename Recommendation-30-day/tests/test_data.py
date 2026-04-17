from data.database import SessionLocal
from data.models import User

def test_users():
    db = SessionLocal()
    assert db.query(User).count() > 0