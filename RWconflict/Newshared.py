import multiprocessing

# Create a shared array
shared_array = multiprocessing.Array('i', [1, 2, 3, 4, 5])

# Create a shared value
shared_value = multiprocessing.Value('i', 0)

# Function to modify the shared array and value
def modify_shared_data(array, value, index):
    # Modify the shared array at the given index
    array[index] = index * 10
    
    # Modify the shared value by incrementing it with the index
    value.value += index

# Create a list to hold the processes
if __name__=="__main__":
 processes = []

# Create 5 processes to modify the shared data

 for i in range(5):
    process = multiprocessing.Process(target=modify_shared_data, args=(shared_array, shared_value, i))
    processes.append(process)
    process.start()

    # Wait for all processes to finish
 for process in processes:
    process.join()

 # Print the modified shared array
 print("Modified shared array:", shared_array[:])

 # Print the modified shared value
 print("Modified shared value:", shared_value.value)
