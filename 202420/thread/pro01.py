import multiprocessing
import os
import time
def print_numbers():
    pid=os.getpid()
    for i in range(10):
        #print(i)
        print(f'{i}@{pid}')
        time.sleep(2)

if __name__ == '__main__':
    processes=[]
    for i in range(5):
        process = multiprocessing.Process(target=print_numbers)
        processes.append(process)
        process.start()
        #process.join()
    print_numbers()    