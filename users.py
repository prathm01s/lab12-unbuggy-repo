from fastapi import APIRouter, HTTPException
from models import User
from bson import ObjectId

router = APIRouter()

async def get_users_collection():
    from db import init_db
    return init_db()["users_collection"]

# BUG: Incorrect HTTP method for fetching users (POST instead of GET)
# @router.post("/")
@router.get("/")  # FIX: Changed from POST to GET
async def get_users():
    collection = await get_users_collection()
    users = []
    async for user in collection.find():
        user["_id"] = str(user["_id"])
        users.append(user)
    return users
# sir i like all music
# BUG: Duplicate POST route for "/" (conflict with get_users)
@router.post("/")
async def create_user(user: User):
    collection = await get_users_collection()
    result = await collection.insert_one(user.dict())
    return {"id": str(result.inserted_id)}

# BUG: Invalid delete operation (delete_all() is not a valid MongoDB method)
# @router.delete("/{user_id}")
# async def delete_user(user_id: str):
#     result = await collection.delete_all()
@router.delete("/{user_id}")
async def delete_user(user_id: str):
    collection = await get_users_collection()
    # FIX: Use delete_one() with the user's ID
    result = await collection.delete_one({"_id": ObjectId(user_id)})
    if result.deleted_count:
        return {"status": "deleted"}
    raise HTTPException(status_code=404, detail="User not found")