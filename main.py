# Pydantic 示例

from enum import Enum

from fastapi import FastAPI

app = FastAPI()


@app.get("/user/me")
async def read_user_me():
    return {"user_id": "the current user"}


@app.get("/user/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}


# Enum 示例


class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


app = FastAPI()


@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the image"}

    return {"model_name": model_name, "message": "Have some residuals"}
