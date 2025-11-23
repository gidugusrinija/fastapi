
def user_helper(user_data) -> dict:
    return {
        "id": str(user_data["_id"]),
        "name": user_data["name"],
        "age": user_data["age"],
        "email": user_data["email"],
    }
