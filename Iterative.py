# The iterative method to solve max subarray problem
def find_maximum_subarray_iterative(A):
    assert(len(A) > 0)
    l_index = 0
    length = 1
    summ = A[0]
    startPoint = 0
    lengthMark = 1
    useSum = A[0]
    for i in range(1, len(A)):
        if(A[i] >= useSum + A[i]):
            startPoint = i
            lengthMark = 1
            useSum = A[i]
        else:
            lengthMark += 1
            useSum += A[i]
        if((useSum > summ)or((useSum == summ)and(lengthMark < length))
           or((useSum == summ)and(lengthMark == length)
           and(startPoint < l_index))):
            l_index = startPoint
            length = lengthMark
            summ = useSum
    return [l_index, l_index+length - 1]
