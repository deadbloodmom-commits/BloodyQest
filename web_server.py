from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles


app = FastAPI()


BASE_DIR = Path(__file__).resolve().parent
WEB_DIR = BASE_DIR / "webapp"


# Статические файлы Mini App:
# style.css, app.js и другие файлы
app.mount(
    "/static",
    StaticFiles(directory=WEB_DIR),
    name="static",
)


@app.get("/")
async def index():
    return FileResponse(
        WEB_DIR / "index.html"
    )
