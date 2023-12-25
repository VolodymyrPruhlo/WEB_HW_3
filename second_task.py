import time
import logging
from multiprocessing import Pool, current_process


def worker(num):
    return [i for i in range(1, num+1) if num % i == 0]
    
    
def factorize(numbers):
    with Pool(processes=2) as pool:
        return pool.map(worker, numbers)
    

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - {} - %(message)s'.format(current_process().name))
    
    numbers = [15, 28, 31, 45, 49]
    start_time = time.time()
    logging.debug(factorize(numbers))
    logging.debug(f"Час виконання: {time.time() - start_time} секунд")
