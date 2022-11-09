print("Inicio da aula 3 (09/11/2022)")

contador = 1
print(contador)
contador = contador+1 #contador += 1
print(contador)
contador += 1
print(contador)

while( contador <= 10):
  print(contador)
  contador =  contador+1 
fruta = "morango"
print(fruta)

fruta1 = "morango" #começa do 0..
fruta2 = "laranja"
fruta3 = "pêra"

#Lista
frutas = ["morango", "laranja", "pêra"]

#Quero exibir apenas a 3a. fruta (pêra)
print(frutas[2])

print(len(frutas)) # length = tamanho

#quero incluir uma fruta nova
frutas.append("manga")

print(len(frutas)) # length = tamanho
print(frutas)

print(frutas[0])
print(frutas[1])
print(frutas[2])
print(frutas[3])
#print(frutas[4])

print("Exemplo das frutas com while..")
frutas.append("uva")

i=0 #(i de index)
while(i<len(frutas)):
  print(frutas[i])
  i = i + 1

print("Exemplo das frutas com FOR")

for fruta in frutas: 
  print(fruta)
