from configuration_layer.settings import Settings
from motor.motor_asyncio import AsyncIOMotorClient

#DB set-up
settings = Settings()

client = AsyncIOMotorClient(settings.MONGO_DETAILS)
database = client[settings.DATABASE_NAME]
user_collection = database.get_collection(settings.COLLECTION_NAME)


async def create_user(user_data: dict, existing_user: dict | None = None, update: bool = False):
    if not update:
        user_data = await user_collection.insert_one(user_data)
        user_data = await get_user(user_data)
    else:
        filter_query = {"_id": existing_user["_id"]}
        update_payload = user_data.copy()
        update_payload.pop("_id", None)
        update_action = {"$set": update_payload}
        user_data = await user_collection.update_one(filter_query, update_action)
        user_data = await get_user(user_data, existing_user, update=True)

    return user_data


async def get_user(user_data, existing_user: dict | None = None, update: bool = False):
    if not update:
        user_data = await user_collection.find_one({"_id": user_data.inserted_id})
    else:
        user_data = await user_collection.find_one({"_id": existing_user["_id"]})
    return user_data


async def get_user_by_id(user_id: int):
    user_data = await user_collection.find_one({"user_id": user_id})
    return user_data
