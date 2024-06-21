import listas

# Imprimindo todos os produtos
def catalogo():
    for produto in range(20):
        print('-' * 60)
        print(f"{produto:<4}{listas.estoque[produto]['nome']:<35}", end=' ')
        print(f"{'R$'} {listas.estoque[produto]['preço']:>8.2f}")

# Prints com linhas
def comlinha(a):
    print('-' * 60)
    print(a)

# Inputs com linhas
def recebe_comlinha(a):
    print('-' * 60)
    valor = int(input(a))

    return valor

# Barra de pesquisa
def pesquisas(chave):
            
            # Redefinindo tudo
            cont_pesquisa = 0
            encontrado_pesquisa = False
            listas.pesquisa.clear()

            # Recebendo busca
            print('-' * 60)
            pesquisa = input("Informe o produto que deseja: ").upper()
            tamanho_pesquisa = len(pesquisa)

            comlinha('Resultados da Pesquisa:'.center(60))

            # Encontrando produto na lista
            for produto in listas.estoque:

                # Produto encontrado_pesquisa
                if pesquisa == produto[chave][:tamanho_pesquisa].upper():

                    # Preparando caso de erro
                    encontrado_pesquisa = True

                    # Armazenando produto
                    listas.pesquisa.append(produto.copy())

                    # Exibindo produto
                    comlinha(
                    f"{cont_pesquisa} " 
                    f"{listas.pesquisa[cont_pesquisa]['nome']} " 
                    f"R$ {listas.pesquisa[cont_pesquisa]['preço']:.2f} " 
                    f"tipo {listas.pesquisa[cont_pesquisa]['tipo']}, "
                    f"tem em estoque {listas.pesquisa[cont_pesquisa]['qtd_estoque']}"
                    )
                    cont_pesquisa += 1
                
            # Produto não existe no estoque
            if encontrado_pesquisa == False:
                return False

            else:
                 return True
            
