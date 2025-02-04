"Definir um dicionário: {chave: valor}"
#Criar um dicionario com uma chave (com um valor dentro):
Dicionario = {}
print(Dicionario)

def Adicionar():
    #Adicionar novas chaves
    Dicionario["Nome"] = "Joaquim"
    print(Dicionario["Nome"])

    Dicionario["Idade"] = 10
    print(Dicionario)

    #Adicionar Chave com numeros
    Dicionario[10] = "Teste"
    print(Dicionario)

def Remover_Alterar():
    #Alterar o valor de uma chave
    Dicionario["Nome"] = input("Introduza um nome: ")
    print(Dicionario["Nome"])

    #Remover Chave:Valor do Dicionario
    Valor = Dicionario.pop("Idade", "Não existe nenhuma Chave chamada: 'Idade'")
    print(f"Idade (removida): {Valor}")

    Valor = Dicionario.pop("Idade", "Não existe nenhuma Chave chamada: 'Idade'")
    print(f"Idade (removida): {Valor}")

"Dica: As chaves e os valores podem ser strings ou numeros"

def Percorrer():
    #Fazer um ciclo para percorrer os pares Chave:Valor
    Chaves = Dicionario.keys()      #Devolve uma lista com as chaves
    Valores = Dicionario.values()   #Devolve uma lista com os Valores
    Valores = Dicionario.items()    #Devolve uma lista com os pares Chave:Valor
    print(Chaves, Valores)

    for Chave in Dicionario.keys():
        print(Dicionario[Chave])

    #Ciclo para percorrer os items do dicionario (Chave:Valor)
    for Pares in Dicionario.items():
        print(f"{Pares[0]} : {Pares[1]}")

    "Função get -> devolve o valor da chave, no caso de não existir essa chave mostra a mensagem da string seguinte"
    print(Dicionario.get("Nome","Não existe nenhuma chave chamada: 'Nome'"))

def Igualdade():
    Carro1 = {"Cor":"Azul", "Marca": "Ford", "Lugares": 5}
    Carro2 = {"Cor":"Azul", "Marca": "Ford", "Lugares": 4}
    Carro2 = {"Cor":"Azul", "Marca": "Ford"}

    #Dois dicionarios são iguais quando têm as mesmas Chaves e Valores
    #A ordem não interessa

    if Carro1 == Carro2:
        print("Carros Iguais")
    
    else:
        print("Carros diferentes")