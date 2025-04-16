from fastapi import FastAPI
from routes.items import router as items_router
from routes.analytics import router as analytics_router
from routes.quiz import router as quiz_router
from routes.users import router as users_router

app = FastAPI()

app.include_router(items_router, prefix="/items")
app.include_router(analytics_router)
# Change 1: Added prefix to quiz router (Issue 15)
# FROM: app.include_router(quiz_router)
# TO: app.include_router(quiz_router, prefix="/quiz")
app.include_router(quiz_router, prefix="/quiz")
app.include_router(users_router, prefix="/users")

# Change 2: Removed unnecessary /home endpoint (Issue 30)
# FROM: 
# @app.get("/home")
# async def get_home():
#     return {"message": "Welcome to the Multi-Page FastAPI App!"}
# TO: Removed as index.html is static
