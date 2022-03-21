from app.models import User
from app.database import Session


class UserService:
    @staticmethod
    def create(username):
        user = User(username=username)

        with Session() as session:
            session.add(user)
            session.commit()

    @staticmethod
    def get_all():
        with Session() as session:
            return session.query(User).all()
