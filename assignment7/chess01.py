import time

my_computer_time = 0.1
opponent_computer_time = 0.5
oppenents = 3
move = 30

def game(x):
    board_start_time = time.perf_counter()
    for i in range(move):
        time.sleep(my_computer_time)
        print(f"{x+1} {i+1} Judit made a move")
        time.sleep(opponent_computer_time)
        print(f"{x+1} {i+1} oppenent made a move")
    print(f"Board - {x+1} >>>>>>>>> Finish move in {round(time.perf_counter() - board_start_time)}sec \n")
    return round(time.perf_counter() - board_start_time)


if __name__ == "__main__":
    start_time = time.perf_counter()
    board_time = 0
    for board in range(oppenents):
        board_time += game(board)
    print(f"Board exhibition finished in {board_time} sec.")
    print(f"Finish in {round(time.perf_counter() - start_time)} secs.")