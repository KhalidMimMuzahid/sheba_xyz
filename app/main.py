from fastapi import FastAPI , Depends
from fastapi.middleware.cors import CORSMiddleware
from app.routes.router import router
from app.database import init_db
from app.exceptions.handler import register_all_errors
from app.dependencies.authenticate_user import authenticate_user

app = FastAPI()
@app.get("/")
async def root():
    return {"message": "Hello World"}

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://localhost:3000"],  # Replace with your frontend URL
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)

# # If you want to automatically initialize your DB on startup,
@app.on_event("startup")
async def on_startup():
    # This will run when the application starts and use the existing event loop.
    await init_db()




# we are redirecting all routes to routes to handle easily
app.include_router(router, prefix="/api/v1" , dependencies=[Depends(authenticate_user)])

register_all_errors(app)




