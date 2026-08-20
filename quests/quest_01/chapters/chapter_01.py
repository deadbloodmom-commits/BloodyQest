# quests/quest_01/chapters/chapter_01.py


CHAPTER_ID = "chapter_01"

CHAPTER_NUMBER = 1

CHAPTER_TITLE = "Начало"


def get_chapter_start_text(player_name: str) -> str:
    return (
        "<b>🕯 ГЛАВА I — НАЧАЛО</b>\n\n"
        f"<i>{player_name}, история начинается.</i>\n\n"
        "Ты ещё не знаешь, что именно привело тебя сюда.\n"
        "Но очень скоро тебе придётся это выяснить.\n\n"
        "<i>Некоторые истории начинаются задолго "
        "до того момента, когда мы понимаем, "
        "что уже стали их частью.</i>"
    )