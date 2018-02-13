import time

class StopWatch(object):
    def __init__(self):
        # Note that this is exactly the same as self.start().
        # So, you can also just call self.start() here.
        self.start_time = time.time()
        self.end_time = -1

    def start(self):
        self.start_time = time.time()
        self.end_time = -1

    def stop(self):
        self.end_time = time.time()

    def elapsed_time(self):
        if not self.end_time == -1:
            return round((self.end_time - self.start_time)*1000)

##
import time
class StopWatch():

    def __init__(self, start_time = time.time(), end_time = -1):
        self.start_time = start_time
        self.end_time = end_time
        
    def start(self):
        self.start_time = time.time()
        self.end_time = -1
        
    def stop(self):
        self.end_time = time.time()
        
    def elapsed_time(self):
        if self.end_time==-1:
            return None
        elapsed_time = time.time() - self.start_time
        return round(float(elapsed_time),1)
        
        
        
        
sw = StopWatch() 
time.sleep(1) 
sw.stop() 
print sw.elapsed_time() 
sw.start() 
time.sleep(0.2) 
print sw.elapsed_time() 
sw.stop() 
print sw.elapsed_time()