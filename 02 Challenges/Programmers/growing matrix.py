def solution(n, left, right):
    # Create and pad the matrix. 
    SIZE = n
    RANGE = np.arange(1, SIZE+1)
    matrix = np.zeros((SIZE, SIZE))

    for i in reversed(RANGE):
        matrix[:i, :i] = i

    print(matrix)   

    array = []
    for i in range(SIZE):
        array.extend(matrix[i])


    array = [int(a) for a in array]
    print(array)

    return array[left:right+1]

print(solution(3, 2, 5))
print(solution(18, 7, 14))
