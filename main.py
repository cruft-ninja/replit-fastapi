from fastapi import FastAPI

from fastapi.responses import FileResponse

# Initialize the FastAPI app
app = FastAPI()

# Route for the root URL ("/")
@app.get("/")
def hello_world() -> dict:
    """
    This route handles GET requests to the root URL ("/").
    It returns a simple JSON message with a status message "OK".
    """
    return {"message": "OK"}

# Route for "/dog"
@app.get("/dog")
def bye_bye() -> dict:
    """
    This route handles GET requests to the URL "/dog".
    It returns a JSON message with the content "bitch".
    """
    return {"message": "bitch"}

# Route for "/foo"
@app.get("/foo")
def foo() -> dict:
    """
    This route handles GET requests to the URL "/foo".
    It returns a humorous JSON message "Too foo for you lulu!"
    """
    return {"message": "Too foo for you lulu!"}

# Route for "/avif"
@app.get("/avif")
async def read_avif_file() -> FileResponse:
    """
    This route handles GET requests to the URL "/avif".
    It serves an AVIF image file located at "pics/image.avif".
    """
    file_path = "pics/image.avif"           # Define the file path for the AVIF image
    media_type = "image/avif"               # Specify the media type for the response
    return FileResponse(file_path, media_type=media_type)

# Route for "/png"
@app.get("/png")
async def read_png_file() -> FileResponse:
    """
    This route handles GET requests to the URL "/png".
    It serves a PNG image file located at "pics/image.png".
    """
    file_path = "pics/image.png"           # Define the file path for the PNG image
    media_type = "image/png"               # Specify the media type for the response
    return FileResponse(file_path, media_type=media_type)

# Route for "/links"
@app.get("/links")
async def read_links_file() -> FileResponse:
    """
    This route handles GET requests to the URL "/links".
    It serves an HTML file located at "html/fastapi-links.html".
    """
    file_path = "html/fastapi-links.html"  # Define the file path for the HTML file
    media_type = "text/html"               # Specify the media type for the response
    return FileResponse(file_path, media_type=media_type)