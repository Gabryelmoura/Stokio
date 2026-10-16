import mysql.connector as my
import pandas as pd
import os
import platform
from time import sleep

"""
db = {
    host: "127.0.0.1",
    user: "Gabryel",
    passwd: "G030807m.",
    database: "estoque"
}

cursor = db.cursor()
"""

dict_produtos = {
    "ID": [],
    "list_nome": [],
    "list_quantidade": [],
    "list_categoria": []
}

def limparTerminal():
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')

def menu():
    print("""
    ================ MENU ==================
    [1]. Cadastrar um produto
    [2]. Comprar um produto
    [3]. Visualizar os produtos em estoque
    [4]. Gerar nota fiscal
    [5]. Sair
    ========================================
    """)

    opc = int(input("Informe qual das seguntes opções você deseja: "))
    return opc

def cadastrarProduto():
    count = 0
    nome = ""
    quantidade = 0
    categoria = ""

    print("""
    ============== CADASTRO DE PRODUTOS ==============
    [1]. Adicionar novo produto
    [2]. Atualizar quantidade de determinado produto
    ==================================================
    """)

    opc = int(input("Informe qual das opções acima você deseja acessar: "))

    if opc == 1:
        limparTerminal()
        print("""================== ADICIONAR NOVO PRODUTO =====================""")
        nome = str(input("Informe o nome do produto: "))
        quantidade = int(input("Informe a quantidade do produto: "))
        categoria = str(input("Informe a categoria do produto: "))
        
        if nome in dict_produtos["list_nome"]:
            print("Produto Já cadastrado em estoque.")
        else:
            if nome != "" and len(nome) >= 3 and quantidade > 0 and quantidade <= 100 and quantidade != '' and categoria != "" and len(categoria) >= 4:
                id_produtos = len(dict_produtos["list_nome"]) + 1
                dict_produtos["ID"].append(id_produtos)
                dict_produtos["list_nome"].append(nome)
                dict_produtos["list_quantidade"].append(quantidade)
                dict_produtos["list_categoria"].append(categoria)
    else:
        limparTerminal()
        print("""================== ATUALIZAR QUANTIDADE PRODUTO ====================""")
        identificador = str(input("Informe o nome do produto que deseja atualizar a quantidade em estoque: "))
        count = 0
        produtoSelecionado = None
        while count < len(dict_produtos["list_nome"]):
            if identificador == dict_produtos["list_nome"][count]:
                print("Produto Encontrado com Sucesso!")
                produtoSelecionado = count
                count += 1
            else:
                count += 1

        if produtoSelecionado != None:
            quantidadeAdicionar = int(input("Informe a quantidade que deseja Adicionar: "))

            if quantidadeAdicionar <= 900 or (dict_produtos["list_quantidade"][produtoSelecionado] + quantidadeAdicionar) <= 1000:
                dict_produtos["list_quantidade"][produtoSelecionado] += quantidadeAdicionar
            else:
                diferenca = 1000 - dict_produtos["list_quantidade"][produtoSelecionado]
                print(f'Valor máximo para adicionar ao produto desejado: {diferenca}')
                print('ERRO: A quantidade máxima que um produto pode chegar no estoque é 1000.')
        else:
            print('ERRO: Produto Não Encontrado.')

def comprarProduto():
    count = 0
    
    print("""================== COMPRAR PRODUTOS =====================""")

    identificador = str(input("Informe o nome do produto: "))
    produtoSelecionado = None
    while count < len(dict_produtos["list_nome"]):
        if identificador == dict_produtos["list_nome"][count]:
            print("Produto Selecionado")
            produtoSelecionado = count
            count += 1
        else:
            count += 1

    if produtoSelecionado != None:
        quantidadeComprar = int(input("Informe a quantidade que deseja comprar: "))
        if quantidadeComprar > dict_produtos["list_quantidade"][produtoSelecionado]:
            print("ERRO: Informe uma quantidade menor ou igual a que esta disponivél para o produto no estoque.")
        else:
            dict_produtos["list_quantidade"][produtoSelecionado] -= quantidadeComprar

def visualizarProdutos():
    count = 0
    print("""================= ESTOQUE =================""")
    if len(dict_produtos["list_nome"]) > 0:
        while count < len(dict_produtos["list_nome"]):
            print(f'ID: {dict_produtos["ID"][count]} Nome: {dict_produtos["list_nome"][count]} Quantidade: {dict_produtos["list_quantidade"][count]} Categoria: {dict_produtos["list_categoria"][count]}')
            count += 1
    else:
        print("Nenhum produto em estoque.")

def notaFiscal():
    print(f"""================== NOTA FISCAL =====================""", '\n')

while True:
    opc_escolhida = menu()
    limparTerminal()
    
    if opc_escolhida == 1:
        cadastrarProduto()
        sleep(1.5)
        limparTerminal()
    elif opc_escolhida == 2:
        comprarProduto()
        sleep(2)
        limparTerminal()
    elif opc_escolhida == 3:
        visualizarProdutos()
        sleep(3)
        limparTerminal()
    elif opc_escolhida == 4:
        notaFiscal()
        sleep(5)
        limparTerminal()
    else:
        break
