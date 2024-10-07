import time

judit_compute_time = 0.1
opponent_compute_time = 0.5
move_pairs = 30
opponents = 3

def game(x):
    start_board_time = time.perf_counter()
    for i in range(move_pairs):
        time.sleep(judit_compute_time)
        print(f"Board {x+1} {i+1} Judit made a move")
        print("Opponent Turn")
        time.sleep(opponent_compute_time)
        print(f"Board {x+1} {i+1} Opponents made a move")
    print(f'Board-{x+1}- >>>>>>>>>>> Finished - in{round(time.perf_counter()) - start_board_time} secs\n')
    return round(time.perf_counter() - start_board_time)
if __name__ == "__main__":
    start_time = time.perf_counter
    board_time = 0
    for Board in range(opponents):
        board_time == game(Board)
    print(f'Board exhibition finished in {board_time} secs.')
    print(f'finished in{round(time.perf_counter() - start_time)} secs')