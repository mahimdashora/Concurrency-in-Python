import time

# CPU-bound task
def cpu_bound_task():
    total = 0
    for _ in range(10**7):
        total += 1
    return total

def main():
    start_time = time.time()
    
    # Sequential execution
    for i in range(100):
        result = cpu_bound_task()
        print(f"Task {i} done")
    
    execution_time = time.time() - start_time
    print("Sequential Execution Time:", execution_time)

if __name__ == '__main__':
    main()
