import listas

# Imprimindo todos os produtos
def catalogo():

    encontrado_carrinho = False
    seguindo = 0

    while True:
        for produto in range(seguindo, 10 + seguindo):
            print('-' * 60)
            print(f"{produto:<4}{listas.estoque[produto]['nome']:<35}", end=' ')
            print(f"{'R$'} {listas.estoque[produto]['preco']:>8.2f}")
        
        comlinha(
            '[1] Selecionar produto\n'
            '[2] Ver mais...\n'
            '[0] Voltar ao menu principal'
            )

        op = recebe_comlinha('Escolha uma opção: ')

        if op == 1:
                
             # Recebendo indice
                escolha_produto = recebe_comlinha("Informe o número do produto: ")

                if escolha_produto >= 0 and escolha_produto < len(listas.estoque):

                    print('-' * 60)
                    ad_carrinho = input(f"Você deseja adicionar {listas.estoque[escolha_produto]['nome']} ao carrinho?[S/N]: ").upper()

                    if ad_carrinho == 'S':

                        qtd_ad_carrinho = recebe_comlinha("Informe a quantidade que dejesa adicionar ao carrinho: ")

                        if qtd_ad_carrinho > 0:

                            # procurando se o produto ja exite no carrinho
                            for produto_c in range(len(listas.carrinho)):
                                
                                if listas.estoque[escolha_produto]['nome'] == listas.carrinho[produto_c]['nome']:

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

                                listas.carrinho.append(listas.estoque[escolha_produto].copy())
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

                        comlinha(f'Você não quis adiconar {listas.estoque[escolha_produto]["nome"]} ao carrinho.')

                        continue

                    #Tradando erro
                    else:

                        comlinha("ERRO! Opção invalida, tente de novo.")

                        continue

                else:
                    comlinha("Erro! Produto invalido, tente novamente")

                    continue
        
        elif op == 2:
            seguindo += 10
            continue

        elif op == 0:
            comlinha('Voltando ao menu pricipal')
            break
        
        else:
            comlinha('Erro! Opção invalida')

# Prints com linhas
def comlinha(a):

    print('-' * 60)
    print(a)

# Inputs de int com linhas
def recebe_comlinha(a):
    print('-' * 60)
    valor = int(input(a))

    return valor

# Inputs de str com linhas
def recebe_comlinha_str(a):
    print('-' * 60)
    valor = input(a)

    return valor

# Exibindo produto
def exibir_lista(lista):

    for i in range(len(lista)):
        comlinha(
        f"{i} " 
        f"{lista[i]['nome']} " 
        f"R$ {lista[i]['preco']:.2f} " 
        f"tipo {lista[i]['tipo']}, "
        f"tem {lista[i]['qtd_estoque']} em estoque"
        )

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
                
            # Produto não existe no estoque
            if encontrado_pesquisa == False:
                return False

            else:
                 return True
            
# Adiciona o produto ao carrinho ou pesquisa de novo
def menu_pesquisa(a):
     
    # Exibindo produto
    exibir_lista(listas.pesquisa)
     
    encontrado_pesquisa = False 
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

                # Recebendo indice
                escolha_produto = recebe_comlinha("Informe o número do produto: ")

                if escolha_produto >= 0 and escolha_produto < len(listas.pesquisa):

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
                encontrado_pesquisa = pesquisas(a)

                # Produto não existe no estoque
                if encontrado_pesquisa == False:
                    comlinha('Produto não encontrado, voltando ao menu principal')

                    break

                else:
                    # Exibindo produto
                    exibir_lista(listas.pesquisa)
                    continue

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
    email = recebe_comlinha_str('Insira seu e-mail: ')

    if email[-10:] == '@gmail.com':

        # email já existente
        for i in range(len(listas.usuarios)):
            if listas.usuarios[i]['e-mail'] == email:
                    ja_existe1= True
        if ja_existe1 == False:

            usu_novo = recebe_comlinha_str('Insira seu nome de usuário: ')

            # Usuário já existente
            for i in range(len(listas.usuarios)):
                if listas.usuarios[i]['usuario'] == usu_novo:
                    ja_existe= True
            if ja_existe == False:

                
                senha_usunovo = recebe_comlinha_str('Insira sua senha: ')
                
                confirma = recebe_comlinha_str('Confirme sua senha: ')

                # Valida cadastro
                if confirma != senha_usunovo:
                    comlinha('As senhas não são coincidentes')

                elif confirma == senha_usunovo:
                    comlinha(f'usuario {usu_novo} cadastrado com sucesso ')

                    if listas.logado['categoria'] == 'cliente':
                        categoria = 'cliente'

                    elif listas.logado['categoria'] == 'administrador':
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
                comlinha('Nome de usuário já cadastrado')
        else:
            comlinha(' E-mail de usuário já cadastrado ')
    else:
        comlinha('E-mail Invalido')

