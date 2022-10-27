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


#Estrutura condicional - o famoso "SE" (if)
#Se a pessoa for maior de idade, mostre "Voce é maior de idade, ótimo! Já pode beber ou dirigir"
if idade >= 18: 
  print ("Voce é maior de idade, ótimo! Já pode beber ou dirigir ") 

else:
  print("vai la beber na sua mamadeira")
print("\n Pergunta valendo 1 milhao de reais. Qual numero representa O amor da vida do carlos")
print("\n 1 - Ribeiro")
print("\n 2 - Nadya")
print("\n 3 - sarah")
Resposta = int(input("\n Qual é a Resposta certa: "))
if Resposta <= 1: 
  print (" Resposta Certa ") 

if Resposta > 1:
 print (" Resposta errada ")


#E se eu quiser perguntar o genero (M = Maculino e F = Feminino)
#Mostre (...e você tambem precisa/precisou prestar o serviço militar obrigatorio)
Genero = input("\n Qual o seu Genero M ou F: ")
if (Genero == "M"):
  print("\n Parabens O Serviço obrigatorio te aguarda rsrs")
else: 
  print("\n Ninguem liga rsrs")
  