from fastapi import FastAPI
from mongo_usage import get_repos, get_users
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from main import username_exists, insert_public_repos
app = FastAPI()

origins = [
    "http://localhost:3000",
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/v1/repos")
def repos(username: str, skip: int = 0, limit: int = -1):
    return JSONResponse(get_repos(username, skip, limit))


@app.get("/v1/users")
def repos():
    return JSONResponse(get_users())


@app.post("/v1/adduser")
def add_user(username):
    if username_exists(username):
        insert_public_repos(username)
