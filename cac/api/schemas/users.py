from sqlalchemy import String, Date
from sqlalchemy.sql.schema import Column
from cac.api.dependencies import Base
from sqlalchemy.dialects.postgresql import UUID
from passlib.hash import bcrypt

class Users(Base):
    __tablename__ = 'users'

    id = Column(UUID(as_uuid=True), primary_key=True)
    username = Column(String, nullable = False)
    email = Column(String, nullable = False)
    password = Column(String, nullable = False)
    creation_date = Column(Date, nullable = False)

    @classmethod
    async def verify_password(self, password):
        return bcrypt.verify(password, self.password)