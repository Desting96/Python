# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    sumas = []
    ini = 0
    cont = 1
    fin = len(arr)-1
    for i in range(0, len(arr)):
        suma = 0
        if fin <= len(arr):
            for j in arr[i:fin]:
                suma += j
            fin += 1
            sumas.append(suma)
        else:
            fin -= 1
            for j in arr[ini:cont]:
                suma += j
            for j in arr[cont+1:fin]:
                suma += j
            cont += 1
            fin += 1
            sumas.append(suma)
    sumord= sorted(sumas)
    print(sumord[0], sumord[fin-2])

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)