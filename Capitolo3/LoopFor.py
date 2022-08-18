# Criando uma tupla e imprimindo cada um dos valores
tp = (2,3,4)
for i in tp:
    print(i)

# Criando uma lista e imprimindo cada um dos valores
ListaDoMercado = ["Leite", "Frutas", "Carne"]
for i in ListaDoMercado:
    print(i)

# Imprimindo os valores no intervalo entre 0 e 5 (exclusive)
for contador in range(0,5):
    print(contador)

# Imprimindo na tela os números pares da lista de números
lista = [1,2,3,4,5,6,7,8,9,10]
for num in lista:
    if num % 2 == 0:
        print ("\n",num) 

print('\n')
# Listando os números no intervalo entre 0 e 101, com incremento em 2
for i in range(0,101,2):  
    print(i)  

# Strings também são sequências
for caracter in 'Python é uma linguagem de programação divertida!':
    print (caracter)                     