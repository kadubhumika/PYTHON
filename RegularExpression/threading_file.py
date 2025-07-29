import threading
import time

def worker(num):
    print(f"Thread {num}: Starting")
    time.sleep(2)
    print(f"Thread {num}: Ending")

threads = []

# Start all threads
for i in range(10):
    t = threading.Thread(target=worker, args=(i,))
    threads.append(t)
    t.start()

# Wait for all threads to complete
for t in threads:
    t.join()

print("All Threads Complete")
