'''x=4
#se
if (x <= 1):
    print("comando executado caso a espressão 1 seja verdadeira")

elif x > 2 and x < 5:
    print("comando executado caso a expresão 1 seja falsa e expressão 2 seja verdadeira")    
#então    
else:
    print("comando executado caso a espressão 1 seja verdadeira")  
'''
# Condicional If
if 5 > 2:
    print("Python funciona!")

# Statement If...Else
if 5 < 2:
    print("Python funciona!")
else:
    print("Algo está errado!")    

print(6 > 3)
print(3 > 7)
print(4 < 8)
print(4 >= 4)

if 5 == 5:
    print("Testando Python!")

if True:
    print('Parece que Python funciona!')
##
print("\n ### Condicionais Aninhados")   

idade = 18
if idade > 17:
    print("Você pode dirigir!")

Nome = "Bob"
if idade > 13:
    if Nome == "Bob":
        print("Ok Bob, você está autorizado a entrar!")
    else:
        print("Desculpe, mas você não pode entrar!")    

idade = 13
Nome = "Bob"
if idade >= 13 and Nome == "Bob":
    print("Ok Bob, você está autorizado a entrar!")

#no caso do or (ou) basta apenas uma das condicão ser verdadeira para entrar
idade = 12
Nome = "Bob"
if (idade >= 13) or (Nome == "Bob"):
    print("\nok Bob, você está autorizado a entrar!")       
else:
    print("desculpe voce não pode entrar")         

### Elif
dia = "Terça"
if dia == "Segunda":
    print("Hoje fará sol!")
else:
    print("Hoje vai chover!")    

if dia == "Segunda":
    print("Hoje fará sol!")
elif dia == "Terça":
    print("Hoje vai chover!")
else:
    print("Sem previsão do tempo para o dia selecionado")



### Operadores Lógicos  
print("\nOperadores Lógicos ")
idade = 18
nome = "Bob"
if idade > 17:
    print("Você pode dirigir!")


idade = 18
if idade > 17 and nome == "Bob":
    print("Autorizado!")    

# Usando mais de uma condição na cláusula if 

disciplina = input('Digite o nome da disciplina: ')
nota_final = input('Digite a nota final (entre 0 e 100): ')

if disciplina == 'Geografia' and nota_final >= '70':
    print('Você foi aprovado!')
else:
    print('Lamento, acho que você precisa estudar mais!')    


# Usando mais de uma condição na cláusula if e introduzindo Placeholders
disciplina = input('Digite o nome da disciplina: ')
nota_final = input('Digite a nota final (entre 0 e 100): ')
semestre = input('Digite o semestre (1 a 4): ')

if disciplina == 'Geografia' and nota_final >= '50' and int(semestre) != 1:
    print('Você foi aprovado em %s com média final %r!' %(disciplina, nota_final))
else:
    print('Lamento, acho que você precisa estudar mais!')    