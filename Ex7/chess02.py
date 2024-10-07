import asyncio
import time

judit_compute_time = 0.1
opponent_compute_time = 0.5
move_pairs = 30
opponents = 24
start_time = time.perf_counter()
async def game(x):
    start_board_time = time.perf_counter()
    for i in range(move_pairs):
        time.sleep(judit_compute_time)
        print(f"Board {x+1} {i+1} Judit made a move")
        print("Opponent Turn")
        await asyncio.sleep(opponent_compute_time)
        print(f"Board {x+1} {i+1} Opponents made a move")
    print(f'Board-{x+1}- >>>>>>>>>>> Finished - in{round(time.perf_counter()) - start_board_time} secs\n')
    return round(time.perf_counter() - start_board_time)
async def async_io():
    tasks = []
    for i in range (opponents):
        tasks += [game(i)]
    await asyncio.gather(*tasks)
    print(f'Board exhibition finished in {round(time.perf_counter() - start_time)} secs.')
if __name__ == "__main__":
    start_game = time.perf_counter()
    asyncio.run(async_io())
    elapsed = time.perf_counter() - start_game
    print(f"{time.ctime()}  finish in ", elapsed, "seconds.")
