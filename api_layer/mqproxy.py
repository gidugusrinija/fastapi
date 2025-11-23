from fastapi import FastAPI
from validation_models import Payload, UserIn
from service_layer.insert_valid_user import insert_valid_user, get_user_data, \
    get_user_by_id, get_user_data_by_id
import uvicorn
from utils.user_output_helper import user_helper


app = FastAPI()


@app.get("/")
def welcome():
    return {"message": "Welcome to the API Layer"}


@app.get("/users/{user_id}")
async def get_users(user_id: int):
    user_data = await get_user_data_by_id(user_id=user_id)
    response_data = user_helper(user_data)
    return response_data


@app.post("/save/user/data")
async def save_user_data(payload: UserIn):
    user_data = payload.model_dump()
    new_user = await insert_valid_user(user_data)
    return user_helper(new_user)


# uncomment below for local debugging
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=18005)
