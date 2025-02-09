def binary_search(arr, target):
    if len(arr) < 4:
        return target in arr
    
    mid = len(arr) // 2
    if arr[mid] == target:
        return True
    elif arr[mid] > target:
        return binary_search(arr[:mid], target)
    else:
        return binary_search(arr[mid+1:], target)
    