# Logando em conta ja existente
def login():

    encontrado = False

    # Recebendo dados
    
    usu = recebe_comlinha_str('Informe o usuário: ')
    senha = recebe_comlinha_str('Informe a senha: ')
    
    # Encontrando usuario
    for i in range(len(listas.usuarios)):

        if listas.usuarios[i]['usuario'] == usu:
            comlinha('Usúario encontrado.')

            if listas.usuarios[i]['senha'] == senha:

                comlinha(f'Login concedido, bem vindo {usu}.')

                listas.logado = listas.usuarios[i].copy()
                encontrado = True
                break

            else:
                comlinha('Senha incorreta, Tente novamente.')
                break
    
    if encontrado == False:

        comlinha('Usuário não encontrado, tente de novo.')

def recuperar_senha():

    encontrado = False

    recuperar = recebe_comlinha_str('Informe seu email: ')

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
            if listas.logado['usuario'] == 'Visitante' and listas.logado['categoria'] == 'cliente':

                comlinha('Menu de login'.center(60))
                comlinha(
                '[1] Cadastro de novo usuário\n'
                '[2] Logar em conta já existente\n'
                '[3] Esqueci minha senha\n'
                '[0] Voltar ao menu principal'
                )

                op = recebe_comlinha("Insira a opção desejada: ")
                
                if op == 1:
                    cadastro_usu()
                    continue

                elif op == 2:
                    login()
                    continue

                elif op == 3:
                    recuperar_senha()
                    continue

                elif op == 0:
                    comlinha('Voltando ao menu Principal')
                    break
                
                else:
                    print('Erro! Opção invalida, tente novamente! ')
    
            # Usuário logado
                
            elif listas.logado['categoria'] == 'administrador':
                comlinha('Menu de login'.center(60))
                comlinha(
                f'Olá {listas.logado["usuario"]}\n'
                '[1] Sair da conta\n'
                '[2] Cadastrar ADM\n'
                '[0] Voltar ao menu principal')

            else: 
                comlinha('Menu de login'.center(60))   
                comlinha(
                f'Olá {listas.logado["usuario"]}\n'
                '[1] Sair da conta\n'
                '[0] Voltar ao menu principal')

            op = recebe_comlinha("insira a opção desejada: ")
            
            if op == 1:
                listas.logado['usuario'] = 'Visitante'
                listas.logado['categoria'] = 'cliente'
                comlinha('Você foi deslogado.')
                continue

            elif op == 2 and listas.logado['categoria'] == 'administrador':
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
                soma = listas.carrinho[i]['preco'] * listas.carrinho[i]['qtd_estoque']
                soma_total += soma
            
            listas.dados_compra.append(listas.carrinho.copy())

        else:
            soma_total = listas.carrinho[a]['preco'] * listas.carrinho[a]['qtd_estoque']
            
            listas.dados_compra.append(listas.carrinho[a].copy())

        comlinha(f'Valor total da compra sera R${soma_total:.2f}')
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

            print('-' * 60)
            endereço = input('Informe o endereço de entrega, frete gratis: ')
            num_cartão = recebe_comlinha('Informe o número do cartão: ')
            cod_segurança = recebe_comlinha('Informe o código de segurança: ')

        elif forma_pagamento == 2:

            pagamento = 'Crédito'

            print('-' * 60)
            endereço = input('Informe o endereço de entrega, frete gratis: ')
            num_cartão = recebe_comlinha('Informe o número do cartão: ')
            cod_segurança = recebe_comlinha('Informe o código de segurança: ')

        elif forma_pagamento == 3:

            pagamento = 'Pix'

            print('-' * 60)
            endereço = input('Informe o endereço de entrega, frete gratis: ')
            comlinha('chave aleatoria:')
            comlinha('dcta478j-196l-03fm-t6gh-4298er7845m2')
        
        elif forma_pagamento == 0:
            break

        else:
            comlinha('Opção invalida, tente novamenete!')
            continue

        dados_com = {'usuario': listas.logado.copy(), 'valor_total': soma_total, 'pagamento': pagamento, 'produtos': listas.dados_compra.copy()}

        listas.relatorio.append(dados_com.copy())

        comlinha(
            f'Usuário {dados_com["usuario"]["usuario"]}\n'
            f'Forma de pagamento {dados_com["pagamento"]}\n'
            f'Valor total {dados_com["valor_total"]:.2f}'
        )

        if a == 999:
            exibir_lista(dados_com['produtos'][0])

            listas.carrinho.clear()
        
        else:
            exibir_lista(dados_com['produtos'])

            listas.carrinho.pop(a)

        comlinha("Boa compra, Volte sempre!")
        dados_com.clear()
        listas.dados_compra.clear()

        break

