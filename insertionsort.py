def insertion_sort(A):
    for j in range (1, len(A)): 
        key = A[j]
        i= j-1
        while i>=0 and A[i]>key:
            A[i+1] = A[i]
            i = i - 1
        A[i+1] = key

# best case: T(n) = an + b
#                   ^^^ linear time complexity

# worst case: T(n) = an^2 + bn + c 
#                   ^^^ quadratic time complexity 