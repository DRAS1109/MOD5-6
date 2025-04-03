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