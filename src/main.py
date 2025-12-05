from fastapi import FastAPI
from fastapi import Response
from fastapi.responses import PlainTextResponse
from fastapi.responses import JSONResponse
import os

if "SERVER_HELLO" not in os.environ:
    raise SystemExit("Error: SERVER_HELLO variable is not set")

app = FastAPI(docs_url=None, redoc_url=None, openapi_url=None)


@app.get("/health-check")
def health_check() -> Response:
 return JSONResponse(content={"status": "good"})


@app.get("/hello-world")
def hello_world() -> Response:
    return PlainTextResponse(content=os.getenv("SERVER_HELLO"))