# Adiciona o produto ao carrinho ou pesquisa de novo
def menu_pesquisa():
     
     encontrado_carrinho = False
     
     while True:
        # Menu de pesquisa
        comlinha('Opções da Pesquisa'.center(60))
        comlinha(
            '[1] Selecionar um produto \n'
            '[2] Pesquisar novamente \n'
            '[0] Voltar ao menu principal'
            )
        
        opcao_pesquisa = recebe_comlinha('Escolha uma ação: ')

        # Seguindo opções
        match opcao_pesquisa:

            # Selecionando produto
            case 1:

                escolha_produto = recebe_comlinha("Informe o número do produto: ")

                if escolha_produto >= 0:

                    print('-' * 60)
                    ad_carrinho = input(f"Você deseja adicionar {listas.pesquisa[escolha_produto]['nome']} ao carrinho?[S/N]: ").upper()

                    if ad_carrinho == 'S':

                        qtd_ad_carrinho = recebe_comlinha("Informe a quantidade que dejesa adicionar ao carrinho: ")

                        if qtd_ad_carrinho > 0:

                            # procurando se o produto ja exite no carrinho
                            for produto_c in range(len(listas.carrinho)):
                                
                                if listas.pesquisa[escolha_produto]['nome'] == listas.carrinho[produto_c]['nome']:

                                    listas.carrinho[produto_c]['qtd_estoque'] += qtd_ad_carrinho

                                    encontrado_carrinho = True

                                    # Encontrando produto na lista
                                    for produto_e in range(len(listas.estoque)):

                                        # Produto encontrado
                                        if listas.carrinho[produto_c]['nome'] == listas.estoque[produto_e]['nome']:

                                            # quantidade em estoque
                                            if qtd_ad_carrinho <= listas.estoque[produto_e]['qtd_estoque']:
                                                listas.estoque[produto_e]['qtd_estoque'] -= qtd_ad_carrinho
                                                
                                                comlinha('Produto adicionado ao carrinho')
                                            
                                            # Falta em estoque
                                            else:
                                                comlinha('Quantidade invalida, exede o que temos em estoque. Por favor, tente de novo')

                                                listas.carrinho[produto_c]['qtd_estoque'] -= qtd_ad_carrinho

                                            break
                                    break           

                            if encontrado_carrinho == False:

                                listas.carrinho.append(listas.pesquisa[escolha_produto].copy())
                                listas.carrinho[-1]['qtd_estoque'] = qtd_ad_carrinho

                                # Encontrando produto na lista
                                for produto in range(len(listas.estoque)):

                                    # Produto encontrado
                                    if listas.carrinho[-1]['nome'] == listas.estoque[produto]['nome']:

                                        # quantidade em estoque
                                        if qtd_ad_carrinho <= listas.estoque[produto]['qtd_estoque']:
                                            listas.estoque[produto]['qtd_estoque'] -= qtd_ad_carrinho
                                            
                                            comlinha('Produto adicionado ao carrinho')
                                        
                                        # Falta em estoque
                                        else:
                                            comlinha('Quantidade invalida, exede o que temos em estoque. Por favor, tente de novo')

                                            listas.carrinho.pop()

                                            break

                        else:
                            comlinha('ERRO! Quantidade Invalido, tente de novo.')

                            continue

                    elif ad_carrinho == 'N':

                        comlinha(f'Você não quis adiconar {listas.pesquisa[escolha_produto]["nome"]} ao carrinho, voltando as opções da pesquisa')

                        continue

                    #Tradando erro
                    else:

                        comlinha("ERRO! Opção invalida, tente de novo.")

                        continue


                else:
                    comlinha("Erro! Produto invalido, tente novamente")

                    continue

            # Pesquisando de novo
            case 2:

                # Recebendo busca
                encontrado_pesquisa = pesquisas()

                # Produto não existe no estoque
                if encontrado_pesquisa == False:
                    comlinha('Produto não encontrado, voltando ao menu principal')

                    break

            #Voltar ao menu principal
            case 0:
                comlinha('Voltando ao menu principal')

                # Redefinindo tudo
                listas.pesquisa.clear()
                encontrado_carrinho = False
                encontrado_pesquisa = False

                break

            #Tratando erro
            case _:
                comlinha("ERRO! Opção invalida, tente de novo.")

                continue

# Cadastro de novos clientes
def cadastro_usu():

    # Inserindo dados
    print('-' * 50)
    email = input('Insira seu e-mail: ')
    print('-' * 50)
    usu_novo = input('Insira seu nome de usuário: ')
    print('-' * 50)
    senha_usunovo = input('Insira sua senha: ')
    print('-' * 50)
    confirma = input('Confirme sua senha: ')

    # Valida cadastro
    if confirma != senha_usunovo:
        comlinha('As senhas não são coincidentes')

    elif confirma == senha_usunovo:
        comlinha(f'usuario {usu_novo} cadastrado com sucesso ')

        if len(listas.logado) == 0:
            categoria = 'cliente'
        elif len(listas.logado) == 1:
            categoria = 'administrador'

        # Adicionando dados a um dicionario
        dict = {
            'e-mail': email,
            'usuario': usu_novo,
            'senha': senha_usunovo,
            'categoria': categoria
            }
        
        #Adicionando o dicionario a lista de usuarios
        listas.usuarios.append(dict)

# Logando em conta ja existente
def login():

    encontrado = False

    # Recebendo dados
    print('-' * 50)
    usu = (input('Informe o usuário: '))
    print('-' * 50)
    senha = (input('Informe a senha: '))
    
    # Encontrando usuario
    for i in range(len(listas.usuarios)):

        if listas.usuarios[i]['usuario'] == usu:
            comlinha('Usúario encontrado.')

            if listas.usuarios[i]['senha'] == senha:
                comlinha(f'Login concedido, bem vindo {usu}.')
                listas.logado.append(listas.usuarios[i].copy())
                encontrado = True
                break

            else:
                comlinha('Senha incorreta, Tente novamente.')
                break
    
    if encontrado == False:
        comlinha('Usuário não encontrado, tente de novo.')

