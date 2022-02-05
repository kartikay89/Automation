# making the code parallel.
import queue
import threading
import web_automation




# queue function used for opening multiple browsers.
def browser_queue():
    """
    This function is used to queue the browsers.
    """
    # Initialize the queue
    q = queue.Queue()
    # add the browsers to the queue
    q.put(web_automation.launchBrowser())
    
    # get the items from the queue
    q = q.get()
    return q
   
    


# initiate workers
def workers(q):
    """
    This function is used to initiate the workers that will start browsers in parallel.
    """
    
    
    print(f'Starting {q}')
    
    # create a list to join threads
    threads = list()
    
    while not q.empty():
    # initialize the worker with a number
        for thread_range in range(2):
            worker = threading.Thread(target=browser_queue, daemon=True, args=(thread_range,))     
            # put all threads in a list to join them.
            threads.append(worker)
            # start the worker
            worker.start()
            
        for index, thread in enumerate(threads):
            print(f"Main: before joining thread {index}")
            thread.join()
            print(f"Main: thread {index} done")
        
        print(f'Finishing {q}')
        
    
    # return 


# main function 
if __name__=='__main__':
    
    # getting the queue
    q = browser_queue()
    
    # initializing workers with queues
    workers(q)
    
    