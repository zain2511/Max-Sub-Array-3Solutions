# The brute force method to solve max subarray problem
def find_maximum_subarray_brute(A):
    assert(len(A) > 0)
    maxVal = A[0]
    l_index = 0
    r_index = 0
    for i in range(0, len(A)):
        summ = 0
        for j in range(i, len(A)):
            summ = summ + A[j]
            if(summ > maxVal):
                maxVal = summ
                l_index = i
                r_index = j
    return l_index, r_index
