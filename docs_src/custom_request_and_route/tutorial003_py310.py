import time

from fastapi import FastAPI, Request

app = FastAPI()


@app.middleware("http")
async def add_response_time_header(request: Request, call_next):
    before = time.time()
    response = await call_next(request)
    if request.url.path == "/timed":
        duration = time.time() - before
        response.headers["X-Response-Time"] = str(duration)
    return response


@app.get("/")
async def not_timed():
    return {"message": "Not timed"}


@app.get("/timed")
async def timed():
    return {"message": "It's the time of my life"}
