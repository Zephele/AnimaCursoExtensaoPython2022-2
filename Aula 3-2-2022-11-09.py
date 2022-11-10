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
print(imposto)