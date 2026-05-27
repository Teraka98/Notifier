from fastapi import FastAPI
from fastapi.responses import FileResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from utils import send_message,generate_qr_code
from pyngrok import ngrok
import uvicorn
import os
from dotenv import load_dotenv

load_dotenv()
### Email ######
PORT_EMAIL= os.getenv("PORT_EMAIL")
SMTP_SERVER=os.getenv('SMTP_SERVER')
SENDER_EMAIL=os.getenv('SENDER_EMAIL')
RECEIVER_EMAIL=os.getenv('RECEIVER_EMAIL')
PASSWORD=os.getenv('PASSWORD')
### Ngrok ######
PORT_NGROK= os.getenv("PORT_NGROK")


app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
def index():
    return FileResponse("static/index.html")

@app.post("/notify")
def notify():
    send_message(
        port=PORT_EMAIL,
        sender_email=SENDER_EMAIL,
        receiver_email=RECEIVER_EMAIL,
        password=PASSWORD,
        smtp_server=SMTP_SERVER,
    )
    return RedirectResponse(url="/", status_code=303)

if __name__ == "__main__":
    tunnel = ngrok.connect(PORT_NGROK)
    generate_qr_code(link=tunnel.public_url)
    uvicorn.run(app, port=8000)

