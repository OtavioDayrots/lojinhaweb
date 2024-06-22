# Importando listas e funções
import listas
import funcoes

# Controles
encontrado_pesquisa = False
encontrado_carrinho = False
encontrado_tipo = False

# Programa principal
while True:

    # Menu
    funcoes.comlinha('Menu Principal'.center(60))
    if len(listas.logado) == 0:
        funcoes.comlinha(
            '[1] Barra de Pesquisa\n'
            '[2] Filtrar de produtos\n'
            '[3] Logar\n'
            '[4] Carrinho\n'
            '[5] Catalago\n'
            '[0] Sair'
    )
    else:
        if listas.logado[0]['categoria'] == 'administrador':
            funcoes.comlinha(
            '[1] Barra de Pesquisa\n'
            '[2] Filtrar de produtos\n'
            '[3] Logar\n'
            '[4] Carrinho\n'
            '[5] Catalago\n'
            '[6] Administrador\n'
            '[0] Sair'
            )

        else:
            funcoes.comlinha(
            '[1] Barra de Pesquisa\n'
            '[2] Filtrar de produtos\n'
            '[3] Logar\n'
            '[4] Carrinho\n'
            '[5] Catalago\n'
            '[0] Sair'
    )

        
    opcao = funcoes.recebe_comlinha("Escolha uma ação: ")

    # Seguindo as opções
    match opcao:

        # Barra de pesquisa
        case 1:

            # Recebendo busca
            encontrado_pesquisa = funcoes.pesquisas('nome')

            # Produto não existe no estoque
            if encontrado_pesquisa == False:
                funcoes.comlinha('Produto não encontrado, voltando ao menu principal')

                continue

            # Adiciona o produto ao carrinho ou pesquisa de novo
            funcoes.menu_pesquisa()

        # Filtro de produto
        case 2:

            # Recebendo busca
            encontrado_tipo = funcoes.pesquisas('tipo')

            # Produto não existe no estoque
            if encontrado_tipo == False:
                funcoes.comlinha('Produto não encontrado, voltando ao menu principal')

                continue

            # Adiciona o produto ao carrinho ou pesquisa de novo    
            funcoes.menu_pesquisa()
        
        #Login
        case 3:
            funcoes.menu_login()
        
        case 4:
            funcoes.carrinho()

        case 6:
            funcoes.menu_admin()

        #Tratando erro
        case _:

            funcoes.comlinha("ERRO! Opção invalida, tente de novo.")

            continue

    # Exibição dos produtos
    print(listas.estoque[0])
    funcoes.catalogo()
  
