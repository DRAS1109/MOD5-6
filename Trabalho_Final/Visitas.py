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

Visitas = [{"Visita": 1, "Horario": "9-10" , "Lotacao": [], "Lotacao Maxima": 30},
           {"Visita": 2, "Horario": "11-12", "Lotacao": [], "Lotacao Maxima": 30},
           {"Visita": 3, "Horario": "15-16", "Lotacao": [], "Lotacao Maxima": 30},
           {"Visita": 4, "Horario": "17-18", "Lotacao": [], "Lotacao Maxima": 30},]

#Menu Obras
def MenuVisitas():
    """Menu para visitas"""

    while True:

        Op = Utils.Menu(["Horarios", "Visitas","Voltar"], "Menu de visitas")
        print("")

        if Op == 3:
            break

        if Op == 1:
            Horarios()

        if Op == 2:
            Visitas_Guiadas()

def Horarios():
    """SubMenu para os horarios das visitas"""
    

def Visitas_Guiadas():
    pass

def Configurar():
    Visitas[0]["Lotação"] = [{"Id": 1, "N_Pessoas": 2}, {"Id": 2, "N_Pessoas": 5}]
    Visitas[1]["Lotação"] = [{"Id": 1, "N_Pessoas": 3}, {"Id": 2, "N_Pessoas": 24}]
    Visitas[3]["Lotação"] = [{"Id": 1, "N_Pessoas": 8}, {"Id": 2, "N_Pessoas": 12}]

def Adicionar_Horario():
    Utils.F_Titulo("Adicionar novo horario de visita")

    #Horario
    Horarios_Visitas = []
    for Visita in Visitas:
        Horarios_Visitas.append(Visita["Horario"])

    Horario = Utils.Ler_Strings(2, "Qual o horario (Exemplo: 8-9): ")
    Horario = Horario.strip()

    #Verificar se o horario é valido
    L_Horario = Horario.split("-")
    if (L_Horario[0] < 0 or L_Horario[0] > 24) or (L_Horario[1] < 0 or L_Horario[1] > 24):
        print("Horario inválido. Deve ser composto por X-Y")
        return

    if Horario in Horarios_Visitas: #Verificar se ja existe alguma visita guiada para aquele horario
        print("Já tem uma visita guiada para este horário")
        return
    
    #Preço Atual
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