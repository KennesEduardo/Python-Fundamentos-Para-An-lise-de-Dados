'''print("Digite seu nome: \n")

s= 'Isso e uma string'

print(s)
s[0]
s[2]

s[1:]

'''

s = 'Data Science Academy'

#s[0] = 'x '  #impossivel mudar uma string.

#concatenação de string
s + ' é a melhor maneira de me preparar para o mercado de trabalho'
s = s + ' é a melhor maneira de me preparar para o mercado de trabalho'
print(s)

letra = 'w'
letra = letra * 3
print(letra)

print('\n')

print(s)
s = s.lower() #string tudo minuscula 
print(s)
s = s.upper() #string tudo maiuscula
print(s)
s = s.split("Y") #dividindo string sempre quando tem o caracter especial
print(s) 
print('\n')

#--String e funcões--
s = 'seja bem vindo ao universo do python Kennes'
cap = s.capitalize() #função que colcoa sempre primeira eltra maiuscula
print(cap)

contador = s.count('a') #conta quandas vezes aparece o caracter desejado
print(contador)

encontra = s.find('p') #encontando onde o caracter esta na string
print(encontra)

verifica = s.islower() #verifica se tem caratcter minuscula
print(verifica)

termina = s.endswith('o')
print(termina)
print('\n')
### Comparando Strings

print("Python" == "R")
print("Python" == "Python")


##LISTAS 

# Criando uma lista
listadomercado = ["ovos, farinha, leite, maças"]
print(listadomercado)

# Criando outra lista 
listadomercado2 = ["ovos", "farinha", "leite", "maças"]
print(listadomercado2)

posicao1 = listadomercado[0]
posicao2 = listadomercado2[0]
print(posicao1)
print(posicao2)

lista3 = [12, 100, "Universidade"]
print(lista3)

item1 = lista3[0]
item2 = lista3[1]
item3 = lista3[2]

print(item1, item2, item3)


#modificando ou atualiando uma lista
print(listadomercado2[2])
listadomercado2[2] = 'chocolate' 

print(listadomercado2)


#deletando um item na lista
del listadomercado2[3]
print(listadomercado2)
print('\n')

### Listas de listas (Listas aninhadas)
print('Listas de listas (Listas aninhadas)')
listas = [1,2,3], [10,15,14], [10.1, 8.7, 2.3] 
print(listas) 

a = listas[0]
print(a)
b = a[0]
print(b)

list1 = listas[1]
print(list1)
print('\n')
### Operações com listas
print('Operações com listas')
listas = [[1,2,3], [10,15,14], [10.1,8.7,2.3]]
print(listas) 

# Atribuindo à variável a, o primeiro valor da primeira lista
a = listas[0][0] #pega a primeira lista e seu primeiro item
print(a) 

b = listas[1][2]
print(b) 

c = listas[0][2] + 10
print(c) 

d = 10 

e = d  * listas[0][1]
print(e)

### Concatenando listas
print('\n Concatenando listas'  )

lista_s1 = [34, 32, 56]
lista_s2 = [21, 90, 51]

lista_total = lista_s1 + lista_s2
print(lista_total)


## Operador in verifica se tem determiando operador na lista
# Criando uma lista
lista_teste_op = [100, 2, -5, 3.4]
print("tem o elemento 10 na lista?", 10 in lista_teste_op)
print("tem o elemento 100 na lista?", 100 in lista_teste_op)

## Funções Built-in
print("\n Funções Built-in")

# Função len() retorna o comprimento da lista
len(lista_teste_op)


# Função max() retorna o valor máximo da lista
max(lista_teste_op)

# Função min() retorna o valor mínimo da lista
min(lista_teste_op)

# Criando outra lista 
listadomercado2 = ["ovos", "farinha", "leite", "maças"]

listadomercado2.append("Carne")
print(listadomercado2)

listadomercado2.append("biscoito")
print(listadomercado2)

contadorl2 = listadomercado2.count("Carne")
print(contadorl2)

# Criando uma lista vazia
a = []
print(a)
qualC= type(a)
print(qualC)

a.append(0)
print(a)
a.append(50)
print(a)

old_list = [1,2,5,10]
new_list = []

for item in old_list:
    new_list.append(item)

print(new_list)

c = [20,30]
c.append(60)
c.append(70)
print(c)
contador = c.count(20)
print(contador)

#lista de cidade 
cidades = ['Recife', 'Manaus', 'Salvador']
cidades.extend(['Fortaleza', 'Palmas'])
print (cidades)

onde = cidades.index('Salvador')
print (onde)

cidades.insert(2,'ituiutaba')
print(cidades)

cidades.reverse()
print(cidades)

x = [3, 4, 2, 1]
print(x)

#ordena a lsita
x.sort()
print(x)







