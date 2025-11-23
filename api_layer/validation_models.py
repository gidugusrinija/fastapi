from pydantic import BaseModel


class Payload(BaseModel):
    data: dict
    user_id: int


class UserIn(BaseModel):
    user_id: int
    name: str
    age: int
    email: str


# Pydantic Model for data retrieved from DB (Response Body)
# Note: MongoDB documents have an '_id' field, which is often returned as a string.
class UserOut(UserIn):
    id: str
