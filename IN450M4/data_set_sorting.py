import random
import timeit

# Generate 100 random whole numbers between 0 and 100
data_set_1 = [random.randint(0, 100) for _ in range(100)]

# Generate 400 random whole numbers between 0 and 100
data_set_2 = [random.randint(0, 100) for _ in range(400)]

# Generate 800 random whole numbers between 0 and 100
data_set_3 = [random.randint(0, 100) for _ in range(800)]

# Print the data sets before sorting
print("First data set (100 numbers):", data_set_1)
print("Second data set (400 numbers):", data_set_2)
print("Third data set (800 numbers):", data_set_3)

# Define a function to sort a dataset and return the time taken
def time_sort(data_set):
    start_time = timeit.default_timer()
    data_set.sort()
    end_time = timeit.default_timer()
    return end_time - start_time

# Sort the data sets using sort and track the time
time_taken_1 = time_sort(data_set_1)
print(f"Time taken to sort first data set (100 numbers): {time_taken_1:.6f} seconds")

time_taken_2 = time_sort(data_set_2)
print(f"Time taken to sort second data set (400 numbers): {time_taken_2:.6f} seconds")

time_taken_3 = time_sort(data_set_3)
print(f"Time taken to sort third data set (800 numbers): {time_taken_3:.6f} seconds")

# Print the sorted data sets
print("Sorted data sets:")
print("First data set (100 numbers):", data_set_1)
print("Second data set (400 numbers):", data_set_2)
print("Third data set (800 numbers):", data_set_3)
