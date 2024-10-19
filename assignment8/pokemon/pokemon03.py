from pypokemon.pokemon import Pokemon
import asyncio
import httpx
import time
import random

#async def get_pokemon(client, url):
    #print(f'{time.ctime()} - get {url}')
    #resp = await client.get(url)
    #pokemon = resp.json()

    #return Pokemon(pokemon)

#async def get_pokemons():
    #async with httpx.AsyncClient() as client:
        #tasks = []
        #rand_list = []
        #for i in range(5):
            #rand_list.append(random.randint(1,151))
        #for number in rand_list:
            #url = f'https://pokeapi.co/api/v2/pokemon/{number}'
            #tasks.append(asyncio.create_task(get_pokemon(client,url)))
        #pokemons = await asyncio.gather(*tasks)
        #return pokemons
#async def index():
    #start_time = time.perf_counter()
    #pokemons = await get_pokemons()
    #end_time = time.perf_counter()
    #print(f"{time.ctime()} - Asynchronous get {len(pokemons)} pokemons. Time taken: {end_time-start_time} seconds")

#if __name__ == '__main__':
   #asyncio.run(index())

from httpx import AsyncClient
import asyncio
import time

async def fetch_ability_data(url):
  """
  Fetches data from the provided URL and returns a dictionary containing name and url keys.

  Args:
      url (str): The URL to fetch data from.

  Returns:
      dict: A dictionary containing 'name' and 'url' keys, or None on error.
  """
  print(f"{time.ctime()} - Fetching ability data from: {url}")
  async with AsyncClient() as client:
    try:
      response = await client.get(url)
      response.raise_for_status()  # Raise an exception for non-200 status codes
      data = response.json()
      return {"name": data["name"], "url": data["url"]}
    except httpx.HTTPStatusError as e:
      print(f"Error fetching data: {e}")
      return None

async def main():
  """
  Fetches data for the "battle-armor" ability and prints the name and URL.
  """
  ability_url = "https://pokeapi.co/api/v2/ability/battle-armor"
  ability_data = await fetch_ability_data(ability_url)

  if ability_data:
    print(f"Ability Name: {ability_data['name']}")
    print(f"Ability URL: {ability_data['url']}")
  else:
    print("Failed to fetch ability data.")

if __name__ == "__main__":
  asyncio.run(main())
