# comando input(): quero permitir que o usuario digite algo...
nome = input("Digite seu nome: ")

#comando de saida... exibir na tela
print (nome)
print (f"Boa noite, seu nome é {nome}")

idade = int(input("Qual a sua idade: "))
print (f"Sua idade é {idade}")

#e se eu quisesse mostrar o DOBRO da idade informada?

dobro = idade * 2
print ("O dobro da idade informada é {}".format (dobro))