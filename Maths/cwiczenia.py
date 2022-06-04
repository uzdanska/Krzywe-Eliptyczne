lista = [(lambda x: x)(x) for x in range(1,53)]
lista.sort()
print(lista)
def wszystkieElementy(lista):
    for i in range(len(lista)):
        if lista[i] == i + 1:
            pass
    return 'PRAWDA'

print(wszystkieElementy(lista))