import random
import timeit

# Generate 100 random whole numbers between 0 and 100
data_set_1 = [random.randint(0, 100) for _ in range(100)]
# Generate 400 random whole numbers between 0 and 100
data_set_2 = [random.randint(0, 100) for _ in range(400)]
# Generate 800 random whole numbers between 0 and 100
data_set_3 = [random.randint(0, 100) for _ in range(800)]


#Using Bubble sort algorithm to sort this time around
# Define the Bubble Sort function
def bubble_sort(data_set):
    n = len(data_set)
    for i in range(n):
        for j in range(0, n-i-1):
            if data_set[j] > data_set[j+1]:
                data_set[j], data_set[j+1] = data_set[j+1], data_set[j]

# Define a function to sort a dataset using Bubble Sort and return the time taken
def time_bubble_sort(data_set):
    start_time = timeit.default_timer()
    bubble_sort(data_set)
    end_time = timeit.default_timer()
    return end_time - start_time

# Sort the data sets using Bubble Sort and track the time
time_taken_1 = time_bubble_sort(data_set_1)
print(f"Time taken to sort first data set (100 numbers) using Bubble Sort: {time_taken_1:.6f} seconds")

time_taken_2 = time_bubble_sort(data_set_2)
print(f"Time taken to sort second data set (400 numbers) using Bubble Sort: {time_taken_2:.6f} seconds")

time_taken_3 = time_bubble_sort(data_set_3)
print(f"Time taken to sort third data set (800 numbers) using Bubble Sort: {time_taken_3:.6f} seconds")

# Print the sorted data sets
print("Sorted data sets using Bubble Sort:")
print("First data set (100 numbers):", data_set_1)
print("Second data set (400 numbers):", data_set_2)
print("Third data set (800 numbers):", data_set_3)