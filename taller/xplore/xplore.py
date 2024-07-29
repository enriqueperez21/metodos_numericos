import json

# Datos de entrada
# Paso 1: Leer el número de entradas y los datos JSON
N = int(input())
entries = []
for _ in range(N): entries.append(input())

# Procesar los datos
author_citations = {}

for entry in entries:
    data = json.loads(entry)
    citing_paper_count = data['citing_paper_count']
    for author in data['authors']['authors']:
        author_citations[author['full_name']] = []

for entry in entries:
    data = json.loads(entry)
    citing_paper_count = data['citing_paper_count']
    for author in data['authors']['authors']:
        author_name = author['full_name']
        author_citations[author_name].append(citing_paper_count)

# Calcular el h-index de cada autor
def calculate_h_index(citations):
    citations.sort(reverse=True)
    h_index = 0
    for index, n_citations in enumerate(citations):
        # Compara que la cantidad de articulos mínimo tenga
        # la misma cantidad de citaciones
        if index + 1 <= n_citations:
            h_index = index + 1
        else:
            break
    return h_index

author_h_index = {}
for author in author_citations: author_h_index[author] = calculate_h_index(author_citations[author])

# Paso 4: Ordenar los autores por h-index y por nombre alfabético en caso de empate
sorted_authors = sorted(author_h_index.items(), key=lambda authors: (-authors[1],authors[0]))
#Key, lambda authors, retorna un array, [author, value], primero es por el value, entonces
# ponemos authors[1], pero los pone de menor a mayor, por eso agregamos el - al inicio, y
# si tienen el mismo value, osea el h_index, usa el valor de authors[0], que son los nombres.

# Paso 5: Imprimir los resultados
for author, h_index in sorted_authors:
    print(f"{author} {h_index}")