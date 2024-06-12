# Insertion Sort
"""
@author: aldocema

Insertion Sort builds the sorted list one element at a time by repeatedly taking 
the next element from the unsorted part of the list and inserting it into its correct 
position in the sorted part of the list. The insertion_sort function takes a list as 
input and sorts it in ascending order in place. Finally, it includes a test case 
to demonstrate the sorting functionality.
"""

def insertion_sort(a_list):
    """
    Sorts a list in ascending order using the Insertion Sort algorithm.

    Parameters:
    a_list (list): The list to be sorted.

    Returns:
    None. The list is sorted in place.
    """
    for index in range(1, len(a_list)):
        current_value = a_list[index]
        position = index

        while position > 0 and a_list[position - 1] > current_value:
            a_list[position] = a_list[position - 1]
            position -= 1

        a_list[position] = current_value

# Test the insertion_sort function
a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20,1]
insertion_sort(a_list)
print(a_list)