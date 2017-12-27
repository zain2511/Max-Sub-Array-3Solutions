# The maximum crossing subarray method for solving the max subarray problem
def find_maximum_crossing_subarray(A, low, mid, high):
    l_index = 0
    i = mid
    summ = 0
    leftsum = 0
    while i >= low:
        summ = summ + A[i]
        if summ > leftsum:
            leftsum = summ
            l_index = i
        i = i - 1
    r_index = 0
    j = mid + 1
    summ = 0
    rightsum = 0
    while j <= high:
        summ = summ + A[j]
        if summ > rightsum:
            rightsum = summ
            r_index = j
        j = j + 1
    if(r_index == 0):
        r_index = l_index
    if((l_index == 0) and (A[r_index] == leftsum + rightsum)):
        l_index = r_index
    return [[l_index, r_index], leftsum + rightsum]


# The recursive method to solve max subarray problem
def find_maximum_subarray_recursive_helper(A, low=0, high=-1):
    if low > high:
        return [[-1, -1], -1]
    if low == high:
        return [[low, high], A[low]]
    else:
        middle = (low + high) // 2
        sumLeft = find_maximum_subarray_recursive_helper(A, low, middle)
        sumRight = find_maximum_subarray_recursive_helper(A, middle+1, high)
        sumCross = find_maximum_crossing_subarray(A, low, middle, high)
        if sumLeft[1] > sumRight[1]:
            if sumLeft[1] > sumCross[1]:
                return sumLeft
            else:
                return sumCross
        else:
            if sumRight[1] > sumCross[1]:
                return sumRight
            else:
                return sumCross


# The recursive method to solve max subarray problem
def find_maximum_subarray_recursive(A):
    assert(len(A) > 0)
    checkNegative = max(A)
    if checkNegative < 0:
        i = A.index(checkNegative)
        return [[i, i]][0]
    else:
        return find_maximum_subarray_recursive_helper(A, 0, len(A) - 1)[0]
