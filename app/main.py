from typing import Union
from fastapi import FastAPI

from app.pokemon.router import pokemon_router

app = FastAPI()

app.include_router(
    router=pokemon_router,
    prefix="/graphql",
)


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
