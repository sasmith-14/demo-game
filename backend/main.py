from fastapi import FastAPI
from fastapi import WebSocket, WebSocketDisconnect

app = FastAPI()

@app.get("/")
def home():
    return {"message" : "server is running"}

@app.websocket("/ws")
async def socket_endpoint(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            data = await websocket.receive_text()
            await websocket.send_text(f"Echo: {data}")
    except WebSocketDisconnect:
        print("connection lost")

