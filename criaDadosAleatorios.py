# -*- coding: utf-8 -*-
"""
Módulo 4
Cria dados aleatórios para a tabela PRODUTO
Comando para conferência: select * from s_ihc."PRODUTO";
"""
from faker import Faker
import psycopg2

conn = psycopg2.connect(database="ihc", user="czf", password="senha123", host="localhost", port="5434")
print("Conexão aberta com sucesso!")
cursor = conn.cursor()
fake = Faker('pt_BR')
n = 10
for i in range(n):
    codigo = i + 10
    nome = 'Produto_' + str(i + 1)
    preco = fake.pyfloat(left_digits=3, right_digits=2, positive=True, min_value=5, max_value=1000)
    print(preco)
    print(nome)
    comandoSQL = """ INSERT INTO s_ihc."PRODUTO" ("CODIGO", "NOME", "PRECO") VALUES (%s, %s, %s)"""
    registro = (codigo, nome, preco)
    cursor.execute(comandoSQL, registro)

conn.commit()
print("Inserção realizada com sucesso!")
conn.close()
