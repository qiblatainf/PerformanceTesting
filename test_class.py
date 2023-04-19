import warnings
from memory_profiler import profile, memory_usage
from line_profiler import LineProfiler
import queue
import threading
import time
import yappi
from numpy import random
from Speech import Speech_Test, Speech_Libraries
# from scalene import scalene_profiler

# area = "speech"
# stream = "multi thread"
# test_string= "small"
# module_name = "better_profanity"
# requests = 5 #N-samples
class TestingComponent:
    # start = time.time()
    # exitFlag = 0
    # queueLock 
    # yappi.set_clock_type("CPU") #can be wall clock as well
    # warnings.filterwarnings("ignore")
    # queueLock = threading.Lock()
    def __init__(self, area, stream, test_string, module_name, requests):
        self.area= area
        self.stream = stream
        self.test_string = test_string
        self.module_name = module_name
        self.requests = requests

        
    
    def process_data(self, threadName, q, test_string, module_name, area, delay):
        while not self.exitFlag:
            self.queueLock.acquire()
            if not workQueue.empty():
                data = q.get()
                print("%s processing %s on module %s" % (threadName, data, module_name))
                
                if (area == "speech"):
                    Speech_Libraries(module_name, test_string)

                self.queueLock.release()   
            else:
                self.queueLock.release()
            time.sleep(delay)
            
    def set_exitFlag(value):
        exitFlag = value
    
    def get_exitFlag():
        return exitFlag
    
    def run(self):        
        start = time.time()
        # exitFlag = 0
        set_exitFlag(0)
        yappi.set_clock_type("CPU") #can be wall clock as well
        warnings.filterwarnings("ignore")

        #4 threads
        if (self.stream == "multi stream"):
            threadList = ["Thread-1", "Thread-2", "Thread-3", "Thread-4"]
        elif (self.stream == "single stream"):
            threadList = ["Thread-1"]
        elif (self.stream == "server"):
            threadList = ["Thread-1", "Thread-2", "Thread-3", "Thread-4"]
            self.requests = self.requests * 2

        if (self.stream == "single stream" or self.stream == "multi stream" or self.stream == "server"):
            #change to 1024 later
            nameList = [self.test_string] * self.requests
            queueLock = threading.Lock()

            #queue size will be 1024
            workQueue = queue.Queue(self.requests)
            threads = []
            threadID = 1

            # scalene_profiler.start()
            yappi.start()

            # Create new threads
            for tName in threadList:
                thread = myThread(threadID, tName, workQueue, self.test_string, self.module_name, self.area, self.stream, self.requests)
                thread.start()
                threads.append(thread)
                threadID += 1

            # Fill the queue
            queueLock.acquire()
            for word in nameList:
                workQueue.put(word)
            queueLock.release()

            # Wait for queue to empty
            while not workQueue.empty():
                pass

            # Notify threads it's time to exit
            exitFlag = 1

            # Wait for all threads to complete
            for t in threads:
                t.join()
            print("Exiting Main Thread")

            yappi.stop()
        
        if (stream == "offline"):
            yappi.start()
            if (area == "speech"):            
                for i in range(requests):
                    test_string = Speech_Test(module_name, test_string)
                    Speech_Libraries(module_name, test_string)
            yappi.stop()  
            
        stop = time.time()

        print("")
        print("CPU Usage:")
        yappi.get_thread_stats().print_all()

        print("")
        print("Time Consumed (Latency): {} secs".format(stop - start))

class myThread (TestingComponent, threading.Thread):
        def __init__(self, threadID, name, q, test_string, module_name, area, stream, requests):
            TestingComponent.__init__(self, area, stream, test_string, module_name, requests)
            threading.Thread.__init__(self)
            self.threadID = threadID
            self.name = name
            self.q = q
            self.test_string = test_string
            self.module_name = module_name
            self.area = area
            self.stream = stream
            
            # self.__exitFlag = 0
        
        def run(self):
            print("Starting " + self.name)
            
            #Conditions for all areas
            if (self.area == "speech"):
                self.test_string = Speech_Test(self.module_name, self.test_string)
                
            #Setting Timer Delay
            if (self.stream == "multi stream"):
                delay = 5
            if (self.stream == "server"):
                delay = random.poisson(lam=2, size=1)[0]
            else:
                delay = 1
            
            TestingComponent.process_data(self, self.name, self.q, self.test_string, self.module_name, self.area, delay)
            print("Exiting " + self.name)



# testing_component("speech", "server", "small", "better_profanity", 5 )

#area, stream, test_string, module_name, requests
t1 = TestingComponent("speech", "server", "small", "better_profanity", 5) 
t1.run()