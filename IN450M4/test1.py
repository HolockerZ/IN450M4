import threading
import time
import random

class DressingRooms:
    def __init__(self, num_rooms=3):
        self.num_rooms = num_rooms # Number of rooms, set to 3 as per assignment
        self.semaphore = threading.Semaphore(num_rooms) # Semaphore equal to the rooms in order to limit the number of rooms
        self.lock = threading.Lock()  # Lock to prevent race conditions, this fixed run error I was having..
        self.rooms_in_use = 0  # To keep track of how many rooms are in use
        self.waiting_time = 0 # To keep track of how long the waiting time is for each person
#in essence, the semaphore is used to limit the number of rooms, the lock is used to prevent race conditions, and the rooms_in_use is used to keep track of how many rooms are in use.
# This was the only way I saw to have the number of rooms be used and the waiting time be tracked.
    def requestRoom(self):
        start_time = time.time()
        self.semaphore.acquire()
        with self.lock:
            self.rooms_in_use += 1
        end_time = time.time()
        self.waiting_time += end_time - start_time

    def releaseRoom(self):
        with self.lock:
            self.rooms_in_use -= 1
        self.semaphore.release()

class Customer(threading.Thread): # Customer class is a thread as per assignment
    def __init__(self, dressing_rooms, num_items=0):
        super().__init__()
        self.dressing_rooms = dressing_rooms
        self.num_items = num_items
        self.usage_time = 0

    def run(self):
        self.dressing_rooms.requestRoom()
        if self.num_items == 0:
            self.num_items = random.randint(1, 6)
        start_time = time.time()
        for _ in range(self.num_items):
            time.sleep(random.uniform(1, 3))
        end_time = time.time()
        self.usage_time = end_time - start_time
        self.dressing_rooms.releaseRoom()

class Scenario:
    def __init__(self, num_rooms, num_customers, num_items):
        self.num_rooms = num_rooms
        self.num_customers = num_customers
        self.num_items = num_items
        self.dressing_rooms = DressingRooms(num_rooms)
        self.customers = []
        self.start_time = 0
        self.end_time = 0

    def scenario(self):
        self.start_time = time.time()
        for _ in range(self.num_customers):
            customer = Customer(self.dressing_rooms, self.num_items)
            customer.start()
            self.customers.append(customer)
        for customer in self.customers:
            customer.join()
        self.end_time = time.time()

    def calculate_stats(self):
        total_usage_time = sum(customer.usage_time for customer in self.customers)
        avg_usage_time = total_usage_time / self.num_customers
        avg_num_items = sum(customer.num_items for customer in self.customers) / self.num_customers
        waiting_time = self.dressing_rooms.waiting_time
        elapsed_time = self.end_time - self.start_time
        print(f"Scenario: {self.num_rooms} rooms, {self.num_customers} customers, {self.num_items} items")
        print(f"Average usage time: {avg_usage_time:.2f} seconds")
        print(f"Average number of items: {avg_num_items:.2f}")
        print(f"Waiting time: {waiting_time:.2f} seconds")
        print(f"Elapsed time: {elapsed_time:.2f} seconds")

def main():
    scenarios = [
        Scenario(10, 20, 0),
        Scenario(20, 20, 0),
        Scenario(10, 10, 6)
    ]
    for i, scenario in enumerate(scenarios):
        print(f"Scenario {i+1}:")
        scenario.scenario()
        scenario.calculate_stats()
        print()

if __name__ == "__main__":
    main()
    