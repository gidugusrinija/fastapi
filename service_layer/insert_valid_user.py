from data_access_layer.user_actions import (create_user, get_user,
                                            get_user_by_id)


async def insert_valid_user(user_data):
    user_data = await create_user(user_data)
    return user_data


async def get_user_data(user_data):
    user_data = await get_user(user_data)
    return user_data


async def get_user_data_by_id(user_id: int):
    user_data = await get_user_by_id(user_id=user_id)
    return user_data
