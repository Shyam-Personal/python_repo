import threading

def worker():
    print("worker")
    
if __name__ == "__main__":
    t= threading.Thread(target=worker)
    t.start()
    
    threads = []
    
    for i in range(5):
        t = threading.Thread(target=worker)
        threads.append(t)
        t.start()
        
