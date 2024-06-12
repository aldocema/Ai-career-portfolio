# Sorting Algorithms
"""
@author: aldocema
Shell Sort is an extension of insertion sort that allows the exchange of items 
that are far apart. The shell_sort function takes a list as input and sorts it 
in ascending order in place. Finally, it includes a test case to demonstrate 
the sorting functionality.
"""
# Shell Sort
def shell_sort(a_list):
    """
    Sorts a list in ascending order using the Shell Sort algorithm.

    Parameters:
    a_list (list): The list to be sorted.

    Returns:
    None. The list is sorted in place.
    """
    def gap_insertion_sort(a_list, start, gap):
        for i in range(start + gap, len(a_list), gap):
            current_value = a_list[i]
            position = i

            while position >= gap and a_list[position - gap] > current_value:
                a_list[position] = a_list[position - gap]
                position -= gap

            a_list[position] = current_value

    sublist_count = len(a_list) // 2
    while sublist_count > 0:
        for start_position in range(sublist_count):
            gap_insertion_sort(a_list, start_position, sublist_count)

        sublist_count //= 2

# Test the shell_sort function
a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
shell_sort(a_list)
print(a_list)
