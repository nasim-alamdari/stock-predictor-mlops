""" To see results do the following steps:
 - in terminal run: uvicorn main:app --reload --workers 1 --host 0.0.0.0 --port 8000
 - Navigate to following link in your browser: http://localhost:8000/ping
 
 
Below is the explanation of the command:
--reload: enables auto-reload so the server will restart after changes are made to the code base.
--workers 1: provides a single worker process.
--host 0.0.0.0 :defines the address to host the server on.
--port 8000: defines the port to host the server on.
--main:app :tells uvicorn where it can find the FastAPI ASGI application. In this case, within the main.py file, you will find the ASGI app app = FastAPI().

"""
from fastapi import FastAPI
app = FastAPI()

@app.get("/ping")
def pong():
    return {"ping": "pong!"}