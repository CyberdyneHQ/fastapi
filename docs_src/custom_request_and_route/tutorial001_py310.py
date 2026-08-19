import gzip
import json

from fastapi import FastAPI, Request

app = FastAPI()


@app.post("/sum")
async def sum_numbers(request: Request):
    body = await request.body()
    if "gzip" in request.headers.getlist("Content-Encoding"):
        body = gzip.decompress(body)
    numbers = json.loads(body)
    return {"sum": sum(numbers)}
