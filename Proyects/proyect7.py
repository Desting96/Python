# Complete the birthdayCakeCandles function below.
def birthdayCakeCandles(ar):
    ar.sort()
    return ar.count(ar[len(ar)-1])

if __name__ == '__main__':

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(ar)
    print(result)