from threading import Thread, Lock
import time
import requests
from queue import Queue, Empty
## multithreading   

thread_visits = 0

thread_lock = Lock()
def myfunction()->None:
    global thread_visits
    for i in range(100_000):
        with thread_lock:
            thread_visits +=  1


if __name__=="__main__":

    threads = [Thread(target = myfunction) for _ in range(100)]

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    print(thread_visits)


## multitheading example    
    
SYMBOLS = ('USD','EUR','PLN','NOK','CZK')
BASES = ('USD','EUR','PLN','NOK','CZK')

def fetch_rates(base :set):
    response  = requests.get(f"https://api.vatcomply.com/rates?base={base}")
    response.raise_for_status()
    rates = response.json()["rates"]

    rates[base] = 1
    return base, rates

def main()->None:
    for base in BASES:
        fetch_rates(base)

def present_result(base,rates):
    rates_line = ", ".join([f"{rates[symbol]:7f} {symbol}" for symbol in SYMBOLS])
    print(f"1 {base} = {rates_line}")


def worker(working_queue :Queue, result_queue :Queue)->None:
    while not working_queue.empty():
        try:
            item = working_queue.get_nowait()
        except Empty:
            break

        try:
            result = fetch_rates(item)
        except Exception as error:
            result_queue.put(error)
        else:
            result_queue.put(result)
        finally:
            working_queue.task_done()


def multi_threaded_main()->None:
    working_queue = Queue()
    result_queue = Queue()


    for base in BASES:
        working_queue.put(base)
    
    threads = [Thread(target=worker,args = (working_queue,result_queue)) for _ in range(4)]

    
    for thread in threads:
        thread.start()
    # unblocks and move forward once all the items are been processed by  task_done signal all the leftover count comes down to 0
    working_queue.join()

    while threads:
        threads.pop().join()

    while not result_queue.empty():
        result = result_queue.get()
        if isinstance(result,Exception):
            raise result
        else:
            present_result(*result)

if __name__ == "__main__":
    start = time.perf_counter()
    multi_threaded_main()
    #main()
    elapsed = time.perf_counter() - start
    print()
    print("time elapsed: {:.2f}s".format(elapsed))

