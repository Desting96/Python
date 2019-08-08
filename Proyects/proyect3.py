#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#
def diagonalDifference(arr):
    sumdiag, sumdiaginv, min, max = 0, 0, 0, len(arr)-1
    for i in range(0, len(arr)):
        for j in range(0, len(arr)):
            if i == j:
                sumdiag += arr[i][j]
            if (min == i) and (max == j):
                sumdiaginv += arr[i][j]
                min += 1
                max -= 1
    if sumdiag >= sumdiaginv:
        return sumdiag - sumdiaginv
    else: return sumdiaginv - sumdiag

if __name__ == '__main__':

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)
    print(result)
