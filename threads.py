import threading
import time
import random

def main():
    class myThread (threading.Thread):
        def __init__(self):
            threading.Thread.__init__(self)
        def run(self):
            start_time=time.time()
            time.sleep(random.randint(1,20))
            print time.time()-start_time

    threads = []
    for thread in xrange(10):
        threads.append(myThread())

    start = time.time()

    for t in threads:
        t.start()
    while (time.time()-start)<5:
        for t in threads:
            t.join(0.01)
            if not t.isAlive():
                print "done in 5"
        if not all(t.isAlive() for t in threads):
            print "breaking"
            break
    for t in threads:
        if t.isAlive():
            print "its alive"




if __name__=="__main__":
    main()
