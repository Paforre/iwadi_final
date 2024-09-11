from fastapi import FastAPI
from  search import search_route

app = FastAPI()


# Base Endpoint


@app.get("/")
def get_welcome():
    return {"message": "Bienvenue sur IWADI!"}


# Parcours Endpoint
app.include_router(search_route)
