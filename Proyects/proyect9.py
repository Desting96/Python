# Complete the bigSorting function below.
def bigSorting(unsorted):

    sort = sorted(unsorted, key=lambda x: int(x))
    return sort

if __name__ == '__main__':

    n = int(input())

    unsorted = []

    for _ in range(n):
        unsorted_item = input()
        unsorted.append(unsorted_item)

    result = bigSorting(unsorted)
    print('\n'.join(result))
