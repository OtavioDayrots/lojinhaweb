import listas

# Imprimindo todos os produtos
def catalogo():
    for produto in range(len(listas.estoque)):
        print('-' * 50)
        print(f"{produto:<4}{listas.estoque[produto]['nome']:<35}", end=' ')
        print(f"{'R$'} {listas.estoque[produto]['preço']:>8.2f}")

# Prints com linhas
def comlinha(a):
    print('-' * 50)
    print(a)

# Inputs com linhas
def recebe_comlinha(a):
    print('-' * 50)
    valor = int(input(a))

    return valor

# Barra de pesquisa
def pesquisas():
            
            # Redefinindo tudo
            cont_pesquisa = 0
            encontrado_pesquisa = False
            listas.pesquisa.clear()

            # Recebendo busca
            print('-' * 50)
            pesquisa = input("Informe o produto: ").upper()
            tamanho_pesquisa = len(pesquisa)

            comlinha('Resultados da Pesquisa:'.center(50))

            # Encontrando produto na lista
            for produto in listas.estoque:

                # Produto encontrado_pesquisa
                if pesquisa == produto['nome'][:tamanho_pesquisa].upper():

                    # Preparando caso de erro
                    encontrado_pesquisa = True

                    # Armazenando produto
                    listas.pesquisa.append(produto.copy())

                    # Exibindo produto
                    comlinha(
                    f"{cont_pesquisa} " 
                    f"{listas.pesquisa[cont_pesquisa]['nome']} " 
                    f"R$ {listas.pesquisa[cont_pesquisa]['preço']:.2f} " 
                    f"tem em estoque {listas.pesquisa[cont_pesquisa]['qtd_estoque']}"
                    )
                    cont_pesquisa += 1
                
            # Produto não existe no estoque
            if encontrado_pesquisa == False:
                return False

            else:
                 return True

def menu_pesquisa():
                