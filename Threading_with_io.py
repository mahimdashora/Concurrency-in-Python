import threading
import time

# io-bound task
def io_bound_task():
    for _ in range(5):
        time.sleep(2)
    

def main():
    start_time = time.time()
    # Threading execution
    threads = []
    for i in range(100):  # Create 100 threads
        thread = threading.Thread(target=io_bound_task)
        thread.start()
        threads.append(thread)
    
    for thread in threads:
        thread.join()
        
    
    execution_time = time.time() - start_time
    print("Threading Execution Time:", execution_time)

if __name__ == '__main__':
    main()