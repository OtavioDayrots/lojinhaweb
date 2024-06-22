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

# Exibindo produto
def exibir_lista(lista):

    cont_pesquisa = 0

    comlinha(
    f"{cont_pesquisa} " 
    f"{lista[cont_pesquisa]['nome']} " 
    f"R$ {lista[cont_pesquisa]['preço']:.2f} " 
    f"tipo {lista[cont_pesquisa]['tipo']}, "
    f"tem em estoque {lista[cont_pesquisa]['qtd_estoque']}"
    )
    cont_pesquisa += 1

# Barra de pesquisa
def pesquisas(chave):
            
            # Redefinindo tudo
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
                    exibir_lista(listas.pesquisa)
                
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
    
    ja_existe = False
    ja_existe1 = False

    # Inserindo dados
    print('-' * 50)
    email = input('Insira seu e-mail: ')
    print('-' * 50)

    # email já existente
    for i in range(len(listas.usuarios)):
        if listas.usuarios[i]['e-mail'] == email:
                ja_existe1= True
    if ja_existe1 == False:

        usu_novo = input('Insira seu nome de usuário: ')
        print('-' * 50)

        # Usuário já existente
        for i in range(len(listas.usuarios)):
            if listas.usuarios[i]['usuario'] == usu_novo:
                ja_existe= True
        if ja_existe == False:


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
        else:
            print(' Nome de usuário já cadastrado')
    else:
        print(' E-mail de usuário já cadastrado ')

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

# Finaliza compra e armazena dados
def finalizar_compra(a= 999):

    while True:
        soma = 0
        soma_total = 0

        if a == 999:
            for i in range(len(listas.carrinho)):
                soma = listas.carrinho[i]['preço'] * listas.carrinho[i]['qtd_estoque']
                soma_total += soma

        else:
            soma_total = listas.carrinho[a]['preço'] * listas.carrinho[a]['qtd_estoque']

        comlinha(f'Valor total da compra sera {soma_total:.2f}')
        comlinha(
            'Informe a forma de pagamento\n'
            '[1] Débito\n'
            '[2] Crédito\n'
            '[3] Pix\n'
            '[0] Cancelar compra'
        )

        forma_pagamento = recebe_comlinha("Informe o opção de pagamento: ")

        if forma_pagamento == 1:

            pagamento = 'Débito'

            num_cartão = recebe_comlinha('Informe o número do cartão: ')
            cod_segurança = recebe_comlinha('Informe o código de segurança: ')

        elif forma_pagamento == 2:

            pagamento = 'Crédito'

            num_cartão = recebe_comlinha('Informe o número do cartão: ')
            cod_segurança = recebe_comlinha('Informe o código de segurança: ')

        elif forma_pagamento == 3:

            pagamento = 'Pix'

            comlinha('chave aleatoria:')
            comlinha('dcta478j-196l-03fm-t6gh-4298er7845m2')
        
        elif forma_pagamento == 0:
            break

        else:
            comlinha('Opção invalida, tente novamenete!')
            continue

        dados_com = {'usuario': listas.logado.copy(), 'valor_total': soma_total, 'pagamento': pagamento, 'produtos': listas.dados_compra.copy()}

        listas.dados_compra.append(dados_com.copy())
        listas.relatorio.append(listas.dados_compra.copy())

        comlinha(
            f'Usuário {dados_com["usuario"][0]["usuario"]}\n'
            f'Forma de pagamento {dados_com["pagamento"]}\n'
            f'Valor total {dados_com["valor_total"]:.2f}'
        )

        exibir_lista(dados_com['produtos'][0])

        dados_com.clear()
        listas.dados_compra.clear()

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
                exibir_lista(listas.carrinho)

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
                exibir_lista(listas.carrinho)

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
                exibir_lista(listas.carrinho)
            
            else:
                comlinha('Carrinho vazio')

        # Finalizando compra
        elif opcao == 4:
            
            if len(listas.carrinho) >= 1:
                if len(listas.logado) == 1:

                    # Exibindo produto
                    exibir_lista(listas.carrinho)
                    
                    comlinha(
                        "Manu de compra\n"
                        '[1] Selecionar item\n'
                        '[2] Comprar tudo\n'
                        '[0] Cancelar compra'
                    )

                    escolha_comprar = recebe_comlinha('Escolha uma opção: ')

                    # Comprando apenas um item
                    if escolha_comprar == 1:

                        escolha_produto = recebe_comlinha('Informe o indice do produto: ')

                        if escolha_produto == 0 or 0 <= escolha_produto <= len(escolha_produto):

                            finalizar_compra(escolha_produto)

                        else:
                            comlinha("Indice invalido, tente novamente!")

                    elif escolha_comprar == 2:

                        finalizar_compra()
            
                else:
                    comlinha('Você não está logado, faça login')

            else:
                comlinha('Carrinho vazio')
        
        elif opcao == 0:
            comlinha('Voltando ao menu principal')
            break

        else:
            comlinha("Opção Invalida, tente de novo.")
def admin():
    print()
def cadastro_produto():
            nome = str(input('insira o nome do novo produto: '))
            categoria = str(input('insira a categoria do novo produto: '))
            valor = float(input('insira o valor do novo produto: '))
            quantidade = int(input('insira a quantidade em estoque do novo produto: '))
            dc = {
                'nome': nome,
                'tipo': categoria,
                'preço': valor,
                'qtd_estoque': quantidade
                }
            print(dc)
            listas.estoque.append(dc)
def editar_produto():
    for indice in range(len(listas.estoque)):
        print(indice, "-", listas.estoque[indice])
    indice2 = int(input('Digite o indice do produto que deseja editar: '))
    produto = listas.estoque[indice2]
    print(produto)
    print('Produto encontrado. Digite os novos dados:')
    nome2 = int(input('insira o indice do produto: '))
    categoria2 = str(input('insira a nova categoria do produto: '))
    valor2 = float(input('Novo preço: '))
    quantidade2 = int(input('Nova quantidade em estoque: '))
    produto['nome'] = nome2
    produto['tipo'] = categoria2
    produto['preço'] = valor2
    produto['qtd_estoque'] = quantidade2
def excluir_produto():
    for indice in range(len(listas.estoque)):
        print(indice, "-", listas.estoque[indice])

    indice3 = int(input("Digite o indice do produto que deseja excluir: "))
    produto2 = listas.estoque[indice3]
    listas.estoque.pop(indice3)
def listar_produtos():
     print(listas.estoque)

def menu_admin():
    while True:
        comlinha('Menu de login'.center(60))
        comlinha(
        '[1] Cadastro de produtos\n'
        '[2] Editar dados de um produto\n'
        '[3] Excluir um produto\n'
        '[4] Listar todos os produtos cadatrados\n'
        '[5] Emitir relatorio de vendas\n'
        '[0] Sair do programa\n'
        )
        
        op = int(input("insira a opção desejada: "))
        
        if op == 1:
            cadastro_produto()
        
        if op == 2:
            editar_produto()

        if op == 3:
            excluir_produto()

        if op == 4:
            listar_produtos()
            
        if op == 0:
             print('Programa encerrado.')
             break
    menu_admin()
