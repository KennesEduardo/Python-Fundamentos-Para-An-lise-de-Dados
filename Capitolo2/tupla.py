# Criando uma tupla
tupla1 = ("Geografia", 23, "Elefantes")
print(tupla1)

'''# Tuplas não suportam append()
tupla1.append("Chocolate")   

# Tuplas não suportam delete de um item específico
del tupla1["Gatos"]'''

# Tuplas podem ter um único item
tupla1 = ("Chocolate")
print(tupla1)

tupla1 = ("Geografia", 23, "Elefantes")
print(tupla1)

posicao0 = tupla1[0]
print(posicao0)

comprimento = len(tupla1)
print(comprimento)

# Slicing, da mesma forma que se faz com listas
slicing = tupla1[1:]
print(slicing)

#verificando indece
indece = tupla1.index('Elefantes')
print(indece)

#duplas podem ser deletadas 
del tupla1


# Criando uma tupla
t2 = ('A', 'B', 'C')
print("\n",t2)


# Usando a função list() para converter uma tupla para lista
lista_t2 = list(t2)
print(lista_t2)

lista_t2.append('D')

# Usando a função tuple() para converter uma lista para tupla
t2 = tuple(lista_t2)

print("\n",t2)
