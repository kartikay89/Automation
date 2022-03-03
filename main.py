# making the code parallel.
import queue
import threading
# import web_automation
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium import webdriver
import time




def launchBrowser(*url):
	"""
    function to launch the browsers.
    """
	driver = webdriver.Chrome(r"/Users/kartikaysingh/Desktop/Projects/Code_snippets/chromedriver")
	# opening the browser urls
	driver.get(url)
	print(driver.title)
	time.sleep(5)
	return driver



# queue function used for opening multiple browsers.
def browser_queue():
    """
    This function is used to queue the browsers.
    """
    # browser url
    browser_url = ["https://webfront.payu.in/webfront/#/payment/webfrontpage/strawesome-quencher/single/455"] * 3
    print(browser_url)
    # Initialize the queue
    q = queue.Queue()
    # multipling the items
    input_browser = browser_url
    
    # add the browsers to the queue
    for urls in input_browser:
        q.put(urls)
    print(q.qsize())
    
    return q


# initiate workers
def workers(q):
    """
    This function is used to initiate the workers that will start browsers in parallel.
    """
    # get the items from the queue
    q = q.get()
    
    print(f'Starting {q}')
    
    # create a list to join threads
    threads = list()
    
    
    # initialize the worker with a number
    for thread_range in range(3):
        worker = threading.Thread(target=launchBrowser, daemon=True, args=( thread_range,))     
        # put all threads in a list to join them.
        threads.append(worker)
        # start the worker
        worker.start()
        
    for index, thread in enumerate(threads):
        print(f"Main: before joining thread {index}")
        thread.join()
        print(f"Main: thread {index} done")
    
    print(f'Finishing {q}')


# main function 
if __name__=='__main__':
    
    # getting the queue
    q = browser_queue()
    launchBrowser(q)
    
    # initializing workers with queues
    # workers(q)
    
    