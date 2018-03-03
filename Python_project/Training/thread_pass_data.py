import threading
import time

data = 10
lock = threading.Lock()

def ThreadFunction(*args):
    global data
    print(threading.current_thread().getName())
    lock.acquire()
    data += 1
    time.sleep(1)
    print(args)
    print(data)
    lock.release()
    
def main():
    thread = []
    
    for i in range(5):
        t1 = threading.Thread(target=ThreadFunction,args=("Hello","Shyam",i), name = "Thread"+str(i))
        thread.append(t1)
        t1.start()
        
    for x in thread:
        x.join()        #wait until thread terminates
            
if __name__ == "__main__":
    main()