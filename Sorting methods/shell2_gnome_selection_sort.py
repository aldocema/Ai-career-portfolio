# Sorting Algorithms
"""
@author: aldocema
Gnome Sort iterates through the list, swapping adjacent elements if they 
are in the wrong order. It moves backward when a swap occurs, ensuring 
that all elements are in the correct position. This process continues until 
the list is sorted.
"""
# gnome sort
def gnome_sort(lista):
    """
    Sorts a list in ascending order using the Gnome Sort algorithm.

    Parameters:
    lista (list): The list to be sorted.

    Returns:
    list: The sorted list.
    """
    i = 0
    n = len(lista)
    
    while i < n:
        if i == 0 or lista[i] >= lista[i-1]:
            i += 1
        else:
            temp = lista[i-1]
            lista[i-1] = lista[i]
            lista[i] = temp
            i -= 1

    return lista


# Second way to program shell and selection sort

def shellsort(lista):
    """
    Sorts a list in ascending order using the Shell Sort algorithm.

    Parameters:
    lista (list): The list to be sorted.

    Returns:
    list: The sorted list.
    """
    n=len(lista)
    g=n//2
    
    while g>0:
        for i in range(g,n):
            temp=lista[i]
            j=i
            while j>=g and lista[j-g] > temp:
                lista[j]=lista[j-g]
                j -=g
            lista[j]=temp
        g=g//2
    return lista

def selectionsort(lista):
    """
    Sorts a list in ascending order using the Selection Sort algorithm.

    Parameters:
    lista (list): The list to be sorted.

    Returns:
    list: The sorted list.
    """
    for i in range(len(lista)):
        min_pos=i
        for j in range(i,len(lista)-1):
            if lista[min_pos]>lista[j+1]:
                min_pos=j+1
        temp=lista[i]
        lista[i]=lista[min_pos]
        lista[min_pos]=temp             
    return lista

var_sort=[0,345,23,52,5,2,7,63,1,45]

print('gnome sort:', gnome_sort(var_sort))
print('Shell sort:', shellsort(var_sort))
print('selection sort', selectionsort(var_sort))