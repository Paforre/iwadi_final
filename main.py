from fastapi import FastAPI
from  search import search_route
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

origins = [
    "*",
]
# Base Endpoint


@app.get("/")
def get_welcome():
    return {"message": "Bienvenue sur IWADI!"}


# Parcours Endpoint
app.include_router(search_route)
