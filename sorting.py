'''
Insertion will have worst case run time of O(n^2)
because we have a while loop nested in a for loop, each
depending on n
'''

def Insertion(arr):
    idx = 0

    for i in range(1, len(arr)):
        idx = arr[i]
        j = i - 1

        while (j >= 0 and idx < arr[j]):
            arr[j+1] = arr[j]
            j -= 1

        arr[j+1] = idx
    print(arr)

print("Insertion sort:")
arr = [2,1,45,21,12,3,4,5,6,9,8,7]
Insertion(arr)
print()

'''
Bubble sort is going to have worst case run time O(n^2)
because we have a nested for loop which is dependent on n
'''
def Bubble(arr):
    for i in range(len(arr)):
        for j in range(0, len(arr)-1):
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp

    print(arr)


print("Bubble Sort:")
arr2 = [2,1,45,21,12,3,4,5,6,9,8,7]
Bubble(arr2)

'''
Selection sort will have worst case run time O(n^2)
because we have a nested for loop which is dependent on n.
'''
def Selection(arr):
    for i in range(len(arr)):
        min = i
        for j in range(i + 1, len(arr)):
            if arr[min] > arr[j]:
                min = j

        arr[i], arr[min] = arr[min], arr[i]

    print(arr)

print("Selection Sort:")
arr3 = [2,1,45,21,12,3,4,5,6,9,8,7]
Selection(arr3)


'''
Merge sort will have worst case run time O(nlog(n))
because each time we iterate, the list gets split in half which takes log(n)
time and the merging process takes linear time, thus, nlog(n).
'''
def Merge(arr):
    if len(arr) > 1:
        mid = len(arr) // 2

        Leftside = arr[:mid]
        Rightside = arr[mid:]
        print(Leftside)
        print(Rightside)
        Merge(Leftside)
        Merge(Rightside)

        i = 0
        j = 0
        k = 0
        while (i < len(Leftside) and j < len(Rightside)):
            if Leftside[i] < Rightside[j]:
                arr[k] = Leftside[i]
                i += 1
            else:
                arr[k] = Rightside[j]
                j += 1
            k += 1

        while i < len(Leftside):
            arr[k] = Leftside[i]
            i += 1
            k += 1

        while j < len(Rightside):
            arr[k] = Rightside[j]
            j += 1
            k += 1

    return(arr)

print("Merge Sort:")
arr4 = [4, 1, 57, 34, 35, 27, 18]
print(Merge(arr4))