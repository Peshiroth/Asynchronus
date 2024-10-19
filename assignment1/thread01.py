# running a function in another thread
from time import sleep,ctime
from threading import Thread

#a custom function blocks from a moment
def task():
    #block from a moment
    sleep(1)
    #display a massage
    print(f'{ctime(1)} This is from another thread')

#create a thread
thread = Thread(target=task)
#run this thread
thread.start()
#wait for a threadto finish
print(f'{ctime()} Waiting for thread...')
thread.join()