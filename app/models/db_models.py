from datetime import datetime

from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base


class Request(Base):
    __tablename__ = "requests"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    address: Mapped[str] = mapped_column(unique=True, index=True)
    timestamp: Mapped[datetime] = mapped_column(default=datetime.utcnow)