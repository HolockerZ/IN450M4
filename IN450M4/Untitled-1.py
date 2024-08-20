import random

#I need a waiting room for the customers, it needs to be able to add customers and remove customers
#I need to be able to check if the room is full
#I need to be able to check if the room is empty


class WaitingRoom:
    def __init__(self, capacity, max_items, rooms):
        self.capacity = capacity
        self.customers = []
        self.max_items = max_items
        self.rooms = rooms

    def add_customer(self, customer_name, Number_of_items):
        if len(self.customers) < self.capacity:
            self.customers.append(customer_name)
            return True # customer added
        else:
            return False # room is full
        if len(Number_of_items) <= self.Number_of_items:
            return "You are good to enter and try those on"
        else:
            return "You have too many items"