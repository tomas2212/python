import threading
import time

cv = threading.Condition()

counter = 0
shared = 0

class Producer(threading.Thread):
    def __init__(self, threadID, name):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name

    def run(self):
        global counter, shared, cv
        while(True):
             cv.acquire()
             if (shared == 0):
                 shared = 1
                 counter += 1
                 print "Producer produce %i , shared: %i" % (counter, shared)
                 cv.notifyAll()
             else:
                  cv.wait()
             cv.release()
        

class Consumer(threading.Thread):
    def __init__(self, threadID, name):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name

    def run(self):
        global shared, counter, cv
        while(True):
            cv.acquire()
            if(shared == 1):
                shared = 0
                print "%s consume %i item , shared: %i" % (self.name, counter, shared)
                cv.notifyAll()
            else:    
                cv.wait()
            cv.release()
   

threads = []

prod = Producer(1, "Producer")
cons1 = Consumer(1, "Consumer1")
cons2 = Consumer(2, "Consumer2")    
cons3 = Consumer(3, "Consumer3")

threads.append(prod)
threads.append(cons1)
threads.append(cons2)
threads.append(cons3)

prod.start()
cons1.start()
cons2.start()
cons3.start()

for t in threads:
    t.join()
print "Exiting main thread"
