"""
Pretendemos criar um sistema de recomendações para compras
Para isso devemos recomendar produtos que o João ainda não comprou mas que pertencem a uma
categoria de produtos que já tanha
"""
#Compras do João
Joao = {"TV", "Sapatos", "Tablet"}

#Produtos por categorias
Roupa = {"Calções", "Casaco", "Camisa"}
Calcados = {"Tenis", "Botas", "Sapatos"}
Eletronicos = {"TV", "Tablet", "PC", "PS5"}


#Recomendar produtos cuja categoria pertence a um produto que o João ja comprou mas cujo produto ainda não comprou
#Testar se ja comprou roupa:
João_Roupa = Joao.intersection(Roupa)

if len(João_Roupa) > 0:
    #Os produtos de roupa que o João ainda não comprou
    Roupa_Para_Joao = Roupa.difference(Joao)
    print(Roupa_Para_Joao)


#Testar se ja comprou calçado:
João_Calcado = Joao.intersection(Calcados)

if len(João_Calcado) > 0:
    #Os produtos calçado que o João ainda não comprou
    Calçado_Para_Joao = Calcados.difference(Joao)
    print(Calçado_Para_Joao)


#Testar se ja comprou eletronica:
João_Eletronica = Joao.intersection(Eletronicos)

if len(João_Eletronica) > 0:
    #Os produtos de eletronico que o João ainda não comprou
    Eletronico_Para_Joao = Eletronicos.difference(Joao)
    print(Eletronico_Para_Joao)