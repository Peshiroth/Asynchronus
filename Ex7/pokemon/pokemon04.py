import os
import aiofiles
import asyncio
import json
from pathlib import Path

pokemonapi_directory = 'asyncioclass67_6510301044/assignment07/pokemon/pokemonapi'
pokemonmove_directory = 'asyncioclass67_6510301044/assignment07/pokemon/pokemonmove'

async def process_file(filename):
    async with aiofiles.open(os.path.join(pokemonapi_directory, filename), mode='r') as f:
        contents = await f.read()

    pokemon = json.loads(contents)
    name = pokemon['name']
    moves = [move['move']['name'] for move in pokemon['moves']]

    async with aiofiles.open(os.path.join(pokemonmove_directory, f'{name}_moves.txt'), mode='w') as f:
        await f.write('\n'.join(moves))

async def main():
    files = [f for f in os.listdir(pokemonapi_directory) if f.endswith('.json')]
    tasks = [process_file(file) for file in files]
    await asyncio.gather(*tasks)

asyncio.run(main())