# Opções carrinho
def carrinho():

    # Loop infinito
    while True:

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

                    # Encontrando produto na lista
                    for produto_e in range(len(listas.estoque)):

                        # Produto encontrado
                        if listas.carrinho[item_excluir]['nome'] == listas.estoque[produto_e]['nome']:

                            # Devolvendo ao carrinho
                            listas.estoque[produto_e]['qtd_estoque'] += listas.carrinho[item_excluir]['qtd_estoque']

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

                if item_editado == 0 or 0 < item_editado < len(listas.carrinho):

                    if nova_qtd > 0:
                        comlinha(f"{listas.carrinho[item_editado]['nome']} do carrinho foi editado")

                        # Encontrando produto na lista
                        for produto_e in range(len(listas.estoque)):

                            # Produto encontrado
                            if listas.carrinho[item_editado]['nome'] == listas.estoque[produto_e]['nome']:

                                # Devolvendo ao carrinho
                                listas.estoque[produto_e]['qtd_estoque'] += (listas.carrinho[item_editado]['qtd_estoque'] - nova_qtd)

                        listas.carrinho[item_editado]['qtd_estoque'] = nova_qtd
                    
                    elif nova_qtd == 0:

                        comlinha("Quantidade 0 exclui o produto do carrinho")
                        comlinha(f"{listas.carrinho[item_editado]['nome']} excluido do carrinho")

                        # Encontrando produto na lista
                        for produto_e in range(len(listas.estoque)):

                            # Produto encontrado
                            if listas.carrinho[item_excluir]['nome'] == listas.estoque[produto_e]['nome']:

                                # Devolvendo ao carrinho
                                listas.estoque[produto_e]['qtd_estoque'] += listas.carrinho[item_excluir]['qtd_estoque']

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

                if listas.logado['usuario'] != 'Visitante':

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

# Cadastrando novos produtos no estoque
def cadastro_produto():
            
            encontrado_estoque = False

            nome = recebe_comlinha_str('insira o nome do novo produto: ')
            categoria = recebe_comlinha_str('insira a categoria do novo produto: ')
            print('-' * 60)
            valor = float(input('insira o valor do novo produto: '))
            quantidade = recebe_comlinha('insira a quantidade em estoque do novo produto: ')

            dc = {
                'nome': nome,
                'tipo': categoria,
                'preço': valor,
                'qtd_estoque': quantidade
                }

            # Encontrando produto na lista
            for produto_e in range(len(listas.estoque)):

                # Produto encontrado
                if dc['nome'] == listas.estoque[produto_e]['nome']:
                    encontrado_estoque = True

            if encontrado_estoque == False:
                listas.estoque.append(dc.copy())
                comlinha(f'{dc["nome"]} cadastrado com sucesso.')
            
            else:
                comlinha("Produto já existe, cadastro cancelado.")

