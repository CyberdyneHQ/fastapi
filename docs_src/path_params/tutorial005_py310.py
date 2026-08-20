from fastapi import FastAPI

app = FastAPI()


@app.get("/models/{model_name}")
async def get_model(model_name: str):
    if model_name == "alexnet":
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}
