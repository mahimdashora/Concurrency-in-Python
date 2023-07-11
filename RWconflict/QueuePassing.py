from multiprocessing import Process, Queue

def sender(queue):
    messages = ['Hello', 'World', 'Goodbye']
    for message in messages:
        queue.put(message)

def receiver(queue):
    while True:
        message = queue.get()
        if message == 'Goodbye':
            break
        print('Received:', message)

if __name__ == '__main__':
    queue = Queue()
    
    sender_process = Process(target=sender, args=(queue,))
    receiver_process = Process(target=receiver, args=(queue,))
    
    sender_process.start()
    receiver_process.start()
    
    sender_process.join()
    receiver_process.join()
