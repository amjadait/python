#!/usr/bin/env python
# coding: utf-8

# # 1)

# In[11]:


def binary_search(A, l, h, k):
    if h >= l:
        mid = int(l + (h - l)/2)
        print(mid)
        if A[mid] == k:
            return 'True, k is found'
        elif A[mid] > k:
            return binary_search(A, l, mid-1, k)
        else:
            return binary_search(A, mid+1, h, k)
    else:
        return 'False, k is not found'
    
A=[1, 2, 3, 5, 8]
k=46;l=0; h=len(A)-1;
binary_search(A, l, h, k)


# # 2)

# In[20]:


def power(a,b):
    resultat = a**b
    return resultat

a = 3 
b = 4 
resultat = power(a, b)
print(resultat)


# # 3)

# In[14]:


def bubbleSort(nlist):
    for passnum in range(len(nlist)-1,0,-1):
        for i in range(passnum):
            if nlist[i]>nlist[i+1]:
                temp = nlist[i]
                nlist[i] = nlist[i+1]
                nlist[i+1] = temp
    return nlist

nlist = [29,13,22,37,52,49,46,71,56]
bubbleSort(nlist)


# # 4)

# In[15]:


def mergeSort(myList):
    if len(myList) > 1:
        mid = len(myList) // 2
        left = myList[:mid]
        right = myList[mid:]

        # Recursive call on each half
        mergeSort(left)
        mergeSort(right)

        # Two iterators for traversing the two halves
        i = 0
        j = 0
        
        # Iterator for the main list
        k = 0
        
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
              # The value from the left half has been used
              myList[k] = left[i]
              # Move the iterator forward
              i += 1
            else:
                myList[k] = right[j]
                j += 1
            # Move to the next slot
            k += 1

        # For all the remaining values
        while i < len(left):
            myList[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            myList[k]=right[j]
            j += 1
            k += 1

myList = [29,13,22,37,52,49,46,71,56]
mergeSort(myList)
print(myList)


# # 5)

# In[18]:


def partition(array, start, end):
    pivot = array[start]
    low = start + 1
    high = end
    while True:
        # If the current value we're looking at is larger than the pivot
        # it's in the right place (right side of pivot) and we can move left,
        # to the next element.
        # We also need to make sure we haven't surpassed the low pointer, since that
        # indicates we have already moved all the elements to their correct side of the pivot
        while low <= high and array[high] >= pivot:
            high = high - 1

        # Opposite process of the one above
        while low <= high and array[low] <= pivot:
            low = low + 1

        # We either found a value for both high and low that is out of order
        # or low is higher than high, in which case we exit the loop
        if low <= high:
            array[low], array[high] = array[high], array[low]
            # The loop continues
        else:
            # We exit out of the loop
            break

    array[start], array[high] = array[high], array[start]

    return high


def quick_sort(array, start, end):
    if start >= end:
        return

    p = partition(array, start, end)
    quick_sort(array, start, p-1)
    quick_sort(array, p+1, end)

array = [29,13,22,37,52,49,46,71,56]
quick_sort(array, 0, len(array) - 1)
print(array)


# In[ ]:




