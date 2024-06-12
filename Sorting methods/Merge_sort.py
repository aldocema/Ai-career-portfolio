# Sorting Algorithms

# Merge Sort
"""
@author: aldocema
Merge Sort divides the list into smaller halves, sorts them recursively, 
and then merges them back together into a sorted list. The merge_sort function 
takes a list as input and sorts it in ascending order in place. Finally, it includes 
a test case to demonstrate the sorting functionality.
"""
def merge_sort(a_list):
    """
    Sorts a list in ascending order using the Merge Sort algorithm.

    Parameters:
    a_list (list): The list to be sorted.

    Returns:
    None. The list is sorted in place.
    """
    def merge(left_half, right_half):
        merged_list = []
        i = j = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                merged_list.append(left_half[i])
                i += 1
            else:
                merged_list.append(right_half[j])
                j += 1

        merged_list.extend(left_half[i:])
        merged_list.extend(right_half[j:])
        return merged_list

    print("Divide ", a_list)
    if len(a_list) > 1:
        mid = len(a_list) // 2
        left_half = a_list[:mid]
        right_half = a_list[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        a_list[:] = merge(left_half, right_half)
    print("Merge ", a_list)

# Test the merge_sort function
a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
merge_sort(a_list)
print(a_list)
