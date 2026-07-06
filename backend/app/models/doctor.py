from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.database import Base


class Doctor(Base):
    __tablename__ = "doctors"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)

    full_name: Mapped[str] = mapped_column(String(255), nullable=False)

    specialty: Mapped[str] = mapped_column(String(150), nullable=False)

    hospital: Mapped[str] = mapped_column(String(255), nullable=True)

    city: Mapped[str] = mapped_column(String(100), nullable=True)

    phone: Mapped[str] = mapped_column(String(30), nullable=True)

    company_id: Mapped[int] = mapped_column(
        ForeignKey("companies.id"),
        nullable=False,
    )

    company = relationship("Company")