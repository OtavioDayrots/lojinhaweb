estoque = [
    {"nome":"Arroz 5KG", "tipo":"Comida", "preço": 26.99, "qtd_estoque": 300},
    {"nome":"Arroz 1KG", "tipo":"Comida", "preço": 8.99, "qtd_estoque": 300},
    {"nome":"Feijão 1KG", "tipo":"Comida", "preço": 14.99, "qtd_estoque": 300},
    {"nome":"Melancia", "tipo": "fruta", "preço": 5.00 , "qtd_estoque": 200},
    {"nome":"Melão", "tipo": "fruta", "preço": 6.00, "qtd_estoque": 100},
    {"nome":"banana", "tipo": "fruta", "preço": 3.99, "qtd_estoque": 50},
    {"nome":"Abacaxi","tipo":"fruta", "preço": 4.00, "qtd_estoque": 250},
    {"nome":"Abacate", "tipo": "fruta", "preço": 2.99, "qtd_estoque": 35},
    {"nome":"Goiaba", "tipo": "fruta", "preço": 1.99, "qtd_estoque": 40},
    {"nome":"laranja", "tipo": "fruta", "preço": 3.45, "qtd_estoque": 55},
    {"nome":"ameixa", "tipo": "fruta", "preço": 3.78, "qtd_estoque": 56},
    {"nome":"pizza congelada", "tipo": "congelados", "preço": 14.99, "qtd_estoque": 250},
    {"nome":"peixe congelado", "tipo": "congelados", "preço": 20.99, "qtd_estoque": 210},
    {"nome":"batata frita", "tipo": "congelados", "preço": 29.99, "qtd_estoque": 150},
    {"nome":"sorvete", "tipo": "congelados", "preço": 14.99, "qtd_estoque": 100},
    {"nome":"frango congelado", "tipo": "congelados", "preço": 11.99, "qtd_estoque": 300},
    {"nome":"hamburguer congelado", "tipo": "congelados", "preço": 1.99, "qtd_estoque": 420},
    {"nome":"lasanha congelada", "tipo": "congelados", "preço": 25.99, "qtd_estoque": 230},
    {"nome":"polpa de fruta", "tipo": "congelados", "preço": 3.99, "qtd_estoque": 260},
    {"nome":"farofa pinduca 500g", "tipo":"comida", "preço":12.99, "qtd_estoque":150},
    {"nome":"Cup Noodles Sabor costela", "tipo":"comida", "preço": 5.00, "qtd_estoque":130},
    {"nome":"Ketchup Heinz sabor natural 500g", "tipo":"comida","preço":17.99, "qtd_estoque":60},
    {"nome":"Suco Prats laranja 500ml", "tipo":"bebida", "preço":13.99, "qtd_estoque":50},
    {"nome":"Sabão em pó OMO 500g", "tipo":"produto de limpeza", "preço":22.49, "qtd_estoque":50},
    {"nome":"Sabão em barra YPÊ 1kg", "tipo":"produto de limpeza", "preço": 8.49, "qtd_estoque":50},
    {"nome":"Bolinho Ana Maria",  "tipo":"comida", "preço":6.99, "qtd_estoque":60},
    {"nome":"Feijão Preto Dona Dê 500g", "tipo":"comida", "preço":22.89, "qtd_estoque":80},
    {"nome":"Macarrão Espaghetti 500g ", "tipo":"comida", "preço":3.50, "qtd_estoque":100},
    {"nome":"Molho de Tomate Heinz", "tipo":"comida", "preço":3.29, "qtd_estoque":90},
    {"nome":"Pão de forma Pullman 480g", "tipo":"comida", "preço":5.49, "qtd_estoque":130},
    {"nome":"Pacote Presunto 180g Seara", "tipo":"comida", "preço":11.80, "qtd_estoque": 130},
    {"nome":"Pacote Leite desnatado 1L", "tipo":"bebida", "preço":7.49, "qtd_estoque": 150},
    {"nome":"Camelinho sabor morango 500ml", "tipo":"bebida", "preço":15.00, "qtd_estoque":100}
]

pesquisa = []

usuarios = [
    {"e-mail": "admin123@gmail.com","usuario": "admin", "senha": "admin123", "categoria": "administrador"},
    {"e-mail": "cliente123@gmail.com","usuario": "cliente1", "senha": "cliente123", "categoria": "cliente"}     
            ]

logado = {"usuario":"Visitante", "categoria": "cliente"}

carrinho = []

dados_compra =   []

relatorio = []
