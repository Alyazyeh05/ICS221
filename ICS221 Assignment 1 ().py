import matplotlib.pyplot as plt
import numpy as np
import time

# Chocolate Distribution Algorithm
def distribute_chocolates_iter(chocolates, students):
    distributed = []
    for i, student in enumerate(students):
        if i < len(chocolates):
            distributed.append((student, chocolates[i]))
        else:
            break
    return distributed

def distribute_chocolates_rec(chocolates, students, index=0):
    if index >= len(students) or index >= len(chocolates):
        return []
    else:
        return [(students[index], chocolates[index])] + distribute_chocolates_rec(chocolates, students, index + 1)

# Sorting Algorithms
def sort_by_weight(chocolates):
    return sorted(chocolates, key=lambda x: x[2])

def sort_by_price(chocolates):
    return sorted(chocolates, key=lambda x: x[3])

# Searching Algorithm
def search_chocolate(chocolates, target):
    for chocolate in chocolates:
        if chocolate[2] == target or chocolate[3] == target:
            return chocolate
    return None

# Time Complexity Functions
def linear(n):
    return n

def nlogn(n):
    return n * np.log(n)

def constant(n):
    return np.ones_like(n)

# Define the range of input values
n_values = np.arange(1, 100)

# Sensitivity analysis for each algorithm
execution_times = {'Distribution': [], 'Sorting': [], 'Searching': []}
min_threshold = 0.0001  # Set a minimum threshold for execution time

for n in n_values:
    # Chocolate Distribution Algorithm
    chocolates = [(i, "Milk", np.random.randint(10, 100), np.random.uniform(1.0, 5.0)) for i in range(n)]
    students = ["Student" + str(i) for i in range(n)]
    start_time = time.time()
    distribute_chocolates_iter(chocolates, students)
    end_time = time.time()
    exec_time = end_time - start_time
    execution_times['Distribution'].append(max(exec_time, min_threshold))

    # Sorting Algorithm
    chocolates = [(i, "Milk", np.random.randint(10, 100), np.random.uniform(1.0, 5.0)) for i in range(n)]
    start_time = time.time()
    sort_by_weight(chocolates)
    end_time = time.time()
    exec_time = end_time - start_time
    execution_times['Sorting'].append(max(exec_time, min_threshold))

    # Searching Algorithm
    chocolates = [(i, "Milk", np.random.randint(10, 100), np.random.uniform(1.0, 5.0)) for i in range(n)]
    sorted_by_weight = sort_by_weight(chocolates)
    start_time = time.time()
    search_chocolate(sorted_by_weight, 40)
    end_time = time.time()
    exec_time = end_time - start_time
    execution_times['Searching'].append(max(exec_time, min_threshold))

# Plotting the Time Complexities

# Plotting Chocolate Distribution Algorithm
plt.figure(figsize=(12, 8))
plt.subplot(2, 2, 1)
plt.plot(n_values, linear(n_values), label='Chocolate Distribution Algorithm', color='blue')
filtered_execution_times_distribution = [max(t, min_threshold) for t in execution_times['Distribution']]
plt.scatter(n_values, filtered_execution_times_distribution, color='blue')
plt.title('Chocolate Distribution Algorithm')
plt.xlabel('Input Size (n)')
plt.ylabel('Time (T)')
plt.grid(True)
plt.legend()

# Plotting Sorting Algorithm
plt.subplot(2, 2, 2)
plt.plot(n_values, nlogn(n_values), label='Sorting Algorithm', color='green')
filtered_execution_times_sorting = [max(t, min_threshold) for t in execution_times['Sorting']]
plt.scatter(n_values, filtered_execution_times_sorting, color='green')
plt.title('Sorting Algorithm')
plt.xlabel('Input Size (n)')
plt.ylabel('Time (T)')
plt.grid(True)
plt.legend()

# Plotting Searching Algorithm
plt.subplot(2, 2, 3)
plt.plot(n_values, constant(n_values), label='Searching Algorithm', color='red')
filtered_execution_times_searching = [max(t, min_threshold) for t in execution_times['Searching']]
plt.scatter(n_values, filtered_execution_times_searching, color='red')
plt.title('Searching Algorithm')
plt.xlabel('Input Size (n)')
plt.ylabel('Time (T)')
plt.grid(True)
plt.legend()

# Plotting Combined Graph
plt.subplot(2, 2, 4)
plt.plot(n_values, linear(n_values), label='Chocolate Distribution Algorithm', color='blue')
plt.plot(n_values, nlogn(n_values), label='Sorting Algorithm', color='green')
plt.plot(n_values, constant(n_values), label='Searching Algorithm', color='red')
plt.title('Combined Time Complexity Analysis')
plt.xlabel('Input Size (n)')
plt.ylabel('Time (T)')
plt.grid(True)
plt.legend()

# Show plot
plt.tight_layout()
plt.show()