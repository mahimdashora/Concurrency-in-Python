import multiprocessing
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
    # Multiprocessing execution
    processes = []
    for i in range(100):  # Create 100 processes
        process = multiprocessing.Process(target=cpu_bound_task, args=(i,))
        process.start()
        processes.append(process)
    
    for process in processes:
        process.join()
    
    execution_time = time.time() - start_time
    print("Multiprocessing Execution Time:", execution_time)

if __name__ == '__main__':
    main()