def find_majority(s, start, end):
    if start == end:
        return s[start]
    else: 
        mid = (end + start) // 2
        l = find_majority(s, start, mid)
        r = find_majority(s, mid + 1, end)
        if l == r:
            return 1
        else:
            if s.count(1) > (end - start + 1)/2:
                return 1
            elif s.count(r) > (end - start + 1)/3:
                return r
            else:
                return None
            