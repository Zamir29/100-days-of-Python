"""Database models for Day 64 (Top 10 Movies)."""

from extensions import db
from sqlalchemy import Integer, String, Float
from sqlalchemy.orm import Mapped, mapped_column


class Movie(db.Model):
    """Represents a ranked movie in the Top 10 list."""

    __tablename__ = "movies"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    year: Mapped[int] = mapped_column(Integer, nullable=True)
    description: Mapped[str] = mapped_column(String(500), nullable=True)
    rating: Mapped[float] = mapped_column(Float, nullable=True)
    ranking: Mapped[int] = mapped_column(Integer, nullable=True)
    review: Mapped[str] = mapped_column(String(250), nullable=True)
    img_url: Mapped[str] = mapped_column(String(500), nullable=True)
