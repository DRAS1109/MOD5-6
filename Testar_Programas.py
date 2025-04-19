"""#Campos que não podem ser editados pelo utilizador
Obras_Campos_Priv = ["Id"] #TODO: Só tem 1 parametro pois futuramente pode ser necessario adicionar mais

#Lista das caracteristicas
def Caracteristicas():
    pass

def Data():
    Data_Atual = datetime.now()
    Str_Data_Atual = Data_Atual.strftime("%Y-%m-%d")
    return Str_Data_Atual
    
#Determinar a maior palavra de cada campo
    for Visita in Visitas:
        for Campo in Campos_Horarios:
            if len(str(Visita[Campo])) > Campos_Horarios[Campo]:
                Campos_Horarios[Campo] = len(str(Visita[Campo])) #Guardar o tamanho da maior palavra de cada campo"""
import Utils
Campos = {"Visita": 1, "Horario": 5, "Lotacao": 1,"Lotacao Maxima": 2} #Começa com valores pois existem visitas pre definidas

Visitas = [{"Visita": 1, "Horario": "9-10" , "Lotacao": 0, "Lotacao Maxima": 30, "Id": []},
           {"Visita": 2, "Horario": "11-12", "Lotacao": 0, "Lotacao Maxima": 30, "Id": []},
           {"Visita": 3, "Horario": "15-16", "Lotacao": 0, "Lotacao Maxima": 30, "Id": []},
           {"Visita": 4, "Horario": "17-18", "Lotacao": 0, "Lotacao Maxima": 30, "Id": []}]

#Verificar se a lista de visitas está vazia
def Verificar():
    #Verificar se existem visitas guiadas
    if len(Visitas) == 0:
        print("Não existem visitas guiadas definidas")
        return True

def Listar(Visitas, Titulo = "Lista de Visitas"):
    """Função para listar os campos (Visita, Horario e Lotação maxima) de todas as Visitas"""

    if Verificar() == True:
        return

    #Descobrir o tamanho da linha --------------
    Tamanho = 0
    for Campo in Campos:
        Tamanho += Campos[Campo] + len(Campo)

    #Adicionar à variavel tamanho os "extras" (espaços, : e |)
    Extras = (len(Campos) *2) + (len(Campos) *3) + 1 # Espaços, : e | + 2 para o primeiro e último |
    Tamanho += Extras  
    
    #Imprimir Titulo
    Utils.F_Titulo(Titulo)

    #Imprimir os dados
    print("-" * Tamanho)

    for Visita in Visitas:
        Linha = ""
        for Campo in Campos:
            CampoTexto = f"{Campo}: {Visita[Campo]}"
            Espacos = " " * (Campos[Campo] - len(str(Visita[Campo])))
            Linha += f"| {CampoTexto}{Espacos} "
        Linha += "|"
        print(Linha)
        print("-" * Tamanho)

Listar(Visitas)