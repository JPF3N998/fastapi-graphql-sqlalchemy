import strawberry
from strawberry.fastapi import GraphQLRouter

from app.pokemon.schema.schema import Query

schema = strawberry.Schema(query=Query)

pokemon_router = GraphQLRouter(schema=schema)
