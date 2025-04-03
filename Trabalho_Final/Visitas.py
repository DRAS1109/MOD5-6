"""
Modulo para gerir as visitas Guiadas ao museu
- Horários de visitas
    - Pre-definidos
    - Adicionar
    - Editar
    - Apagar

-Visitas
    - Adicionar mais pessoas a uma visita
        - Perguntar nº de pessoas, apresentar visitas com esses espaços disponiveis, escolher visita, aumentar a lotação da visita e atribuir id do grupo

    - Retirar pessoas a uma visita (necessario identificaçao de id para ninguem cancelar a visita de outras pessoas)
        - Perguntar o id da visita, perguntar se deseja cancelar a visita, cancelar, atualizar lotação da visita e eliminar id

    - Listar (Visita 9-10: 30 pessoas | Visita 11-12: 27 pessoas)
"""
import Utils

Visitas = [{"Visita": 1, "Horario": "9-10" , "Lotacao": 0, "Lotacao Maxima": 30, "Id": []},
           {"Visita": 2, "Horario": "11-12", "Lotacao": 0, "Lotacao Maxima": 30, "Id": []},
           {"Visita": 3, "Horario": "15-16", "Lotacao": 0, "Lotacao Maxima": 30, "Id": []},
           {"Visita": 4, "Horario": "17-18", "Lotacao": 0, "Lotacao Maxima": 30, "Id": []}]

#Dicionario para guardar os campos e o comprimento da maior palavra de cada campo
Campos = {"Visita": 1, "Horario": 5, "Lotacao": 1,"Lotacao Maxima": 2} #Começa com valores pois existem visitas pre definidas

#Adicionar Horario
def Adicionar_Horario():
    Utils.F_Titulo("Adicionar novo horario de visita")

    #Horario
    Horario = Utils.Ler_Strings(2, "Qual o horario (Exemplo: 8-9): ")
    Horario = Horario.strip()

    #Verificar se o horario é valido´
    Horarios_Visitas = []
    for Visita in Visitas:
        Horarios_Visitas.append(Visita["Horario"])

    L_Horario = Horario.split("-")
    if L_Horario[0].isdigit() and L_Horario[1].isdigit():
        L_Horario[0] = int(L_Horario[0])
        L_Horario[1] = int(L_Horario[1])

        if (L_Horario[0] < 0 or L_Horario[0] > 24) or (L_Horario[1] < 0 or L_Horario[1] > 23):
            print("Horario inválido. Deve ser composto por numeros entre 0 e 23")
            return

        if Horario in Horarios_Visitas: #Verificar se ja existe alguma visita guiada para aquele horario
            print("Já tem uma visita guiada para este horário")
            return
    else:
        print("Horario inválido. Deve ser composto por digitos separados por -")
        return

    #Lotacao Maxima
    Lotacao_Maxima = Utils.Ler_Inteiro("Qual a lotação máxima? ")

    #Numero da visita (id)
    NVisita = 1
    if len(Visitas) > 0:
        NVisita = Visitas[len(Visitas) - 1]["Visita"] + 1 #Gera o numero da visita a partir do nº da ultima

    Nova_Obra ={"Visita": NVisita,
                "Horario": Horario,
                "Lotacao Maxima": Lotacao_Maxima}
    
    Visitas.append(Nova_Obra)
    print(f"Visita adicionada com sucesso. \n")

    #Verificar se o tamanho dos campos Visita, Horario, Lotacao Maxima é maior do que os anteriores
    #Evita sempre que se chama o listar, testar a maior palavra
    if len(str(NVisita)) > Campos["Visita"]:
        Campos["Visita"] = len(str(NVisita))
    
    if len(Horario) > Campos["Horario"]:
        Campos["Horario"] = len(Horario)

    if len(str(Lotacao_Maxima)) > Campos["Lotacao Maxima"]:
        Campos["Lotacao Maxima"] = len(str(Lotacao_Maxima))
            

