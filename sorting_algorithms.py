# Sorting Algorithms Performance Analysis
# Author: Evelyn Contreras

import random
import time
import matplotlib.pyplot as plt
import sys


# Sorting Algorithms (Implement these)
def bubble_sort(arr):
    
    # outer loop which keeps track of elements settled at the end
    for i in range(len(arr)):
    # inner loop which compares adjacent elements
        for j in range(len(arr)-1-i):
            # if left element is greater than right element then swap them
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j] # swapping adjacent elements
    return arr #returns sorted array


def quick_sort(arr):
    
    # if: list has one or fewer elements, it is sorted
    if len(arr) <= 1:
        return arr
    
    # else: assign a pivot element, compare elements in arr to pivot element
    else:
        pivot_element_index = random.randint(0, len(arr)-1)
        pivot_element = arr[pivot_element_index] # assign an element from arr as the pivot element
        left = [] # contains elements smaller than the pivot element
        right = [] # contains elements greater than the pivot element
        middle = [] # contains pivot element and any duplicates of it
        
        # compare each element in arr to pivot element
        for num in arr:
            
            # if: element is less than the pivot element, append to left list
            if num < pivot_element: 
                left.append(num)
                
            # elif: element is greater than the pivot element, append to right list
            elif num > pivot_element:
                right.append(num)
                
            else:
                middle.append(num) # catch the pivot element and any duplicates of it
                
        combined_list = quick_sort(left) + middle + quick_sort(right) # recursively call quick_sort on left and right list, and combine results
        
        return (combined_list) #return the combined result

def merge_sort(arr):
    
    # if: list has one or fewer elements, it is sorted
    if len(arr) <= 1: 
        return arr
    
    # else: split the list into two halves 
    else:
        left_list = arr[:(len(arr))//2] # left half of the list
        right_list = arr[(len(arr))//2:] # right half of the list
        
        left_list = merge_sort(left_list) # recursively sort left half
        right_list = merge_sort(right_list) # recursively sort right half
        
        return merge(left_list, right_list) # merge the two halves and return
    
    
def merge(left, right):
    
    combined_list = []
    # while both, the left and right list, are not empty
    while left and right:
        if left[0] <= right[0]: # if: left element is less than right element
            combined_list.append(left[0]) # append left element to combined_list
            left.pop(0) # remove left element from list left
            
        # else: right element is less than
        else:
            
            combined_list.append(right[0]) # append right element to combined_list
            right.pop(0) # remove right element from list right 
            
    combined_list = combined_list + left # add remaining elements to combined_list from list left
    combined_list = combined_list +right # add remaining elements to combined_list from list right 
    
    return combined_list #return combined_list


# Function to generate input data
def generate_input(cnt, input_type):
    if input_type == 1:  # Totally random numbers
        return [random.randint(0, cnt) for _ in range(cnt)]
    elif input_type == 2:  # Sorted numbers
        return list(range(cnt))
    else:
        raise ValueError("Invalid input type")

# Function to sort the array and measure the execution time
def sort_and_measure(cnt, sorting, input_type):
    arr = generate_input(cnt, input_type)
    start_time = time.time()
    
    if sorting == "Bubble sort":
        sorted_arr = bubble_sort(arr)
    elif sorting == "Quick sort":
        sorted_arr = quick_sort(arr)
    elif sorting == "Merge sort":
        sorted_arr = merge_sort(arr)
    else:
        raise ValueError("Invalid sorting algorithm")
    
    elapsed_time = time.time() - start_time
    print(f"{cnt} elements sorted using {sorting}. Time taken: {elapsed_time:.4f} seconds.")
    return elapsed_time

# Function to plot the performance of the sorting algorithms
def plot_performance(cnt, input_types, sorting_algorithms):
    results = {alg: {inp: [] for inp in input_types} for alg in sorting_algorithms}
    
    for alg in sorting_algorithms:
        for inp in input_types:
            time_taken = sort_and_measure(cnt, alg, inp)
            results[alg][inp].append(time_taken)
    
    for alg in sorting_algorithms:
        plt.plot(input_types, [results[alg][inp][0] for inp in input_types], label=alg)
    
    plt.xlabel('Input Type')
    plt.ylabel('Time (seconds)')
    plt.title(f'Performance of Sorting Algorithms for {cnt} elements')
    plt.xticks(input_types, ['Random', 'Sorted'])
    plt.legend()
    plt.show()

if __name__ == "__main__":
    if len(sys.argv) == 3:
        cnt = int(sys.argv[1])
        sorting = sys.argv[2]
        sort_and_measure(cnt, sorting, 1)
        
    else:
        cnt = 500000
        input_types = [1, 2]  # 1: Random, 2: Sorted
        sorting_algorithms = ["Bubble sort", "Quick sort", "Merge sort"]
        plot_performance(cnt, input_types, sorting_algorithms)
        