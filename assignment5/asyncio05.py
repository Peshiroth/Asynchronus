from random import random
import asyncio

# coroutine to execute in a new task
async def task_coro(food):
    # generate a random value between 0 and 1
    value = 1+random()
    print(f'>Microwave {food}: Cooking  {value} s')
    # block for a moment
    await asyncio.sleep(value)
    # report the value
    return food,value

# main coroutine
async def main():
    # create many tasks
    food_items = ["rice", "noodle", "curry"]
    tasks = [asyncio.create_task(task_coro(food)) for food in food_items]

    # wait for the first task to complete
    done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)

    # wait for all remaining tasks to complete and print their times
    # for task in pending:
    #     food, time = await task
    # get the first task to complete
    first = done.pop()
    first_food, first_time = await first
    print(f'\nFirst completed: {first_food}, took {first_time:.2f} seconds')

# start the asyncio program
asyncio.run(main())