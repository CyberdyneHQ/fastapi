from typing import Annotated

from fastapi import Body, FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

app = FastAPI()


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    body = await request.body()
    detail = {"errors": exc.errors(), "body": body.decode()}
    return JSONResponse(status_code=422, content={"detail": detail})


@app.post("/")
async def sum_numbers(numbers: Annotated[list[int], Body()]):
    return sum(numbers)
