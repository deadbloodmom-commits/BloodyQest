import asyncpg
from config import DATABASE_URL

async def init_db():
    conn = await asyncpg.connect(DATABASE_URL)
    
    # Таблица пользователей и их анкет
    await conn.execute("""
        CREATE TABLE IF NOT EXISTS users (
            user_id BIGINT PRIMARY KEY,
            name TEXT,
            gender TEXT,
            appearance TEXT,
            personality TEXT,
            photo_id TEXT,
            sound_enabled INTEGER DEFAULT 1
        )
    """)
    
    # Таблица прогресса по квестам
    await conn.execute("""
        CREATE TABLE IF NOT EXISTS user_progress (
            user_id BIGINT,
            quest_id INTEGER,
            chapter_id INTEGER,
            is_completed INTEGER DEFAULT 0,
            PRIMARY KEY (user_id, quest_id, chapter_id)
        )
    """)
    
    await conn.close()

async def get_user(user_id):
    conn = await asyncpg.connect(DATABASE_URL)
    user = await conn.fetchrow(
        "SELECT name, gender, appearance, personality, photo_id, sound_enabled FROM users WHERE user_id = $1",
        user_id
    )
    await conn.close()
    return user

async def save_user_profile(user_id, name, gender, appearance, personality, photo_id):
    conn = await asyncpg.connect(DATABASE_URL)
    await conn.execute("""
        INSERT INTO users (user_id, name, gender, appearance, personality, photo_id)
        VALUES ($1, $2, $3, $4, $5, $6)
        ON CONFLICT (user_id) DO UPDATE SET
            name = EXCLUDED.name,
            gender = EXCLUDED.gender,
            appearance = EXCLUDED.appearance,
            personality = EXCLUDED.personality,
            photo_id = EXCLUDED.photo_id
    """, user_id, name, gender, appearance, personality, photo_id)
    await conn.close()

async def update_sound_setting(user_id, sound_enabled):
    conn = await asyncpg.connect(DATABASE_URL)
    await conn.execute(
        "UPDATE users SET sound_enabled = $1 WHERE user_id = $2",
        sound_enabled, user_id
    )
    await conn.close()