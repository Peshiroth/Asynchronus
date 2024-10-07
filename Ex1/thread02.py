# running a function with arguments in another thread
from time import sleep,ctime
from threading import Thread

#a custom function blocks from a moment
def task(sleep_time,massage):
    #block from a moment
    sleep(sleep_time)
    #display a massage
    print(f'{ctime(1)} {massage}')

#create a thread
thread = Thread(target=task,args=(1.5,'new massage from another thread'))
#run this thread
thread.start()
#wait for a thread to finish
print(f'{ctime()} Waiting for thread...')
thread.join()