# check the type of a coroutine
import asyncio
#define a coroutine
async def custom_coro():
    #wait another coroutine
    await asyncio.sleep(1)
#create coroutine
coro = custom_coro()
#check the type of the coroutine
print(type(coro))
