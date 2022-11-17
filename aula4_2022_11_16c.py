#1o. passo: importar a biblioteca sqlite3
import sqlite3

#PASSOS 2 e 3 VIRARÃO funcao conectar()
def conectar():
  conexao = sqlite3.connect("dc_universe.db")

  cursor = conexao.cursor()
  return conexao, cursor