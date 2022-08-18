# Exercício 4 - Crie uma tupla com os seguintes elementos: 1, 2, 2, 3, 4, 4, 4, 5 e depois utilize a função count do 
# objeto tupla para verificar quantas vezes o número 4 aparece na tupla

tupla1 = (1,2,2,3,4,4,4,5)
print(tupla1)

verifica = tupla1.count(4)
print(verifica)


# Exercício 5 - Crie um dicionário vazio e imprima na tela
dic = {}
print(dic)
# Exercício 6 - Crie um dicionário com 3 chaves e 3 valores e imprima na tela
dic = {'chave1' :1, 'chave2' : 2, 'chave3' : 3}
print(dic)
# Exercício 7 - Adicione mais um elemento ao dicionário criado no exercício anterior e imprima na tela
dic['chave4'] = 4
print(dic)

# Exercício 8 - Crie um dicionário com 3 chaves e 3 valores. Um dos valores deve ser uma lista de 2 elementos numéricos. .
# Imprima o dicionário na tela.
dic = {'chave1' :1, 'chave2' : 2, 'chave3' :[2,3]}
print(dic)

# Exercício 9 - Crie uma lista de 4 elementos. O primeiro elemento deve ser uma string, 
# o segundo uma tupla de 2 elementos, o terceiro um dcionário com 2 chaves e 2 valores e 
# o quarto elemento um valor do tipo float.
# Imprima a lista na tela.
lista =['Kennes Eduardo ', (50, 55), {'chave1': 1, 'chave2': 2},  2.254]
print(lista)



# Exercício 10 - Considere a string abaixo. Imprima na tela apenas os caracteres da posição 1 a 18.
#frase = 'Cientista de Dados é o profissional mais sexy do século XXI'

frase = 'Cientista de Dados é o profissional mais sexy do século XXI'
nova_frase = frase[0:18]
print(nova_frase)