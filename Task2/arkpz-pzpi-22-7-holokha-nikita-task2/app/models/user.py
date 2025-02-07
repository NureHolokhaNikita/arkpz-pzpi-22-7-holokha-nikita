from app import db
from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from app.utils.error_handler import ErrorHandler
from app.responses.user_response import UserResponse

class User(db.Model):
    __tablename__ = "user"

    user_id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False, unique=True)
    password = Column(String(255), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<User {self.name}>"

    @staticmethod
    def get_all_users():
        users = User.query.all()
        return UserResponse.response_all_users(users)

    @staticmethod
    def get_user_by_id(user_id):
        user = User.query.get(user_id)
        return UserResponse.response_user(user)

    @staticmethod
    def create_user(data):
        try:
            new_user = User(
                name=data.get("name"),
                email=data.get("email"),
                password=data.get("password")
            )
            db.session.add(new_user)
            db.session.commit()
            return {"message": "User created successfully"}, 201
        except Exception as e:
            db.session.rollback()
            return ErrorHandler.handle_error(e, "Failed to create user", 500)

    @staticmethod
    def update_user(user_id, data):
        try:
            user = User.query.get(user_id)
            if not user:
                return {"error": "User not found"}, 404

            user.name = data.get("name", user.name)
            user.email = data.get("email", user.email)
            db.session.commit()
            return {"message": "User updated successfully"}, 200
        except Exception as e:
            db.session.rollback()
            return ErrorHandler.handle_error(e, "Failed to update user", 500)

    @staticmethod
    def delete_user(user_id):
        try:
            user = User.query.get(user_id)
            if not user:
                return {"error": "User not found"}, 404

            db.session.delete(user)
            db.session.commit()
            return {"message": "User deleted successfully"}, 200
        except Exception as e:
            db.session.rollback()
            return ErrorHandler.handle_error(e, "Failed to delete user", 500)
