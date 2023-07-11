import multiprocessing

def increment_counter(counter):
    counter.value += 1  # Atomic increment operation

if __name__ == '__main__':
    counter = multiprocessing.Value('i', 0)
    
    processes = []
    for _ in range(5):
        p = multiprocessing.Process(target=increment_counter, args=(counter,))
        processes.append(p)
        p.start()
    
    for p in processes:
        p.join()
    
    print("Counter value:", counter.value)
