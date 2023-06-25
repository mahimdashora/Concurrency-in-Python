import threading
import time

# CPU-bound task
def cpu_bound_task(i):
    total = 0
    for _ in range(10**7):
        total += 1
    print(f"Task {i} done")
    return total
    

def main():
    start_time = time.time()
    # Threading execution
    threads = []
    for i in range(100):  # Create 100 threads
        thread = threading.Thread(target=cpu_bound_task,args=(i,))
        thread.start()
        threads.append(thread)
    
    for thread in threads:
        thread.join()
        
    
    execution_time = time.time() - start_time
    print("Threading Execution Time:", execution_time)

if __name__ == '__main__':
    main()