#Pede o nome do aluno e sua nota (de 0 a 10) e, se ele tirou nota 10, mostra "{Nome} Você é bichão, mesmo..."
nome = input("Informe seu nome: ")
Nota = float(input("Digite sua nota de 0 a 10 sobre a aula: "))

if (Nota == 10):
  print(f"{Nota}, você é o bichão, mesmo...")

elif (Nota >= 6 and Nota < 10):
  print("Carlos aprova")
else:
  print("Incopetente rsrs parece o kaua rsrs")