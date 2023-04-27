import warnings
from memory_profiler import profile, memory_usage
from line_profiler import LineProfiler
import queue
import threading
import time
import yappi
from numpy import random
# from Speech import Speech_Test, Speech_Libraries
from Speech.SpeechLibraries import SpeechLibrary
from Speech.SpeechTestData import SpeechData
from PerformanceMetrics.ProfaneAccuracy import ProfaneAccuracy
# from scalene import scalene_profiler

# area = "speech"
# stream = "multi thread"
# test_string= "small"
# module_name = "better_profanity"
# requests = 5 #N-samples

def testing_component(area, stream, test_string, module_name, requests):
    start = time.time()
    exitFlag = 0
    yappi.set_clock_type("CPU") #can be wall clock as well
    warnings.filterwarnings("ignore")
    
    class myThread (threading.Thread):
        def __init__(self, threadID, name, q, test_string, module_name, area):
            threading.Thread.__init__(self)
            self.threadID = threadID
            self.name = name
            self.q = q
            self.test_string = test_string
            self.module_name = module_name
            self.area = area
        
        def run(self):
            print("Starting " + self.name)
            # print("Test string: " + self.test_string)
            
            #Conditions for all areas
            if (area == "speech"):
                # self.test_string = Speech_Test(module_name, test_string)
                self.test_string = SpeechData(module_name, self.test_string).test_data()
                
            # print("Test string now: " + self.test_string)
            #Setting Timer Delay
            if (stream == "multi stream"):
                delay = 5
            if (stream == "server"):
                delay = random.poisson(lam=2, size=1)[0]
            else:
                delay = 1
            
            process_data(self.name, self.q, self.test_string, self.module_name, self.area, delay)
            print("Exiting " + self.name)

    def process_data(threadName, q, test_string, module_name, area, delay):
        while not exitFlag:
            queueLock.acquire()
            if not workQueue.empty():
                data = q.get()
                print("%s processing %s on module %s" % (threadName, data, module_name))
                
                if (area == "speech"):
                    # Speech_Libraries(module_name, test_string)
                    SpeechLibrary(module_name, test_string).lib()
                    
                    # print(test_string)
                    # print(SpeechLibrary(module_name, test_string).lib())

                queueLock.release()   
            else:
                queueLock.release()
            time.sleep(delay)

    #4 threads
    if (stream == "multi stream"):
        threadList = ["Thread-1", "Thread-2", "Thread-3", "Thread-4"]
    elif (stream == "single stream"):
        threadList = ["Thread-1"]
    elif (stream == "server"):
        threadList = ["Thread-1", "Thread-2", "Thread-3", "Thread-4"]
        requests = requests * 2

    if (stream == "single stream" or stream == "multi stream" or stream == "server"):
        #change to 1024 later
        nameList = [test_string] * requests
        queueLock = threading.Lock()

        #queue size will be 1024
        workQueue = queue.Queue(requests)
        threads = []
        threadID = 1

        # scalene_profiler.start()
        yappi.start()

        # Create new threads
        for tName in threadList:
            thread = myThread(threadID, tName, workQueue, test_string, module_name, area)
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


# testing_component("speech", "server", "small", "better_profanity", 5 )

class TestingComponent(object):
        
    def __init__(self, area, stream, test_string, module_name, requests):
        self.area= area
        self.stream = stream
        self.test_string = test_string
        self.module_name = module_name
        self.requests = requests
    
    def utilization(self):
        myfunc = testing_component(self.area, self.stream, self.test_string, self.module_name, self.requests)
        
    def performance_metrics(self):        
        if ("prof" in self.module_name):
            return ProfaneAccuracy(self.module_name).accuracy()

t1 = TestingComponent("speech", "single stream", "large", "better_profanity", 1) 
t1.utilization()
print(t1.performance_metrics())