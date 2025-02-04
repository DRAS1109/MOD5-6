Dicionario1 = {"A": 1, "B": 2}
Dicionario2 = {"C": 2, "D": 3}

Dicionario3 = Dicionario2   #Esta linha não faz uma copia do dicionario2
                            #O dicionario3 é um ponteiro do dicionario2, ou seja, partilham os mesmos dados

Dicionario3["E"] = 4
print(Dicionario2)

Dicionario4 = Dicionario1.copy()
Dicionario4["Z"] = 10
print(Dicionario1)