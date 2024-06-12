# Sorting Algorithms
"""
@author: aldocema
Bubble Sort is a sorting algorithm that repeatedly steps through the list, 
compares adjacent elements, and swaps them if they are in the wrong order. 
This process continues until the list is sorted. The name "Bubble Sort" comes from 
the way larger elements gradually "bubble" towards their correct positions. 
While easy to understand, Bubble Sort is not efficient for large lists due to its 
quadratic time complexity O(n2)O(n^2)O(n2). However, it's useful for teaching sorting 
concepts and for small lists where simplicity is more important than performance.
"""
# Bubble Sort
def bubble_sort(a_list):
    """
    Sorts a list in ascending order using the Bubble Sort algorithm.

    Parameters:
    a_list (list): The list to be sorted.

    Returns:
    None. The list is sorted in place.
    """
    for pass_num in range(len(a_list)-1, 0, -1):
        for i in range(pass_num):
            if a_list[i] > a_list[i+1]:
                a_list[i], a_list[i+1] = a_list[i+1], a_list[i]

# Test the bubble_sort function
a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
bubble_sort(a_list)
print(a_list)