"""1. Crie um dicionário com informações de pelo menos três pessoas, como nome, idade e cidade. 
Em seguida, imprima cada informação para cada pessoa."""

Dicionario = {  "Pessoa 1": {"Nome": "Jorge", "Idade": 23, "Cidade": "Viseu"},
                "Pessoa 2": {"Nome": "Andre", "Idade": 17, "Cidade": "Lisboa"},
                "Pessoa 3": {"Nome": "Adelino", "Idade": 35, "Cidade": "Porto"}}

for Chave in Dicionario:
    for Chave2 in Dicionario[Chave]:
        print(f"{Chave} | {Chave2}: {Dicionario[Chave][Chave2]}")
    
    print("")