def recuperar_senha():

    encontrado = False

    print('-' * 50)
    recuperar = input('Informe seu email: ')

    # Encontrando usuario
    for i in range(len(listas.usuarios)):

        if listas.usuarios[i]['e-mail'] == recuperar:
            comlinha('Usúario encontrado.')

            encontrado = True

            comlinha(f'Seu usuário é: {listas.usuarios[i]["usuario"]}')
            comlinha(f'Sua senha é: {listas.usuarios[i]["senha"]}')
    
    if encontrado == False:
        comlinha("Usuário não encontrado, tente de novo.")

# Opções de login
def menu_login():

        while True:

            # Usuário não logado
            if len(listas.logado) == 0:
                comlinha('Menu de login'.center(60))
                comlinha(
                '[1] Cadastro de novo usuário\n'
                '[2] Logar em conta já existente\n'
                '[3] Esqueci minha senha\n'
                '[0] Voltar ao menu principal'
                )

                op = recebe_comlinha("insira a opção desejada: ")
                
                if op == 1:
                    cadastro_usu()
                
                elif op == 2:
                    login()

                elif op == 3:
                    recuperar_senha()

                elif op == 0:
                    comlinha('Voltando ao menu Principal')
                    break
                
                else:
                    print('Erro! Opção invalida, tente novamente! ')
    
            # Usuário logado
            elif len(listas.logado) == 1:
                
                if listas.logado[0]['categoria'] == 'administrador':
                    comlinha('Menu de login'.center(60))
                    comlinha(
                    f'Olá {listas.logado[0]["usuario"]}\n'
                    '[1] Sair da conta\n'
                    '[2] Cadastrar ADM\n'
                    '[0] Voltar ao menu principal')

                else: 
                    comlinha('Menu de login'.center(60))   
                    comlinha(
                    f'Olá {listas.logado[0]["usuario"]}\n'
                    '[1] Sair da conta\n'
                    '[0] Voltar ao menu principal')

                op = recebe_comlinha("insira a opção desejada: ")
                
                if op == 1:
                    listas.logado.clear()
                    comlinha('Você foi deslogado. Voltando ao menu principal')
                    continue

                elif op == 2 and listas.logado[0]['categoria'] == 'administrador':
                    cadastro_usu()

                elif op == 0:
                    comlinha('Voltando ao menu Principal')
                    break
                
                else:
                    print('Erro! Opção invalida, tente novamente! ')

