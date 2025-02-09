def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[(len(arr) - 1) // 2]
        less, equal, greater = [], [], []
        for i in arr:
            if i < pivot:
                less.append(i)
            elif i> pivot:
                greater.append(i)
            else:
                equal.append(i)
        return quicksort(less) + equal + quicksort(greater)

arr = [6, 3, 8, 5, 2, 7, 4, 1]
sorted_arr = quicksort(arr)
print(sorted_arr)