# Editar produtos do estoque
def editar_produto():

    while True:

        sub_opcao = 999

        for indice in range(len(listas.estoque)):
            comlinha(f'{indice} - {listas.estoque[indice]}')

        excluir_produto = recebe_comlinha_str('Deseja editar um item? [S/N]\: ').upper()

        if excluir_produto == 'S':

            comlinha("Editar Produto".center(50))
                    
            #Recebenco a posição do produto
            indice = recebe_comlinha("Informe o indice do produto: ")

            #Validando indice
            if indice >= 0 and indice < len(listas.estoque):
                
                #Submenu
                while sub_opcao != 5:
                    print(
                        "\n[1] Nome"
                        "\n[2] Categoria"
                        "\n[3] Preço"
                        "\n[4] Quantidade"
                        "\n[0] Voltar a área de administração"
                        )
                                
                    sub_opcao = recebe_comlinha("Escolha uma opção: ")
                    
                    #Validando a sub_opção
                    if sub_opcao >= 0 and sub_opcao < 5:

                        #Recebendo novo valor e tipo a ser alterado
                        match sub_opcao:
                            case 1:
                                tipo = 'nome'
                                novo_valor = recebe_comlinha_str("Informe o novo nome: ")

                            case 2:
                                tipo = 'categoria'
                                novo_valor = recebe_comlinha_str("Informe a nova categoria: ") 

                            case 3:
                                tipo = 'preço'
                                print('-' * 60)
                                novo_valor = float(input("Informe o novo preço: "))

                            case 4:
                                tipo = 'qtd_estoque'
                                novo_valor = recebe_comlinha("Informe a nova quantidade: ")
                            
                            case 0:
                                comlinha('Voltando ao menu de administração')
                                
                                break

                        #Executando a alteração de valor
                        listas.estoque[indice][tipo] = novo_valor

                    else:
                        comlinha('Opção invalida')
                
                break

            else:
                comlinha("Valor do indice invalido")

        elif excluir_produto == 'N':
            comlinha('Voltando a área do administrador')

            break

        else:
            comlinha('Erro! Tente novamente.')

            continue

# Relatorio de vendas
def relatorio():

    for indice in range(len(listas.relatorio)):

        comlinha(
            f"O {listas.relatorio[indice]['usuario']['categoria']} {listas.relatorio[indice]['usuario']['usuario']}\n"
            f"E-mail: {listas.relatorio[indice]['usuario']['e-mail']}\n"
            f"Comprou no {listas.relatorio[indice]['pagamento']} R${listas.relatorio[indice]['valor_total']:.2f}\n"
            "Produtos comprados:"     
            )

        exibir_lista(listas.relatorio[indice]['produtos'][0])

# Excluir produtos do estoque
def excluir_produto():

    while True:
        for indice in range(len(listas.estoque)):
            comlinha(f'{indice} - {listas.estoque[indice]}')

        excluir_produto = recebe_comlinha_str('Deseja excluir um item? [S/N]: ').upper()

        if excluir_produto == 'S':
            indice3 = recebe_comlinha("Digite o indice do produto que deseja excluir: ")

            if indice3 > 0 and indice3 <= len(listas.estoque):
                comlinha(f'{listas.estoque[indice3]["nome"]} excluido do estoque.')

                listas.estoque.pop(indice3)

            else:
                comlinha('Indice invalido, tente novamente')
        
        elif excluir_produto == 'N':
            comlinha('Voltando a área do administrador')

            break

        else:
            comlinha('Erro! Tente novamente.')

            continue

# Exibir produtos do estoque
def listar_produtos():
     
    for indice in range(len(listas.estoque)):
        comlinha(f'{indice} - {listas.estoque[indice]}')

# Área de manutenção de estoque e ralatorio de vendas
def menu_admin():
    while True:
        comlinha('Menu de login'.center(60))
        comlinha(
        '[1] Cadastro de produtos\n'
        '[2] Editar dados de um produto\n'
        '[3] Excluir um produto\n'
        '[4] Listar todos os produtos cadatrados\n'
        '[5] Emitir relatorio de vendas\n'
        '[0] Sair do programa'
        )
        
        op = recebe_comlinha("Insira a opção desejada: ")
        
        if op == 1:
            cadastro_produto()
        
        elif op == 2:
            editar_produto()

        elif op == 3:
            excluir_produto()

        elif op == 4:
            listar_produtos()
        
        elif op == 5:
            relatorio()
            
        elif op == 0:
             print('Programa encerrado.')
             break
        
        else:
            comlinha('Opção invalida! Tente novamente.')
            continue
