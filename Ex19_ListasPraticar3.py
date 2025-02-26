"""
Programa para gerir o stock de produtos.
De cada vez que um produto é vendido o stock deve baixar e da cada vez que o produto é comprado o stock aumenta
Ex:
    Vender 10 Batatas  (diminui em 10 a quantidade de batatas)
    Comprar 50 Bananas (aumenta em 50 o stock de bananas)
    Consultar Batatas  (mostrar: tem X kg de batatas)
    Terminar           (Terminar)

- Se for inserido um comando não conhecido 
- De cada vez que é realizada uma operação deve ser indicado o stock remanescente incluindo a unidade de medida
        (by Afonso & Afonso)
- Não deve ser possivel vender o stock que não existe e não deve ser possivel comprar valores negativos de stock

Hacker:
- Adicionar uma lista com preços unitarios e mostrar em cada operação o valoor total a receber / pagar
        (by Gabriel)

- Adicionar a possibilidade de comprar produtos novos
"""
Produtos = ["Batatas", "Bananas", "Arroz"    , "Bacalhau", "Maçãs"]
Stock    = [10       , 50       , 10         , "5"       , "5"    ]
Unidades = ["Kg"     , "Kg"     , "Embalagem", "Unidade" , "Kg"   ]

def Vender(Quantidade, Produto):
    """Recebe a quantidade e o produto, atualiza e mostra o stock"""
    #Verificar se o produto existe
    if Verificação(Produto) == False:
        return
    
    Indice  = Produtos.index(Produto)

    if Stock[Indice] > Quantidade:
        print(f"Vendeu {Quantidade} {Unidades[Indice]} de {Produto}")
        Stock[Indice] = Stock[Indice] - Quantidade
        Consultar()
    
    else:
        print("Não pode vender mais do que tem no stock x_X")

def Comprar(Produto):
    if Verificação(Produto) == False:
        return

    #TODO:
    #Não comprar produtos negativos
    #Comprar produtos novos

def Consultar(Produto):
    """Recebe o produto e mostra a quantidade no stock"""
    if Verificação(Produto) == False:
        return
    
    Indice  = Produtos.index(Produto)
    print(f"Tem {Stock[Indice]} {Unidades[Indice]} de {Produto} em Stock")

def Verificação(Produto):
    """Recebe o Produto e verifica se existe"""
    if Produto not in Produtos:
        print("O produto não existe")
        return False
    return True

def main():
    #Frase[1] = Operação | Frase[2] = Quantidade | Frase[3] = Produto 
    while True:
        Frase = input("O que deseja fazer? ").strip()
        Frase = Frase.split(" ")

        if Frase[0] == "Vender":
            Vender(Frase[1], Frase[2])

        elif Frase[0] == "Comprar":
            Comprar()
        
        elif Frase[0] == "Consultar":
            Consultar(Frase[2])
        
        else:
            print("Desculpe, não conheço este comando")