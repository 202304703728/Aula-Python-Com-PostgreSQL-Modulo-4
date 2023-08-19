# -*- coding: utf-8 -*-
"""
Módulo 4
Cria a tabela PRODUTO
Comando para conferência:

SELECT table_name
FROM information_schema.tables
WHERE table_schema='s_ihc'
AND table_type='BASE TABLE';

"""
import psycopg2

conn = psycopg2.connect(database="ihc", user="czf", password="senha123", host="localhost", port="5434")
print("Conexão com o banco de dados feita com sucesso!")
cur = conn.cursor()
cur.execute('''CREATE TABLE PRODUTO(CODIGO INT PRIMARY KEY NOT NULL,Nome TEXT NOT NULL,PRECO REAL NOT NULL);''')
print("Tabela criada com sucesso!")
conn.commit()
conn.close()
