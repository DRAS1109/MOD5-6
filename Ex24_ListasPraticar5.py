#Converter de um dicionario numa lista

Meu_Dicionaio = {"Nome": "Joaquim", "Idade": 15, "Morada": "Viseu"}

Minha_Lista = list(Meu_Dicionaio.items())
print(Minha_Lista)


#Converter 2 listas num dicionario
Chaves = ["Nome", "Idade", "Morada"]
Valores = ["Joaquim", 16, "Viseu"]

Dicionaio = dict(zip(Chaves, Valores))
print(Dicionaio)