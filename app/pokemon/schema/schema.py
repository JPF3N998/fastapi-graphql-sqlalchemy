import typing
import httpx
import strawberry

from app.constants.constants import POKE_API_BASE_URL


@strawberry.type
class Pokemon:
    id: int
    name: str
    types: list[str]
    height: int
    weight: int


@strawberry.type
class Query:
    @strawberry.field(description="Get a pokemon by id or name.")
    async def get_pokemon(self, id_or_name: str) -> typing.Optional[Pokemon]:
        """
        Get a pokemon by id or name from PokeAPI.
        Args:
            id_or_name (int | str): The id or name of the pokemon, parsedand used as strings.
        Returns:
            Pokemon | None: The pokemon data or None if not found.
        """
        # Input validation

        if not id_or_name or not isinstance(id_or_name, str) or not id_or_name.strip():
            raise ValueError("id_or_name must be a non-empty string.")

        async with httpx.AsyncClient() as client:
            # Make a GET request to the PokeAPI
            response = await client.get(f"{POKE_API_BASE_URL}{id_or_name}")

            # Check if the request was successful
            if response.status_code == 200:
                data = response.json()

                types = [t["type"]["name"] for t in data["types"]]

                return Pokemon(
                    id=data["id"],
                    name=data["name"],
                    types=types,
                    height=data["height"],
                    weight=data["weight"],
                )

            return None
