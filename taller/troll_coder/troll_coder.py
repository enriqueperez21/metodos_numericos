import sys

n = int(input())

solucion_actual = [0] * n
print("Q", *solucion_actual)
sys.stdout.flush()
respuesta_actual = int(input())

for i in range(n):
    solucion_actual[i] = 1 
    print("Q", *solucion_actual)
    sys.stdout.flush() 
    nueva_respuesta = int(input())
    
    if nueva_respuesta <= respuesta_actual:
        solucion_actual[i] = 0
    else:
        respuesta_actual = nueva_respuesta 

print("A", *solucion_actual)
sys.stdout.flush()