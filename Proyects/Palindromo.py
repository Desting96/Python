def palindromo(data):
    atras, palin= -1, True
    for i in data:
        if i == data[atras]:
            atras += -1
        else:
            palin = False
            break
    return palin

def centuryFromYear(year):
    cont, century = 1, 0
    while cont <= year:
        cont = cont +100
        century +=1
    return century

def adjacentElementsProduct(inputArray):
    pos, res = 0, []
    for i in inputArray[pos+1:]:
        res.append(inputArray[pos]*i)
        pos += 1
    return max(res)

def shapeArea(n):
    poligon = 1
    for i in range(n):
        poligon += (4*i)
    return poligon

def makeArrayConsecutive2(statues):
    cont = 0
    for i in range(min(statues),max(statues)+1):
        if (i in statues) == False:
            cont += 1
    return cont


def almostIncreasingSequence(sequence):
    inicio, medio, fin, cont, res = 0, 1, 2, 0, True
    for i in range(len(sequence)-2):
        if sequence[inicio] > sequence [medio]:
            sequence.pop(inicio)
            print(sequence)
            cont += 1
        elif (sequence[inicio] >= sequence[medio] <= sequence[fin]):
                sequence.pop(medio)
                cont += 1
                print(sequence)

        elif (sequence[inicio] <= sequence[medio] >= sequence[fin]):
            if sequence[inicio] >= sequence[fin]:
                sequence.pop(fin)
                cont += 1
                print(sequence)
            else:
                sequence.pop(medio)
                cont += 1
                print(sequence)
        elif sequence[medio] > sequence[fin]:
            sequence.pop(fin)
            print(sequence)
            cont += 1
        else:
            inicio += 1
            medio += 1
            fin += 1

        if cont > 1:
            res = False
            break
    return res

data = 'hlbeeykoqqqokyeeblh'
print(palindromo(data))
year = 1996
print(centuryFromYear(year))
array = [3, 6, -2, -5, 7, 3]
print(adjacentElementsProduct(array))
area = 5
print(shapeArea(area))
num = [6, 3]
print(makeArrayConsecutive2(num))
sequence = [1, 2, 3, 4, 99, 5, 6]
print(almostIncreasingSequence(sequence))