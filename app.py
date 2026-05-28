import os

from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.responses import FileResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles

from utils import send_message

load_dotenv()
### Email ######
PORT_EMAIL:str = os.getenv("PORT_EMAIL")
SMTP_SERVER:str = os.getenv('SMTP_SERVER')
SENDER_EMAIL:str = os.getenv('SENDER_EMAIL')
RECEIVER_EMAIL:str = os.getenv('RECEIVER_EMAIL')
PASSWORD:str = os.getenv('PASSWORD')

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
def index():
    return FileResponse("static/index.html")

@app.get("/notified")
def notified():
    return FileResponse("static/notified.html")

@app.post("/notify")
def notify():
    send_message(
        port=PORT_EMAIL,
        sender_email=SENDER_EMAIL,
        receiver_email=RECEIVER_EMAIL,
        password=PASSWORD,
        smtp_server=SMTP_SERVER,
    )
    return RedirectResponse(url="/notified", status_code=303)


