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
    if listas.logado['categoria'] == 'administrador':
        funcoes.comlinha(
        '[1] Barra de Pesquisa\n'
        '[2] Filtrar de produtos\n'
        '[3] Logar\n'
        '[4] Carrinho\n'
        '[5] Catalago\n'
        '[6] Área do administrador\n'
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
        
        # Login
        case 3:
            funcoes.menu_login()

        # Carrinho
        case 4:
            funcoes.carrinho()

        case 5:

            # Exibição dos produtos
            funcoes.catalogo()

        # Area do administrador
        case 6:
            if listas.logado['categoria'] == 'administrador':
                funcoes.menu_admin()

            else:
                funcoes.comlinha("ERRO! Opção invalida, tente de novo.")

            continue

        case 0:
            funcoes.comlinha("Volte sempre :)")
            print('-' * 60)

            break

        #Tratando erro
        case _:

            funcoes.comlinha("ERRO! Opção invalida, tente de novo.")

            continue
