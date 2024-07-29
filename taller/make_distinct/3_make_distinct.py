from collections import defaultdict

n = int(input())
numbers = list(map(int, input().split()))

list_numbers = sorted(numbers)
before_numbers = list(list_numbers)

def make_distinct():
    numero_alto = 0
    viewer = defaultdict()
    for i in range(len(list_numbers)-1):
        if abs(list_numbers[i] - list_numbers[i+1]) > 1:
            numero_alto = list_numbers[i] + 1
            break
    numero_bajo = list_numbers[0] - 1
    for index, number in enumerate(list_numbers):
        if (index+1 == len(list_numbers)): break
        if number != list_numbers[index + 1]: 
            viewer[number] = 1
            continue
        else:
            if(numero_alto > abs(numero_bajo)):
                list_numbers[index] = numero_bajo
                if list_numbers[index] - list_numbers[index-1] > 1: numero_bajo = list_numbers[index]-1 
                else: numero_bajo -= 1
            else:
                for i in range(index, len(list_numbers)-1):
                    if abs(list_numbers[i] - list_numbers[i+1]) > 1:
                        numero_alto = list_numbers[i] + 1
                else:
                    numero_alto = list_numbers[len(list_numbers)-1] + 1
                    list_numbers[index] = numero_alto
                    numero_alto += numero_alto
            viewer[number] = 1

make_distinct()
list_numbers = sorted(list_numbers)

def calculate_operations(arr_original, arr_distinct):
    operations = 0
    # Comparar y calcular las diferencias
    for original, distinct in zip(arr_original, arr_distinct):
        operations += abs(distinct - original)

    return operations

print(calculate_operations(before_numbers,list_numbers))
