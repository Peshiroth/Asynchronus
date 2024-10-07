import aiofiles
import asyncio
import json

pokemonapi_directory = 'asyncioclass67_6510301044/assignment07/pokemon/pokemonapi'
pokemonmove_directory = 'asyncioclass67_6510301044/assignment07/pokemon/pokemonmove'

async def main():
    #Read the contents of the json file.
    async with aiofiles.open(f'{pokemonapi_directory}/articuno.json',mode='r') as f:
        contents = await f.read()
    
    pokemon = json.loads(contents)
    print(pokemon['name'])


asyncio.run(main())