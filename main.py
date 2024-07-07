from fastapi import FastAPI

from fastapi.responses import FileResponse

app = FastAPI()


# "/" is the default URL
@app.get("/")
def hello_world() -> dict:
    return {"message": "OK"}


# "/dog"
@app.get("/dog")
def bye_bye() -> dict:
    return {"message": "bitch"}


@app.get("/foo")
def foo() -> dict:
    return {"message": "Too foo for you!"}


@app.get("/avif")
async def read_avif_file() -> FileResponse:
    file_path = "pics/image.avif"
    media_type = "image/avif"
    return FileResponse(file_path, media_type=media_type)


@app.get("/png")
async def read_png_file() -> FileResponse:
    file_path = "pics/image.png"
    media_type = "image/png"
    return FileResponse(file_path, media_type=media_type)


@app.get("/links")
async def read_links_file() -> FileResponse:
    file_path = "html/fastapi-links.html"
    media_type = "text/html"
    return FileResponse(file_path, media_type=media_type)
