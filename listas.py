import json

dados_usua= open('usuarios.json', 'r', encoding='utf-8')
usuarios = json.load(dados_usua)
dados_usua.close()

dados_estoque= open('estoque.json', 'r', encoding='utf-8')
estoque = json.load(dados_estoque)
dados_estoque.close()

dados_relatorio= open('relatorio.json', 'r', encoding='utf-8')
relatorio = json.load(dados_relatorio)
dados_relatorio.close()

pesquisa = []

logado = {"usuario":"Visitante", "categoria": "cliente"}

carrinho = []

dados_compra = []
