"""Models module."""

from sqlalchemy import Column, String, Boolean, Integer

from app.infrastructure.database import Base


class UserEntity(Base):

    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    def __repr__(self):
        return f"<User(id={self.id}, " \
               f"email=\"{self.email}\", " \
               f"hashed_password=\"{self.hashed_password}\", " \
               f"is_active={self.is_active})>"
