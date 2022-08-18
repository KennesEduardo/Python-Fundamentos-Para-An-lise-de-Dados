# Isso é uma lista
'''estudantes_lst = ["Mateus", 24, "Fernanda", 22, "Tamires", 26, "Cristiano", 25] 
print(estudantes_lst)

# Isso é um dicionário
estudantes_dict = {"Mateus":24, "Fernanda":22, "Tamires":26, "Cristiano":25}
print(estudantes_dict)


print("A idade do Matheus é: ", estudantes_dict["Mateus"])

estudantes_dict["Pedro"] = 23 #adicionando um elemento ao dicionarios 

print(estudantes_dict)

estudantes_dict.clear()
print(estudantes_dict)'''

#del estudantes_dict #comando para deletar o dicionario
#print(estudantes_dict)


estudantes = {"Mateus":24, "Fernanda":22, "Tamires":26, "Cristiano":25}
print("\n", estudantes)

tamanho = len(estudantes)
print("O tamanaho do dicionario é: ",tamanho)

valores = estudantes.values()
print("Valores é igual a: ", valores)

chaves = estudantes.keys()
print("As chaves são composata por ", chaves)

itens = estudantes.items()
print("itens é igual a: ", itens)

estudantes2 = {"Maria":27, "Erika":28, "Milton":26}
print("\n",estudantes2)

#fazendo update em uma tupla
estudantes.update(estudantes2)
print(estudantes)

dic1 = {}
print(dic1)

dic1['key_one'] = 2
print(dic1)

dic1['key_duas'] = 1
print(dic1)

dic1[10] = 5
print(dic1)

dic1[8.2] = 'Python'
print(dic1)

dic1['Teste'] = 5
print(dic1)

dict1 = {}
print(dict1)

dict1["teste"] = 10
dict1['key'] = "teste"
print(dict1)


dict2 = {}
dict2["key1"] = "Big Data"
dict2["key2"] = 10
dict2["key3"] = 5.6
print(dict2)

a = dict2["key1"]
b = dict2["key2"]
c = dict2["key3"]
print("As variaveis são iguas a ", a,b,c)

# Dicionário de listas
dict3 = {'key1':1230,'key2':[22,453,73.4],'key3':['leite','maça','batata']}
print("\n", dict3)

print("os elementos da key 2 é: ",dict3['key2'])

# Acessando um item da lista, dentro do dicionário
valor1 = dict3['key3'][0].upper()
print("valor na posição 0 maiuscula é igual a:", valor1)

# Operações com itens da lista, dentro do dicionário
var1 = dict3['key2'][0] - 2
print(var1)

# Duas operações no mesmo comando, para atualizar um item dentro da lista
dict3['key2'][0] -= 2
print(dict3)

# Criando dicionários aninhados
dict_aninhado = {'key1':{'key2_aninhada':{'key3_aninhada':'Dict aninhado em Python'}}}
print(dict_aninhado)

# Verificando o comprimento da tupla
valor2 = dict_aninhado['key1']['key2_aninhada']['key3_aninhada']
print(valor2)
