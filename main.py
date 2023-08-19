# -*- coding: utf-8 -*-
"""
Módulo 4
Programa principal
"""

import tkinter as tk
import aplicacaoCRUD

if __name__ == '__main__':
    janela = tk.Tk()
    principal = aplicacaoCRUD.PrincipalDB(janela)
    janela.title("Bem-vindo ao Cadastro do Produtos")
    janela.geometry("800x600+10+10")
    janela.mainloop()
