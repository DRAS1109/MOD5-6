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
Produtos = ["batatas", "bananas", "arroz"    , "bacalhau", "maçãs"]
Stock    = [10       , 50       , 10         , "5"       , "5"    ]
Unidades = ["Kg"     , "Kg"     , "Embalagem", "Unidade" , "Kg"   ]

def Vender(Quantidade, Produto):
    """Recebe a quantidade e o produto, atualiza e mostra o stock"""
    #Verificar se o produto existe
    if Verificação(Produto) == False:
        return
    
    Indice  = Produtos.index(Produto)

    if Stock[Indice] >= Quantidade:
        print(f"Vendeu {Quantidade} {Unidades[Indice]} de {Produto}")
        Stock[Indice] = Stock[Indice] - Quantidade
        Consultar(Produto)
    
    else:
        print("Não pode vender mais do que tem no stock x_X")

def Comprar(Quantidade, Produto):
    if Produto in Produtos:
        Indice = Produtos.index(Produto)

        #Não comprar produtos negativos
        if Quantidade > 0:
            print(f"Comporu {Quantidade} {Unidades[Indice]} de {Produto}")
            Stock[Indice] = Stock[Indice] + Quantidade
            Consultar(Produto)
    
        else:
            print("Não pode comprar produtos negativos x_X")
        
    else: 
        #Comprar produtos novos
        Op = input(f"{Produto} ainda não está nos seus produtos, pretende adiciona-lo? (S/N)")

        if Op.lower() == "s":
            Unidade = input(f"Qual a unidade de medida de {Produto}? ")
            print(f"Comporu {Quantidade} {Unidade} de {Produto}")
            Produtos.append(Produto)
            Stock.append(Quantidade)
            Unidades.append(Unidade)
            Consultar(Produto)


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
    while True:
        Frase = input("O que deseja fazer? ").strip()
        Op = Frase.split(" ")
        
        if len(Op) == 3:
            Operacao = Op[0].strip().lower()
            Quantidade = Op[1].strip().lower()
            Produto = Op[2].strip().lower()

        elif Operacao == "vender":
            Vender(int(Quantidade), Produto)

        elif Operacao == "comprar":
            Comprar(int(Quantidade), Produto)
        
        elif Operacao == "consultar":
            Consultar(Quantidade)
        
        elif Frase == "":
            break
        
        else:
            print("Desculpe, não conheço este comando")

if __name__ == "__main__":
    main()