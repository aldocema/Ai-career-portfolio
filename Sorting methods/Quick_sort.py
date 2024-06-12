# Sorting Algorithms
"""
@author: aldocema
Quick Sort works by selecting a 'pivot' element from the list and partitioning 
the other elements into two sub-lists according to whether they are less than 
or greater than the pivot. It then recursively sorts the sub-lists. 
The quick_sort function takes a list as input and sorts it in ascending order in place.
Finally, it includes a test case to demonstrate the sorting functionality.
"""
# Quick Sort
def quick_sort(a_list):
    """
    Sorts a list in ascending order using the Quick Sort algorithm.

    Parameters:
    a_list (list): The list to be sorted.

    Returns:
    None. The list is sorted in place.
    """
    def quick_sort_helper(a_list, first, last):
        if first < last:
            pivot_index = partition(a_list, first, last)
            quick_sort_helper(a_list, first, pivot_index - 1)
            quick_sort_helper(a_list, pivot_index + 1, last)

    def partition(a_list, first, last):
        pivot_value = a_list[first]
        left_mark = first + 1
        right_mark = last
        done = False

        while not done:
            while left_mark <= right_mark and a_list[left_mark] <= pivot_value:
                left_mark += 1

            while a_list[right_mark] >= pivot_value and right_mark >= left_mark:
                right_mark -= 1

            if right_mark < left_mark:
                done = True
            else:
                a_list[left_mark], a_list[right_mark] = a_list[right_mark], a_list[left_mark]

        a_list[first], a_list[right_mark] = a_list[right_mark], a_list[first]

        return right_mark

    quick_sort_helper(a_list, 0, len(a_list) - 1)

# Test the quick_sort function
a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20,543]
quick_sort(a_list)
print(a_list)
