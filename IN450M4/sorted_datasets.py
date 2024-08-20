import random
import timeit

# Generate 100 random whole numbers between 0 and 100
data_set_1 = [random.randint(0, 100) for _ in range(100)]
# Generate 400 random whole numbers between 0 and 100
data_set_2 = [random.randint(0, 100) for _ in range(400)]
# Generate 800 random whole numbers between 0 and 100
data_set_3 = [random.randint(0, 100) for _ in range(800)]

# Define a function to sort a dataset using sorted() and return the time taken
#Using the sorted() function with a custom key: The sorted() function is similar to the .sort() method but returns a new sorted list. 
#it can be used with a custom key function to optimize certain types of sorting
def time_sorted(data_set):
    start_time = timeit.default_timer()
    sorted_data_set = sorted(data_set)
    end_time = timeit.default_timer()
    return end_time - start_time, sorted_data_set

# Sort the data sets using sorted() and track the time
time_taken_1, sorted_data_set_1 = time_sorted(data_set_1)
print(f"Time taken to sort first data set (100 numbers) using sorted(): {time_taken_1:.6f} seconds")

time_taken_2, sorted_data_set_2 = time_sorted(data_set_2)
print(f"Time taken to sort second data set (400 numbers) using sorted(): {time_taken_2:.6f} seconds")

time_taken_3, sorted_data_set_3 = time_sorted(data_set_3)
print(f"Time taken to sort third data set (800 numbers) using sorted(): {time_taken_3:.6f} seconds")

# Print the sorted data sets
print("Sorted data sets using sorted():")
print("First data set (100 numbers):", sorted_data_set_1)
print("Second data set (400 numbers):", sorted_data_set_2)
print("Third data set (800 numbers):", sorted_data_set_3)