#Editar Horarios
def Editar():
    #Verificar se existem visitas guiadas
    if len(Visitas) == 0:
        print("Não existem visitas guiadas para editar")
        return
    
    #Mostrar as visitas
    Listar(Visitas)
    #print("")

    #Utilizador escolher a visita a editar
    Max = len(Visitas)
    N_Visita = Utils.Ler_Inteiro_Limites(0, Max,f"Visita a editar (Numero) ou 0 (Cancelar): ")

    if N_Visita == 0:
        return

    Visita_Encontrada = Visitas[N_Visita - 1] #Dicionario da visita encontrada

    #Lista com os campos que pode editar editar
    Lista_Campos = ["Horario", "Lotacao Maxima"]

    #Escolher o campo a editar
    Op = Utils.Menu(Lista_Campos, "Qual o campo a editar? ")
    Campo = Lista_Campos[Op - 1]

    #Se o campo a editar for Horario
    if Campo == Lista_Campos[0]:
        Horarios_Visitas = []
        for Visita in Visitas:
            Horarios_Visitas.append(Visita["Horario"])

        Horario = Utils.Ler_Strings(2, "Qual o horario (Exemplo: 8-9): ")
        Horario = Horario.strip()

        #Verificar se o horario é valido
        L_Horario = Horario.split("-")
        if L_Horario[0].isdigit() and L_Horario[1].isdigit():
            L_Horario[0] = int(L_Horario[0])
            L_Horario[1] = int(L_Horario[1])

            if (L_Horario[0] < 0 or L_Horario[0] > 24) or (L_Horario[1] < 0 or L_Horario[1] > 23):
                print("Horario inválido. Deve ser composto por numeros entre 0 e 23")
                return

            if Horario in Horarios_Visitas: #Verificar se ja existe alguma visita guiada para aquele horario
                print("Já tem uma visita guiada para este horário")
                return
        else:
            print("Horario inválido. Deve ser composto por digitos separados por -")
            return

        Novo_Valor = Horario #O codigo ficaria confuso com o nome da variavel a Novo_Valor

    #Se o campo a editar for Lotação maxima
    if Campo == Lista_Campos[1]:
        Novo_Valor = Utils.Ler_Inteiro("Qual a lotação máxima? ")

    #Guardar o novo valor:
    Visita_Encontrada[Campo] = Novo_Valor
    print("Edição concluida com sucesso.")

#Apagar
def Apagar():
    #Verificar se existem visitas guiadas
    if len(Visitas) == 0:
        print("Não existem visitas guiadas para remover")
        return
    
    #Mostrar as visitas
    Listar(Visitas)

    #Utilizador escolher 
    Max = len(Visitas)
    N_Visita = Utils.Ler_Inteiro_Limites(0, Max,f"Visita a apagar (Numero) ou 0  para cancelar: ")

    if N_Visita == 0:
        return
    
    Visita_Encontrada = Visitas[N_Visita - 1] #Dicionario da visita encontrada
    Visitas.remove(Visita_Encontrada)
    print(f"Visita removida com sucesso")

    for N in range(N_Visita-1, Max-1):
        Visitas[N]["Visita"] -= 1

#Listar 
def Listar(Visitas, Titulo = "Lista de Visitas"):
    """Função para listar os campos (Visita, Horario, Lotação maxima) de todas as Visitas"""

    if len(Visitas) == 0:
        print("")
        return

    #Descobrir o tamanho da linha --------------
    Tamanho = 0
    for Campo in Campos:
        Tamanho += Campos[Campo] + len(Campo)

    #Adicionar à variavel tamanho os "extras" (espaços, : e |)
    Extras = (len(Campos) *2) + (len(Campos) *3) - 1 
        #*2 porque cada campo tem : e espaço
        #*3 porque cada campo tem espaço | espaço
        #-1 porque começa com 1 espaço
    Tamanho += Extras  
    
    #Imprimir Titulo
    Utils.F_Titulo(Titulo)

    #Imprimir os dados
    print(f" {Tamanho*"-"}")
    for Visita in Visitas:
        for Campo in Campos:
            print(f" {Campo}: {Visita[Campo]} {" " * (Campos[Campo] - len(str(Visita[Campo])))}", end="|")
        print("\n", Tamanho*"-")


