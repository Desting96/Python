# Complete the compareTriplets function below.
def compareTriplets(a, b):
    pointa = 0
    pointb = 0
    for i in range(0, 3):
        if a[i] > b[i]:
            pointa += 1
        elif a[i] < b[i]:
            pointb += 1
    return (pointa, pointb)

if __name__ == '__main__':

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)
    print(result)


