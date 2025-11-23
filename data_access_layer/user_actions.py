from configuration_layer.settings import Settings
from motor.motor_asyncio import AsyncIOMotorClient

#DB set-up
settings = Settings()

client = AsyncIOMotorClient(settings.MONGO_DETAILS)
database = client[settings.DATABASE_NAME]
user_collection = database.get_collection(settings.COLLECTION_NAME)


async def create_user(user_data: dict):
    user_data = await user_collection.insert_one(user_data)
    user_data = await get_user(user_data)

    return user_data


async def get_user(user_data):
    user_data = await user_collection.find_one({"_id": user_data.inserted_id})
    return user_data

async def get_user_by_id(user_id: int):
    user_data = await user_collection.find_one({"user_id": user_id})
    return user_data

