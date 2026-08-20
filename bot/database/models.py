from datetime import datetime

from sqlalchemy import (
    BigInteger,
    Boolean,
    DateTime,
    String,
    Text,
)
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True,
    )

    telegram_id: Mapped[int] = mapped_column(
        BigInteger,
        unique=True,
        nullable=False,
        index=True,
    )

    username: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True,
    )

    name: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True,
    )

    pronouns: Mapped[str | None] = mapped_column(
        String(50),
        nullable=True,
    )

    appearance: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    personality: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    # 📷 Фото профиля Telegram
    photo_file_id: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True,
    )

    sound_enabled: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
    )

    music_enabled: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
    )

    notifications_enabled: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
    )