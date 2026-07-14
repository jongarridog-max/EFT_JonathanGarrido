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
        unidades_categoria==prendas_dict [cat][1].lower()
        if unidades_categoria == categoria_buscar:
            if cat in bodega_dict:
                tota_unidades = tota_unidades + prendas_dict[cat][1]
        contador = contador +1
    print("total unidades dsiponibles para la categoria",tota_unidades)


def busqueda_precio(p_min,p_max,prendas_dict,bodega_dict):
    resultado=[]
    tallas=list(bodega_dict.keys())
    contador=0
    while contador < len (tallas):
        cat =tallas [contador]
        precio=bodega_dict[cat][0]
        unidades=bodega_dict[cat][1]
        if precio >= p_min and precio <= p_max and unidades > 0:
            if cat in prendas_dict:
                caegoria= prendas_dict [cat][0]
                resultado.append(caegoria + "--" + cat)
        contador = contador +1
    if len (resultado)==0:
        print("No hay prendas en ese cango de precio")
    else:
        resultado.sort()
        contador_res=0
        while contador_res < len (resultado):
            print(resultado[contador_res])
            contador_res= contador_res +1

def actualizar_precio_prenda(nuevo_precio,categoria,prendas_dict,bodega_dict):
    if buscar_categoria(categoria,prendas_dict)== False:
        return False
    categoria_up=str(categoria).upper()
    tallas=list(bodega_dict.keys())
    contador =0
    while contador < len (tallas):
        k =tallas [contador]
        if k.upper()== categoria_up:
            bodega_dict [k][0]=int(nuevo_precio)
            return True
        contador = contador + 1
    return False    

def agregar_prenda(categoria,tallas,polera_basica,polera,jeans_slim,pantalon,chaqueta_urban,chaqueta,vestido_sol,vestido,poleron_cozt,poleron,camisa_formal,camisa,prendas_dict,bodega_dict):
    categoria_up=str(categoria).upper()
    if buscar_categoria(categoria_up,prendas_dict)== True:
        return False
    if str(pantalon).lower()=="s":
        bool_pantalon= True
    else:
     bool_pantalon= False
     prendas_dict[categoria_up]=[tallas,polera,polera_basica,int(chaqueta),bool_pantalon,chaqueta_urban,jeans_slim,vestido,vestido_sol,poleron,poleron_cozt,camisa,camisa_formal]
     bodega_dict[categoria_up]=[int(precio),int(unidades)]
    return True

def eiminar_prenda(categoria,prenda_dict,bodega_dict):
    if buscar_categoria(categoria,prenda_dict)== False:
        categoria_up=str(categoria).upper()
        tallas=list(prendas_dict.keys())
        key_real=""
        contador=0
        while contador <len (tallas):
            if tallas [contador].upper()== categoria_up:
                key_real = tallas [contador]
            contador = contador +1
        if key_real !"":
            prenda_dict.pop(key_real)
            bodega_dict.pop(key_real)
            return True
        return False

prendas = {
    'S001': ['Polera Basica', 'polera', 'M', 'negro', 'algodon', True],
    'S002': ['Jeans Slim', 'pantalon', 'L', 'azul', 'denim', False],
    'S003': ['Chaqueta Urban', 'chaqueta', 'M', 'gris', 'poliester', True],
    'S004': ['Vestido Sol', 'vestido', 'S', 'rojo', 'lino', False],
    'S005': ['Poleron Cozy', 'poleron', 'XL', 'verde', 'algodon', True],
    'S006': ['Camisa Formal', 'camisa', 'M', 'blanco', 'algodon', False],
    ...
}

bodega = {
    'S001': [7990, 12],
    'S002': [19990, 0],
    'S003': [29990, 3],
    'S004': [24990, 6],
    'S005': [17990, 8],
    'S006': [14990, 2],
    ...
}









        

