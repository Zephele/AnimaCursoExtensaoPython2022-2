#criação de funções

preco1 = 1999.90

#Calcular 5% de imposto, guardar na variavel e exibir na tela
imposto = preco1 * 0.05
print(imposto)

preco2 = 100
imposto2 = preco2 *0.05
print(imposto2)

#criar uma funcao calcular_imposto() que calcularr um imposto de 5% e retorna a quem pediu...
def calcular_imposto(preco_produto):
  imposto = preco_produto * 0.05
  return imposto

#Aqui é o uso... aqui é imposto a calcular
preco = 299
imposto = calcular_imposto(preco)
print(f"Esse aqui é com a funcaao (7%): {imposto}")

print(preco) #????
preco_produto = 100
print(preco_produto) #????

#agora calcular imposto aa aliquota agora é 7%

valores = [1.99, 24.50, 78.27, 1515.5]
# se eu quiser calcular o imposto destes quatro valores ... e exibir na tela assim: "O impostos de .... é ...." (1o. preco, 2o. imposto)
for valor in valores:
  print(f"O imposto de {valor} é {calcular_imposto(valor)}")

#Declarar um funcao calcula_imposto_aliquota que recebe dois parametro: o preco do produto e a aliquota de imposto a ser aplicada e retorna o imposto calculado. Se a aliquota nao for informada, utilize 7% como padrao.
def calcular_imposto_aliquota(valor, aliquota=7):
  imposto = valor * aliquota / 100
  return imposto

for valor in valores:
  print(f"O imposto de {valor} é {calcular_imposto_aliquota(valor, 10)}")

