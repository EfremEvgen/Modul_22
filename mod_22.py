array = [(int(i)) for i in input('Введите целые числа через пробел: ').split()]
print(array)
def merge_list(a,b):
    c = []
    n = len(a)
    m = len(b)

    i, j = 0, 0
    while i < n and j < m:
        if a[i] <= b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1
    c += a[i:] + b[j:]
    return c
def merge_sort(array):
    N1 = len(array) // 2
    a1 = array[:N1]
    a2 = array[N1:]

    if len(a1) > 1:
        a1 = merge_sort(a1)
    if len(a2) > 1:
        a2 = merge_sort(a2)
    return merge_list(a1, a2)

array = merge_sort(array)
print(array)

while True:
    try:
        element = int(input('Введите целое число из списка: '))
        if element not in array:
            print('Указанное число не входит в список!')
            raise Exception
        break
    except ValueError:
        print('Введите целое число!')
    except Exception:
        print('Введите положительное число!')
def binary_search(array, element, left, right):
    if left > right:
        return False
    middle = (right + left) // 2
    if array[middle] == element:
        return middle
    elif element < array[middle]:
        return binary_search(array, element, left, middle - 1)
    else:
        return binary_search(array, element, middle + 1, right)

print(binary_search(array, element, 0, len(array) - 1))