# Complete the plusMinus function below.
def plusMinus(arr):
    contpositive, contnegative, contzero = 0, 0, 0

    for i in arr:
        if i > 0:
            contpositive += 1
        elif i < 0:
            contnegative += 1
        else:
            contzero += 1

    print('{0:.6f}'.format(contpositive/len(arr)))
    print('{0:.6f}'.format(contnegative/len(arr)))
    print('{0:.6f}'.format(contzero/len(arr)))

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
