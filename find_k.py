def find_k(s, left = 0, right = None):
    if right is None:
        right = len(s) - 1

    # if s has less than 4 elements, perform sequential search
    if right - left + 1 < 4:
        min_index = left
        for i in range(left, right + 1):
            if s[i] < s[min_index]:
                min_index = i
        return min_index
    
    mid = (left + right) // 2
    if s[mid] < s[mid - 1] and s[mid] < s[mid + 1]:
        return mid
    elif s[mid] > s[mid + 1]:
        return find_k(s, mid + 1, mid - 1)
    else: 
        return find_k(s, left, mid - 1)
    
