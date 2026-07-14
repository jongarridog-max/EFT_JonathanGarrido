def validar_texto(texto):
    if str(texto).strip()=="":
        return False
    else:
        return True
    
def validar_entero_mayor_cero(numero):
    try:
        val=int(numero)
        if val >0:
            return True
        else:
            return False
    except ValueError:
        return False
def validar_entero_mayor_igual_cero(numero):
    try:
        val=int(numero)
        if  val >= 0:
            return True
        else:
            return False
    except ValueError:
        return False
    
def validar_opcion(opcion):
    if str(opcion).lower()in ["s","n"]:
        return True
    else:
        return False

def buscar_categoria(categoria,prendas_dict):
    categoria_up=str(categoria).upper ()
    tallas=list(prendas_dict.keys)
    contador = 0
    encontrado= False
    while contador < len (tallas):
        if tallas [contador].upper()==categoria_up:
            encontrado= False
        contador = contador +1
    return encontrado

def mostra_menu():
    print("========== MENÚ PRINCIPAL ==========")   
    print("1.. Unidades por categoría") 
    print("2.Busqueda de prendas por ango de precio")
    print("3.Actualizar precio de prenda")
    print("4.Agregar prenda")
    print("5.Eliminar prenda")
    print("6.Salir")
    print("=======================================")

def  leer_opcion():
    opcion= 0
    while opcion < 1 or opcion > 6:
        try:
            opcion=int(input("Debe selecionar una opcion:"))
            if opcion < 1 or opcion > 6:
                print("[ERROR] debe selecionar una opcion valida")
        except ValueError:
            print("debe selecionar una opcion valida")
            opcion=0
    return opcion


def unidades_categoria(categoria,prendas_dict,bodega_dict,unidades_categoria):
    categoria_buscada=str(categoria).lower()
    tota_unidades=0
    tallas=list(prendas_dict.keys())
    contador= 0
    while contador < len (tallas):
        cat=tallas[contador]
        categoria_prendas ==prendas_dict [cat][1].lower()
        if categoria_prendas == marca_buscada:
            if cat in catalogo_dict:
                tota_unidades = tota_unidades +catalogo_dict [cat][1]
        contador = contador +1
    print("total unidades dsiponibles para la categoria",tota_unidades)

def buscar_precio


        

