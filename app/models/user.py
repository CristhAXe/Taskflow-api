from app.database import Base
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from datetime import datetime
from sqlalchemy import func


class User(Base):
    __tablename__= "user_account"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_name: Mapped[str] = mapped_column(String(30))
    email: Mapped[str]
    password: Mapped[str] 
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())