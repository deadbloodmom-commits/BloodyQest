from sqlalchemy import select

from bot.database.database import SessionLocal
from bot.database.models import User


async def get_or_create_user(telegram_user):
    async with SessionLocal() as session:

        result = await session.execute(
            select(User).where(
                User.telegram_id == telegram_user.id
            )
        )

        user = result.scalar_one_or_none()

        if user:
            return user

        user = User(
            telegram_id=telegram_user.id,
            username=telegram_user.username,
        )

        session.add(user)

        await session.commit()
        await session.refresh(user)

        return user


async def get_user(telegram_id: int):
    async with SessionLocal() as session:

        result = await session.execute(
            select(User).where(
                User.telegram_id == telegram_id
            )
        )

        return result.scalar_one_or_none()