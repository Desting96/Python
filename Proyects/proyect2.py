# Complete the aVeryBigSum function below.
def aVeryBigSum(ar):
    res = 0
    for i in ar:
        res += i
    return res

if __name__ == '__main__':

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = aVeryBigSum(ar)
    print(result)