#Adicionar Visitantes
def Adicionar_Visitantes():
    #Numero de Pessoas
    N_Pessoas = Utils.Ler_Inteiro("Quantas pessoas são? ")

    #Listar todas com espaços livres para o nº de pessoas
    Visitas_Encontradas = []
    for Visita in Visitas:
        if Visita["Lotacao Maxima"] - Visita["Lotacao"] > N_Pessoas:
            Visitas_Encontradas.append(Visita["Visita"])
    
    Listar(Visitas_Encontradas)

    #Utilizador escolher qual visita
    Max = Visitas[len(Visitas) - 1]["Visita"] #N da ultima visita
    N_Visita = Utils.Ler_Inteiro_Limites(0, Max,f"Visita a (Numero) ou 0  para cancelar: ")

    if N_Visita == 0 or N_Visita not in Visitas_Encontradas:
        return
    Visita = Visitas[N_Visita - 1] #Dicionario da visita encontrada

    #Id
    Id = 1
    if len(Visita["Lotacao"]) > 0:
        Id = Visita[len("Lotacao") - 1]["Id"] + 1 #Gera o id a partir do id da ultima obra
    print(f"Visita: {Visita['Visita']}, Horario: {Visita["Horario"]}, Id: {Id}")

    Visita["Lotacao"] += N_Pessoas
    Visita["Id"].append({Id:N_Pessoas})

def Cancelar_Visitantes():
    #Utilizador escolhe qual visita
    Max = len(Visitas)
    N_Visita = Utils.Ler_Inteiro_Limites(0, Max,f"Visita a (Numero) ou 0  para cancelar: ")
    Visita = Visitas[N_Visita - 1]

    Id = Utils.Ler_Inteiro("Qual o id atribuido? ")

    if Id not in Visita["Id"]:
        print("O id indicado não existe")
        return

    N_Pessoas = Visita["Id"][Id]
    Visita["Lotacao"] -= N_Pessoas
    Visita["Id"].remove({Id:N_Pessoas})

#Menu para Horarios
def Menu_Horarios():
    """SubMenu para os horarios das visitas"""
    while True:
        Op = Utils.Menu(["Adicionar", "Editar", "Apagar","Listar","Voltar"], "Menu dos horarios")
        print("")

        if Op == 5:
            break

        if Op == 1:
            Adicionar_Horario()

        if Op == 2:
            Editar()
        
        if Op == 3:
            Apagar()
        
        if Op == 4:
            Listar(Visitas)

#Menu para Visitas Guiadas
def Menu_Visitas_Guiadas():
    """SubMenu para as visitas guiadas"""
    while True:
        Op = Utils.Menu(["Adicionar Visitantes", "Cancelar Visitas", "Voltar"], "Menu das visitas guiadas")
        print("")

        if Op == 5:
            break

        if Op == 1:
            Adicionar_Visitantes()

        if Op == 2:
            Cancelar_Visitantes()

#Menu principal do modulo
def MenuVisitas():
    """Menu para visitas"""

    while True:
        Op = Utils.Menu(["Horarios", "Visitante","Voltar"], "Menu de visitas")
        print("")

        if Op == 3:
            break

        if Op == 1:
            Menu_Horarios()

        if Op == 2:
            Menu_Visitas_Guiadas()

#Configurar: Adiciona dados de teste
def Configurar():
    Visitas[0]["Lotação"] = 8
    Visitas[0]["Id"] = {1: 8}

    Visitas[1]["Lotação"] = 21
    Visitas[1]["Id"] = {1:6, 2:12, 3:3}

    Visitas[3]["Lotação"] = 15
    Visitas[3]["Id"] = {1:3, 2:12}