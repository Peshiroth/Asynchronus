# Asynchronous breakfast
import asyncio
from time import sleep, time

async def make_coffee():
    print("coffee: prepare ingridients")
    sleep(1)
    print("coffee: waiting...")
    await asyncio.sleep(2)
    fry_eggs()
    print("coffee: ready")

def fry_eggs():
    print("eggs: prepare ingridients")
    sleep(1)
    print("eggs: frying...")
    sleep(3)
    print("eggs: ready")

async def main():
    start = time()
    await make_coffee()
    print(f"breakfast is ready in {time()-start} min")


asyncio.run(main())