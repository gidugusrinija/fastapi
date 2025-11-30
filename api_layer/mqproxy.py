from fastapi import FastAPI
from validation_models import UserIn
from service_layer.insert_valid_user import (insert_valid_user,
                                             get_user_data_by_id)
import uvicorn
from utils.user_output_helper import user_helper

from fastapi.responses import JSONResponse


app = FastAPI()


@app.get("/")
def welcome():
    return {"message": "Welcome to the API Layer"}


@app.get("/get/user/{user_id}/orders")
async def get_user_orders(user_id: int, limit: int | None = None):
    user_data = await get_user_data_by_id(user_id=user_id)
    response_data = user_helper(user_data).get("orders", [])
    if limit:
        response_data = response_data[:limit]
    return JSONResponse(response_data)


@app.get("/users/{user_id}")
async def get_users(user_id: int):
    user_data = await get_user_data_by_id(user_id=user_id)
    response_data = user_helper(user_data)
    return JSONResponse(response_data)


@app.post("/save/user/data")
async def save_user_data(payload: UserIn):
    user_data = payload.model_dump()
    new_user = await insert_valid_user(user_data)
    json_response = {"message": "User data saved successfully",
                     "metadata": user_helper(new_user)}
    return JSONResponse(json_response)


# uncomment below for local debugging
# if __name__ == "__main__":
#     uvicorn.run(app, host="0.0.0.0", port=18005)
