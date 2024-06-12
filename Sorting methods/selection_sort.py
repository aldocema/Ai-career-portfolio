# Sorting Algorithms
"""
@author: aldocema
Selection Sort repeatedly selects the minimum element from the unsorted 
portion of the list and moves it to the sorted portion. The selection_sort 
function takes a list as input and sorts it in ascending order in place. Finally, 
it includes a test case to demonstrate the sorting functionality.
"""
# Selection Sort
def selection_sort(a_list):
    """
    Sorts a list in ascending order using the Selection Sort algorithm.

    Parameters:
    a_list (list): The list to be sorted.

    Returns:
    None. The list is sorted in place.
    """
    for fill_slot in range(len(a_list)-1, 0, -1):
        max_position = 0
        for location in range(1, fill_slot+1):
            if a_list[location] > a_list[max_position]:
                max_position = location

        a_list[fill_slot], a_list[max_position] = a_list[max_position], a_list[fill_slot]

# Test the selection_sort function
a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
selection_sort(a_list)
print(a_list)
