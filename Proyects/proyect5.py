# Complete the staircase function below.
def staircase(n):
    matriz = []
    cont = n-1
    for i in range(0, n):
        filas = []
        for j in range(0, n):
            if cont <= j:
                filas.append("#")
            else:
                filas.append(" ")
        cont -= 1
        matriz.append(filas)
    a = ""
    for i in range(0, n):
        for j in range(0, n):
            a += str(matriz[i][j])
        a += '\n'
    print(a)

if __name__ == '__main__':
    n = int(input())

    staircase(n)
