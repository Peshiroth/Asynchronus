# extending the Thread class
from time import sleep,ctime
from threading import Thread

#custom thread class
class CustomThread(Thread):
    #override the run function
    def run(self):
        #block for a moment
        sleep(1)
        #display a massage
        print(f'{ctime()} This is coming from another thread')

#create a thread
thread = CustomThread()
#start the thread
thread.start()
#wait for a thread to finish
print(f'{ctime()} Waiting for thread to finish')
thread.join()
#get the value returned
        