# Opções carrinho
def carrinho():

    # Loop infinito
    while True:

        cont_pesquisa = 0

        # Menu do carrinho
        comlinha ("Carrinho de Compras".center(60))
        comlinha (
        "[1] Remover produto do Carrinho\n"
        "[2] Editar quantidade de produto\n"
        "[3] Listar produtos cadastrados\n"
        "[4] Finalizar compra\n"
        "[0] Voltar ao menu principal"
        )

        opcao = recebe_comlinha("Informe qual opção desejada: ")

        # Excluir produto
        if opcao == 1:
            
            if len(listas.carrinho) >= 1:
                # Exibindo produto
                comlinha('Exibindo lista de produtos'.center(60))
                for indice in range(len(listas.carrinho)):
                    comlinha(
                    f"{cont_pesquisa} " 
                    f"{listas.carrinho[cont_pesquisa]['nome']} " 
                    f"R$ {listas.carrinho[cont_pesquisa]['preço']:.2f} " 
                    f"tipo {listas.carrinho[cont_pesquisa]['tipo']}, "
                    f"tem em estoque {listas.carrinho[cont_pesquisa]['qtd_estoque']}"
                    )
                    cont_pesquisa += 1

                item_excluir = recebe_comlinha("Qual o indice do produto que deseja excluir? ")

                # Ecluindo produto
                if item_excluir >= 0 or 0 < item_excluir < len(listas.carrinho):
                    comlinha(f"{listas.carrinho[item_excluir]['nome']} excluido do carrinho")
                    listas.carrinho.pop(item_excluir)

                else:
                    comlinha('Produto não encontrado, tente de novo')
            else:
                comlinha('Carrinho vazio')

        # Editar produto
        elif opcao == 2:

            if len(listas.carrinho) >= 1:
                # Exibindo produto
                comlinha('Exibindo lista de produtos'.center(60))
                for indice in range(len(listas.carrinho)):
                    comlinha(
                    f"{cont_pesquisa} " 
                    f"{listas.carrinho[cont_pesquisa]['nome']} " 
                    f"R$ {listas.carrinho[cont_pesquisa]['preço']:.2f} " 
                    f"tipo {listas.carrinho[cont_pesquisa]['tipo']}, "
                    f"tem em estoque {listas.carrinho[cont_pesquisa]['qtd_estoque']}"
                    )
                    cont_pesquisa += 1

                item_editado = recebe_comlinha("Digite o indice do produto que deseja editar: ")
                nova_qtd = recebe_comlinha("Nova quantidade em estoque: ")

                if item_editado >= 0 or 0 < item_editado < len(listas.carrinho):

                    if nova_qtd > 0:
                        comlinha(f"{listas.carrinho[item_editado]['nome']} do carrinho foi editado")
                        listas.carrinho[item_editado]['qtd_estoque'] = nova_qtd
                    
                    elif nova_qtd == 0:
                        comlinha("Quantidade 0 exclui o produto do carrinho")
                        comlinha(f"{listas.carrinho[item_editado]['nome']} excluido do carrinho")
                        listas.carrinho.pop(item_editado)
                    
                    else:
                        comlinha("Valor invalido, tente de novo.")

                else:
                    comlinha('Produto não encontrado, tente de novo')

            else:
                comlinha('Carrinho vazio')

        # Listando carrinho
        elif opcao == 3:
            if len(listas.carrinho) >= 1:
                # Exibindo produto
                comlinha('Exibindo lista de produtos'.center(60))
                for indice in range(len(listas.carrinho)):
                    comlinha(
                    f"{cont_pesquisa} " 
                    f"{listas.carrinho[cont_pesquisa]['nome']} " 
                    f"R$ {listas.carrinho[cont_pesquisa]['preço']:.2f} " 
                    f"tipo {listas.carrinho[cont_pesquisa]['tipo']}, "
                    f"tem em estoque {listas.carrinho[cont_pesquisa]['qtd_estoque']}"
                    )
                    cont_pesquisa += 1
            
            else:
                comlinha('Carrinho vazio')

        # Finalizando compra
        elif opcao == 4:
            if len(listas.carrinho) >= 1:
                # Exibindo produto
                comlinha('Exibindo lista de produtos'.center(60))
                for indice in range(len(listas.carrinho)):
                    comlinha(
                    f"{cont_pesquisa} " 
                    f"{listas.carrinho[cont_pesquisa]['nome']} " 
                    f"R$ {listas.carrinho[cont_pesquisa]['preço']:.2f} " 
                    f"tipo {listas.carrinho[cont_pesquisa]['tipo']}, "
                    f"tem em estoque {listas.carrinho[cont_pesquisa]['qtd_estoque']}"
                    )
                    cont_pesquisa += 1
                
                comlinha(
                    "Manu de compra"
                    '[1] Selecionar item'
                    '[2] Comprar tudo'
                    '[0] Cancelar compra'
                )

                comprar = recebe_comlinha('Escolha uma opção: ')

                if comprar == 1:
                    escolha_produto = recebe_comlinha('Informe o indice do produto: ')

                    if escolha_produto == 0 or 0 <= escolha_produto <= len(escolha_produto):
                        print()
            
            else:
                comlinha('Carrinho vazio')
        
        elif opcao == 0:
            comlinha('Voltando ao menu principal')
            break

        else:
            print("Opção Invalida, tente de novo,")
