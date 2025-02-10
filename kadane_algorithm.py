def kadane_max_subarray(arr):
    if not arr: 
        return 0
    
    max_current = arr[0]
    max_global = arr[0]

    for i in range(1, len(arr)):
        max_current = max(arr[i], max_current + arr[i])
        if max_current > max_global:
            max_global = max_current
        
    return max_global