def merge_sort(list):
    """
    Sorts a list in ascending order
    Returns a new sorted list

    Divide: Find the mid_index of the list and divide into sublist
    Conquer: Recursivly sort the sublists create in previous step
    Combine: merge the sorted sublists create in previous step
    
    Takes O(k n log n) time
    """

    if len(list) <= 1:
        return list
    
    left_half, right_half = split(list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)
    
    return merge(left, right)


def split(list):
    """
    Divide the unsorted list at the midpoint into sublist
    Returns two sublist - left and right 

    Takes O(k log n)  time
    """ 

    mid = len(list)//2
    left = list[:mid]
    right = list[mid:]

    return left, right


def merge(left, right):
    """
    Merges two list (array), sorting them in the process
    Returns a new merged list

    Runs in overall O(n) time
    """
 
    l = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            l.append(left[i])
            i+=1
        else:
            l.append(right[j])
            j+=1
        
    while i < len(left):
        l.append(left[i])
        i+=1
    
    while j < len(right):
        l.append(right[j])
        j+=1

    return l 


def verify_sorted(list):
    n = len(list)

    if n == 0 or n == 1:
        return True

    return list[0] < list[1] and verify_sorted(list[1:])

alist = [34, 55, 81, 5, 54, 57, 43 ,12 ,32, 65, 87, 52]


print(f"Unsorted list: {alist}")
l = merge_sort(alist)
print(f"Sorted list: {l}")
print(f"Is the list sorted: {verify_sorted(l)}")

