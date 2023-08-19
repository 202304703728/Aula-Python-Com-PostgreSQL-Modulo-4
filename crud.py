# -*- coding: utf-8 -*-
"""
Módulo 4
Programa responsável pelas operações CRUD
"""

import psycopg2


# Classe com os métodos para realizar as operações de interação com o BD
class AppBD:
    def __init__(self):
        print('Método construtor')

    # Conecta com a tabela PRODUTO
    def abrirConexao(self):
        try:
            self.connection = psycopg2.connect(database="ihc", user="czf", password="senha123", host="localhost",
                                               port="5434")

        except (Exception, psycopg2.Error) as error:
            if self.connection:
                print("Falha ao conectar com o banco de dados: ", error)

    # Seleciona os produtos cadastrados na tabela PRODUTO
    def selecionarDados(self):
        try:
            self.abrirConexao()
            cursor = self.connection.cursor()
            print("Selecionando produtos, aguarde...")
            sql_select_query = """SELECT * FROM s_ihc."PRODUTO" """
            cursor.execute(sql_select_query)
            registros = cursor.fetchall()
            print(registros)

        except (Exception, psycopg2.Error) as error:
            print("Erro na seleção de dados: ", error)

        finally:
            if self.connection:
                cursor.close()
                self.connection.close()
                print("Conexão com o banco de dados encerrada.")

        return registros

    # Cadastra um produto na tabela PRODUTO
    def inserirDados(self, codigo, nome, preco):
        try:
            self.abrirConexao()
            cursor = self.connection.cursor()
            postgres_insert_query = """INSERT INTO s_ihc."PRODUTO" ("CODIGO", "NOME", "PRECO") VALUES (%s, %s, %s)"""
            record_to_insert = (codigo, nome, preco)
            cursor.execute(postgres_insert_query, record_to_insert)
            self.connection.commit()
            count = cursor.rowcount
            print(count, "Produto cadastrado com sucesso!")

        except (Exception, psycopg2.Error) as error:
            if self.connection:
                print("Erro ao cadastrar o produto: ", error)

        finally:
            if self.connection:
                cursor.close()
                self.connection.close()
                print("Conexão com o banco de dados encerrada.")

    # Atualiza dados do produto na tabela PRODUTO
    def atualizarDados(self, codigo, nome, preco):
        try:
            self.abrirConexao()
            cursor = self.connection.cursor()
            print("Localizando o produto, aguarde...")
            sql_select_query = """select * from s_ihc."PRODUTO" where "CODIGO" = %s"""
            cursor.execute(sql_select_query, (codigo,))
            record = cursor.fetchone()
            print(record)
            # Atualizando o registro do produto
            sql_update_query = """update s_ihc."PRODUTO" set "NOME" = %s, "PRECO" = %s where "CODIGO" = %s"""
            cursor.execute(sql_update_query, (nome, codigo, preco))
            self.connection.commit()
            count = cursor.rowcount
            print(count, "Produto atualizado com sucesso!")
            print("Dados do produto após a atualização: ")
            # Não repeti a linha que define sql_select_query porque é igual à anterior
            cursor.execute(sql_select_query, (codigo,))
            record = cursor.fetchone()
            print(record)

        except (Exception, psycopg2.Error) as error:
            print("Erro ao atualizar os dados do produto: ", error)

        finally:
            if self.connection:
                cursor.close()
                self.connection.close()
                print("Conexão com o banco de dados encerrada.")

    # Exclui um produto da tabela PRODUTO
    def excluirDados(self, codigo):
        try:
            self.abrirConexao()
            cursor = self.connection.cursor()
            # Exclui o produto
            sql_delete_query = """delete from s_ihc."PRODUTO" where "CODIGO" = %s"""
            cursor.execute(sql_delete_query, (codigo,))
            self.connection.commit()
            count = cursor.rowcount
            print(count, "Produto excluído com sucesso!")

        except (Exception, psycopg2.Error) as error:
            print("Erro ao excluir o produto: ", error)

        finally:
            if self.connection:
                cursor.close()
                self.connection.close()
                print("Conexão com o banco de dados encerrada.")
