#numbers
def process_numbers(Nombres_bruts):
    
    Nombres=[]
    
    if isinstance(Nombres_bruts, list) == False:
        return Nombres   

    for Nombre_brut in Nombres_bruts:

        if isinstance(Nombre_brut, int):
            Nombres.append(Nombre_brut)
        elif isinstance(Nombre_brut, str):
            if Nombre_brut.isnumeric():
                Nombre = int(Nombre_brut)
                Nombres.append(Nombre)

    Nombres.sort()
    return Nombres

def process_names(Names_bruts):
    
    Names=[]
    
    if isinstance(Names_bruts, list) == False:
        return Names   

    for Name_brut in Names_bruts:

        if isinstance(Name_brut, str):
            if Name_brut.isnumeric()==False:
                Names.append(Name_brut)

    Names.sort()
    return Names
