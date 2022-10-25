from functools import reduce

''' soma dois valores'''
def soma_dois_itens(item1, item2):
    return item1 + item2
''' verifica se o número é par'''
def eh_par(item):
    return item % 2 == 0

''' acumulador'''
def acumulador(item, acum):
    return acum + item

''' dois exemplos de listas'''
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista3 = [(1, 2), (3, 10), (5, 6), (7, 8), (9, 1)]

''' exemplo de map'''
nova_lista = list(map(soma_dois_itens, lista, lista2))

''' exemplo de filter'''
nova_lista2 = list(filter(eh_par, lista))

''' exemplo de zip'''
nova_lista3 = list(zip(lista, lista2))

''' exemplo de reduce'''
valor = reduce(acumulador, lista, 0)

''' exemplo de lambdas: soma 3'''
nova_lista4 = list(map(lambda item: item + 3, lista))

''' quadrado dos elementos da lista'''
nova_lista5 = list(map(lambda item: item * item, lista))

''' ordenando uma lista de tuplas'''
lista3.sort(key=lambda item: item[1])

''' list comprehentions'''
nova_lista6 = [ (numero,numero2) for numero in range(10) for numero2 in range(10,20,1) if numero % 2 == 0 and numero2 % 2 != 0 ]


# saída
print(nova_lista)
print(nova_lista2)
print(nova_lista3)
print(valor)
print(nova_lista4)
print(nova_lista5)
print(lista3)
print(nova_lista6)

# x
# x
# x
# x
# x



    