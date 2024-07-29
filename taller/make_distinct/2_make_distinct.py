n = int(input())
numbers = list(map(int, input().split()))

list_numbers = sorted(numbers)
before_numbers = list(list_numbers)

def make_distinct():
    # Inicializa el número alto y bajo con el último y primer elemento ajustados
    numero_bajo = list_numbers[0] - 1
    numero_alto = list_numbers[0] + 1
    temp = list_numbers[0]
    for i in range(len(list_numbers) - 1):
        if list_numbers[i] == list_numbers[i + 1]:
            # Calcular número bajo
            try:
                if list_numbers[i] - temp > 1: numero_bajo = temp -1
            except: pass
            
            # Calcular número alto
            while numero_alto in list_numbers:
                numero_alto += 1

            temp = list_numbers[i]
            # Decidir si asignar número bajo o alto
            if abs(list_numbers[i]-numero_bajo) <= abs(numero_alto-list_numbers[i]):
                list_numbers[i] = numero_bajo
            else:
                list_numbers[i] = numero_alto

make_distinct()
list_numbers = sorted(list_numbers)

def calculate_operations(arr_original, arr_distinct):
    operations = 0
    # Comparar y calcular las diferencias
    for original, distinct in zip(arr_original, arr_distinct):
        operations += abs(distinct - original)

    return operations

print(before_numbers,list_numbers)
print(calculate_operations(before_numbers,list_numbers))