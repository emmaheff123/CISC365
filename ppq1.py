def singleletter(s, start, end):
    if start > end: 
        return None
    elif start == end:
        return start
    else: 
        mid = (start + end) // 2
        if mid % 2 == 0:
            if s[mid] == s[mid+1]:
                return singleletter(s, mid + 2, end)
            else:
                return singleletter(s, start, mid)
        else: 
            if s[mid] == s[mid - 1]:
                return singleletter(s, mid + 1, end)
            else:
                return singleletter(s, start, mid - 1)
