import os 
import pickle
import os.path
import datetime
from re import A
from webbrowser import Opera
clear = lambda x: os.system(x)

#Falta modificacion en administracion

class Operaciones():
    def __init__(self) -> None:
        self.patente=""
        self.codpro=0
        self.fechacupo=""
        self.estado=""
        self.bruto=0
        self.tara=0
class Productos():
    def __init__(self) -> None:
        self.cod=0
        self.nombre=""
        self.estado="A"
class Rubros():
    def __init__(self) -> None:
        self.cod=0
        self.nombre=""
        self.estado="A"
class RubrosxProducto():
    def __init__(self) -> None:
        self.codrubro=0
        self.codpro=0
        self.valmin=0.0
        self.valmax=0.0
class Silos():
    def __init__(self) -> None:
        self.codsilo=0
        self.nombre=""
        self.codpro=0
        self.stock=0

""" ---------------------------Funcionales---------------------- """
        
def validar_patente(patent):
    espacios = " " in patent
    while not(len(patent) >=6 and len(patent) <=7) or espacios:
        if(espacios):
            print("Error. La patente no debe contener espacios.")
        if not(len(patent) >=6 and len(patent) <=7):
            print("Error. La patente debe tener entre 6 y 7 caracteres de longitud.")
        print("Intente nuevamente...")
        patent = input("Ingrese patente: ")
    return patent.upper()

def validar_tipo(tipo,opc,desde,hasta):
    try:
        opc=tipo(opc)
        while opc < desde or opc > hasta:
            print("Error. El numero ingresado debe estar entre",desde,"y",hasta)
            opc = tipo(input("Intente nuevamente: "))
    except:
        print("Error. Debe ingresar un numero.")
        opc = tipo(input("Intente nuevamente: "))
        validar_tipo(tipo,opc,desde,hasta)
    return opc

def validar_longitud(mensaje,hasta):
    opc = input(mensaje)
    while len(opc) > hasta:
        print("Error. La longitud del codigo debe ser menor a",hasta)
        opc = input("Intente nuevamente: ")
    return opc

def formatear(obj,b):
    if b==0: # PRODUCTOS || RUBROS
        obj.cod=str(obj.cod).ljust(10," ")
        obj.nombre=obj.nombre.ljust(20," ")
    elif b==1: # RUBROSXPRODUCTO
        obj.valin=str(obj.valmin).ljust(5," ")
        obj.valmax=str(obj.valmax).ljust(5," ")
    elif b==3: # SILOS
        obj.codsilo=obj.codsilo.ljust(10," ")
        obj.nombre=obj.nombre.ljust(10," ")
        obj.codpro=obj.codpro.ljust(10," ")
        obj.stock=obj.stock.ljust(5," ")
    elif b==4: # OPERACIONES
        obj.patente=obj.patente.ljust(10," ")
        obj.fechacupo=obj.fechacupo.ljust(10," ")
        obj.estado=obj.estado.ljust(1," ")
        obj.codpro=str(obj.codpro).ljust(10," ")
        obj.bruto=str(obj.bruto).ljust(10," ")
        obj.tara=str(obj.tara).ljust(10," ")



def busqueda_secuencial(al,af,bus,cod):
    encontrado = False
    al.seek(0)
    t=os.path.getsize(af)
    while al.tell() <t and encontrado == False:
        pos = al.tell()
        bus = pickle.load(al)
        if bus.cod.strip() == cod:
            encontrado = True
    if encontrado:
        return pos
    else:
        return -1

def mostrar(vr,archf,archl):
    t=os.path.getsize(archf)
    archl.seek(0)
    if t== 0:
        print("No hay nda")
    else:
        while archl.tell() < t:
            vr=pickle.load(archl)
            print(vr.cod,vr.nombre)

def crear_archivos(archivo):
    if not os.path.exists(archivo):
        logico=open(archivo,"w+b")
    else:
        logico=open(archivo,"r+b")
    return logico
#-----------------------Archivos
afo="./operaciones.dat"
afp="./productos.dat"
afr="./rubros.dat"
afrxp="./rubrosxproductos.dat"
afs="./silos.dat"

alo=crear_archivos(afo)
alp=crear_archivos(afp)
alr=crear_archivos(afr)
alrxp=crear_archivos(afrxp)
als=crear_archivos(afs)
""" --------------Procedure-------------------- """

def construccion():
    print("Esta funcionalidad esta construccion")
    clear("pause")

def adminstracion_visible():
    print("A-Titulares\nB-Productos\nC-Rubros\nD-RubrosXProductos\nE-Silos\nF-Sucursales\nG-Productos\nV-Volver al menu")

def submenu_administacion_visible():
    print("A-Alta\nB-Baja\nC-Consulta\nM-Modificaciones\nV-Volver al menu")

def menu_visible():
    print("[1] ADMINISTRACIONES \n[2] ENTREGA DE CUPOS \n[3] RECEPCION \n[4] REGISTRAR CALIDAD \n[5] REGISTRAR PESO BRUTO\n[6] REGISTRAR DESCARGA\n[7] REGISTRAR TARA\n[8] REPORTES\n[0] Fin del programa")

""" #---------------------Functions-Main-------------------# """
""" ---------------------Rubros_Productos--------------------------- """
def alta_producto_rubro(car,nombre,al,af):
    clear("cls")
    print("---------Alta---------")
    t=os.path.getsize(af)
    al.seek(t)
    print("Seleccione codigo de",nombre,". Presione 0 para salir")
    codigo = validar_tipo(int,input("Codigo: "),0,1000)
    while codigo != 0:
        car.cod=codigo 
        print("Nombre de",nombre,": ")
        car.nombre=input("")
        while len(car.nombre)<0 or len(car.nombre)>20:
            print("El ",nombre,"debe tener como maximo 20 caracteres")
            print("Nombre de",nombre,":")
            car.nombre=input("")
        formatear(car,0)
        pickle.dump(car,al)
        al.flush()
        print("Seleccione codigo de",nombre,". Presione 0 para salir")
        codigo = validar_tipo(int,input("Codigo: "),0,1000)
        
    mostrar(car,af,al)
    clear("pause")

def baja_producto(af,al,car):
    car=Productos()
    t=os.path.getsize(af)
    print("Ingrese codigo que desea dar de baja logicamente [0]-Salir")
    codigo=validar_longitud("Codigo: ",10)
    while codigo != 0 and t != 0:
        idx=busqueda_secuencial(al,af,car,codigo)
        if idx !=-1:
            al.seek(idx)
            car=pickle.load(al)
            car.estado="B"
            al.seek(idx)
            pickle.dump(car,al)
            al.flush()
        else:
            print("El codigo ingresado no existe")
        print("Ingrese codigo que desea dar de baja logicamente [0]-Salir")
        codigo=validar_longitud("Codigo: ",10)
        codigo=int(codigo)
        

def consulta_producto(af,al,car,nombre):
    clear("cls")
    t=os.path.getsize(af)
    al.seek(0)
    salida=""
    salida+="{:<24}".format(nombre)
    salida+="{:<40}".format("Codigo")
    salida+="{:<40}".format("Estado")
    print(salida)
    print("---------------------------------------------------------------")
    while al.tell() < t:
        car=pickle.load(al)
        salida=" "
        salida+="{:<25}".format(car.nombre)
        salida+="{:<40}".format(car.cod)
        salida+="{:<25}".format(car.estado)
        print(salida)
    clear("pause")
    
""" ----------------------RubroXProducto--------------------------- """
def alta_silos_rubroxproducto(af,al,car):
    t = os.path.getsize(af)
    # ____________________________ ESTO HAY QUE HACERLO FUNCION___ LA BUSQUEDA DE CODIGOS YA SEA
    # DE RUBBROS O PRODUCTOS SE HACE EN RUBROXPRODUCTO, SILOS (Y CAPAPZ OPERACIONES)
    idx1=idx2=-1
    rub=Rubros()
    pro=Productos()
    while idx1 == -1:
        codrubro = input("Ingrese codigo de rubro: ")
        idx1 = busqueda_secuencial(alr,afr,rub,codrubro)
        if  idx1 == -1:
            print("Error. El codigo de rubro ingresado no existe.")
    while idx2==-1:
        codproducto = input("Ingrese codigo de producto: ")
        idx2 = busqueda_secuencial(alp,afp,pro,codproducto)
        if idx2== -1:
            print("Error. El codigo de producto ingresado no existe.")

    valmin,valmax=rubroxproducto_valminmax()
    al.seek(t)
    car.codrubro=codrubro
    car.codpro=codproducto
    car.valmin=valmin
    car.valmax=valmax
    formatear(car,1)
    pickle.dump(car,al)
    al.flush()


def rubroxproducto_valminmax():
    valmin = validar_tipo(int,input("Ingrese el valor minimo: "),0,100)
    valmax = validar_tipo(int,input("Ingrese el valor maximo: "),valmin,100)
    return valmin,valmax
    
""" --------------------------Silos--------------------------- """
def silos(af,al,car):
    global alp,afp
    t = os.path.getsize(af)
    codigo = validar_longitud("Ingrese el codigo de silo: ",10)
    nombre = validar_longitud("Ingrese un nombre: ",10)
    regp = Productos()
    idx=-1
    while idx ==-1:
        codpro = validar_longitud("Ingrese un codigo de producto: ",10)
        idx = busqueda_secuencial(alp,afp,regp,codpro)
    alp.seek(idx)
    regp = pickle.load(alp)   
    stock = validar_longitud("Ingrese un codigo de stock: ",10)
    al.seek(t)
    car.codsilo=codigo
    car.nombre=nombre
    car.codpro=regp.cod
    print(car.codpro)
    car.stock=stock
    formatear(car,3)
    pickle.dump(car,al)
    al.flush()

""" --------------------------Menu--------------------------- """

def submenu_administacion(opc1):
    opc=""
    while opc != "V":
        clear("cls")
        submenu_administacion_visible()
        opc=input("Seleccione una opcion: ").upper()
        match opc:
            case "A":
                altas(opc1)
            case "B":
                bajas(opc1)
            case "C":
                consultas(opc1)
            case "M":
                print("Hola")
            case "V":
                pass 
            case _:
                print("Opcion invalida")
                                
def altas(opc1):
    if opc1 == "B":
        car=Productos() #Define donde estas yendo######################
        alta_producto_rubro(car,"producto",alp,afp)
    elif opc1== "C":
        rub=Rubros() 
        alta_producto_rubro(rub,"rubro",alr,afr)
    elif opc1=="D":
        car=RubrosxProducto() 
        alta_silos_rubroxproducto(afrxp,alrxp,car)
    elif opc1 =="E":
        sil=Silos()
        silos(afs,als,sil)


def consultas(opc1):
    if opc1 == "B":
        car=Productos() #Define donde estas yendo######################
        consulta_producto(afp,alp,car,"Producto")
    elif opc1 =="C" or opc1 =="D" or opc1 =="E":
        construccion()

def bajas(opc1):
    if opc1 == "B":
        car=Productos() #Define donde estas yendo######################
        baja_producto(afp,alp,car)
    elif opc1 =="C" or opc1 =="D" or opc1 =="E":
        construccion()


def administraciones():
    opc=""
    while opc != "V":
        clear("cls")
        adminstracion_visible()
        opc=input("Seleccione una opcion: ").upper()
        if opc == "B"  or opc == "C" or opc== "D" or opc == "E":
            submenu_administacion(opc)
        elif opc == "A" or opc =="F" or opc=="G":
            construccion()            
        elif opc != "V":
            print("Opcion invalida")
            clear("pause")


def ingreso_fecha():
    print("La fecha debe escribirse en el formato dia-mes-ano. Ejemplo '01-12-05'.")
    ban = True
    while ban:
        try:
            fecha = input("Ingrese fecha en formato DD-MM-AAAA: ")
            datetime.datetime.strptime(fecha, '%d-%m-%Y')
            ban = False
            print("Fecha Valida")
        except ValueError:
            print("Fecha Invalida")
    return fecha


def busqueda_sec_op(rego,pat):
    t = os.path.getsize(afo)
    encontrado = False
    alo.seek(0)
    while alo.tell() < t and encontrado==False:
        idx = alo.tell()
        rego = pickle.load(alo)
        if rego.patente.strip() == pat:
            encontrado = True
    if encontrado:
        return idx
    else:
        return -1
        
def entrega_cupos():
    regpro=Productos()
    rego=Operaciones()
    op="1"
    while op != "0":
        continuar = True
        pat = validar_patente(input("Ingrese patente: "))
        # verificar que la patente no tenga cupos en esa fecha
        fecha = ingreso_fecha()
        idx = busqueda_sec_op(rego,pat)
        if  idx !=1 :
            alo.seek(idx)
            rego = pickle.load(alo)
            if rego.fechacupo.strip() == fecha and rego.estado!="":
                print("Error. Cupo ya otorgado")
                continuar = False
        if continuar:
            alo.seek(alo.tell())
            print(rego.fechacupo)
            idx = busqueda_secuencial(alp,afp,regpro,input("Ingrese el codigo del producto: "))
            if idx == -1:
                print("Error. El codigo de producto ingresado no existe.")
                continuar = False
            else:
                alp.seek(idx)
                regpro = pickle.load(alp)
        if continuar:
            t = os.path.getsize(afo)
            alo.seek(t)
            rego.patente = pat
            rego.codpro = regpro.cod
            rego.fechacupo = fecha
            rego.estado="P"
            formatear(rego,4)
            pickle.dump(rego,alo)
            alo.flush()
            print("Cupo entregado con exito. Estado [Pendiente]")

        op=input("Presione [0] para salir y [1] para continuar:")
        while op!="0" and op!="1":
            op=input("Presione [0] para salir y [1] para continuar:")
        

def recepcion():
    op="1"
    m = 0
    t = os.path.getsize(afo)
    if t!=0:
        alo.seek(0)
        pickle.load(alo)
        m = alo.tell()
    while op != "0": 
        rego = Operaciones()
        pat = validar_patente(input("Ingrese patente: "))
        fecha = datetime.datetime.now().strftime("%d-%m-%Y")
        idx = busqueda_sec_op(rego,pat)
        if idx!=-1:
            alo.seek(idx)
            rego = pickle.load(alo)
            if rego.fechacupo.strip()== fecha:
                rego.estado="A"
                alo.seek(alo.tell()-m)
                pickle.dump(rego,alo)
                alo.flush()
                print("Estado actualizado a [Arribado]")
            else:
                print(rego.fechacupo)
                print("Error. La fecha del camion no coincide con la fecha del dia")
        else:
            print("Error. La patente ingresada no ha sido encontrada")

        op=input("Presione [0] para salir y [1] para continuar:")
        while op!="0" and op!="1":
            op=input("Presione [0] para salir y [1] para continuar:")


def tamano_un_registro(af,al):
    t = os.path.getsize(af)
    if t!=0:
        al.seek(0)
        pickle.load(al)
        tamano_registro = al.tell()
        al.seek(0)
        return tamano_registro
    else:
        return 0

def ordenamiento_decreciente_rubros():
    t_t = os.path.getsize(afr)
    t_u = tamano_un_registro(afr,alr)
    regr1 = Rubros()
    regr2 = Rubros()
    ln = t_t//t_u
    if(ln > 2):
        for x in range(ln):
            alr.seek(0)
            for y in range(ln-(x+1)):
                pos1 = y*t_u
                #print(pos1)
                #print(t_u)
                alr.seek(pos1)
                regr1 = pickle.load(alr)
                regr2 = pickle.load(alr)
                alr.seek(pos1)
                if(regr1.cod<regr2.cod):
                    pickle.dump(regr2,alr)
                    alr.flush()
                    pickle.dump(regr1,alr)
                    alr.flush()
                    alr.seek(pos1)



def busqueda_dico_validacion_rubro_calidad(regr,regrxp,made_in_china):
    # buscar cod de rubro de regrxp(rubrosxproductos.dat) en rubros.dat
    print(made_in_china)
    t = os.path.getsize(afr)
    encontrado = False
    tamano_registro = tamano_un_registro(afr,alr)
    if(tamano_registro!=0):
        inicio = 0
        final = (t//tamano_registro)-1
        while inicio <= final  and encontrado == False:
            print(inicio,final)
            medio = (inicio+final)//2
            print(medio)
            alr.seek(medio*tamano_registro)
            regr = pickle.load(alr)
            print(regr.cod,regrxp.codrubro)
            if int(regr.cod) == int(regrxp.codrubro):
                encontrado = True
                print(regr.cod,regr.nombre)
                print("Ahora hay que ingresar el valor de la calidad del archivo rxp")
                valor_calidad = validar_tipo(float,input("Ingrese el valor del control de calidad: "),0,100)
                if not(valor_calidad<=float(regrxp.valmax) and valor_calidad>=float(regrxp.valmin)):
                    made_in_china[0] += 1
            elif(int(regr.cod) < int(regrxp.codrubro)):
                final = medio-1
            else:
                inicio = medio+1
    return encontrado


def busqueda_validacion_rubros_en_rxp(regrxp,rego,tam_rego):
    regr = Rubros()
    t = os.path.getsize(afrxp)
    alrxp.seek(0)
    encontrado = False
    made_in_china = [0]
    encontrado_dico = False
    while alrxp.tell()<t:
        regrxp = pickle.load(alrxp)
        if (int(regrxp.codpro) == int(rego.codpro)):
            encontrado_dico = busqueda_dico_validacion_rubro_calidad(regr,regrxp,made_in_china)
            encontrado = True
    print(made_in_china)
    if made_in_china[0] > 1 and encontrado and encontrado_dico:
        rego.estado = "R"
        print("El producto no cumple con los estandares de calidad. Estado actualizado a [Rechazado].")
    elif encontrado and encontrado_dico:
        rego.estado = "C"
        print("El producto cumple con los estandares de calidad. Estado actualizado a [Con Calidad]")
    else:
        print("Error. El codigo de producto correspondiente a la patente ingresada no existe.")
    alo.seek(alo.tell()-tam_rego)
    pickle.dump(rego,alo)
    alo.flush()


def registrar_calidad():
    rego = Operaciones()
    regrxp = RubrosxProducto()
    regr = Rubros()
    tam_rego = tamano_un_registro(afo,alo)
    ordenamiento_decreciente_rubros() # ordenamiento del archivo rubros por codigos decreciente
    conti = "1"
    while conti != "0":
        patente = validar_patente(input("Ingrese patente: "))
        idx = busqueda_sec_op(rego,patente) 
        if idx != -1:
            alo.seek(idx)
            rego = pickle.load(alo)
            if rego.estado=="A":
                print("Patente encontrada con exito. El estado [Arribando] es correcto")
            # rego.codpro buscar en rubroxproducto.dat. Si se encuentra, regr.cod (codigo de rubro)
            # para buscar en rubros.dat y si esta, buscar el nombre del rubro y mostrarlocon su codigo correspondiente
            # Ingresar un valor y verificar que ese valor se encuentre entre el maximo y minimo admitido por
            # el archivo rubroxproductos.dat
            busqueda_validacion_rubros_en_rxp(regrxp,rego,tam_rego) # retorna verdadero si encuentra
        elif rego.estado=="A":
            print("Error. La patente ingresada no fue encontrada.")  
        else:
            print("Error. El estado NO es [Arribando]")

        conti=input("Presione [0] para salir y [1] para continuar:")
        while conti!="0" and conti!="1":
            conti=input("Presione [0] para salir y [1] para continuar:")

def menu():
    opc=""
    while opc != "0":
        clear("cls")
        menu_visible()
        opc=input("Seleccione una opcion: ")
        match opc:
            case "1":
                administraciones()
            case "2":
                entrega_cupos()
            case "3":
                recepcion()
            case "4":
                registrar_calidad()
            case "5":
                print("hola")
            case "6":
                print("hola")
            case "7":
                print("hola")
            case "8":
                print("hola")
            case "9":
                print("hola")
            case "0":
                print("Has salido")
            case _:
                pass


menu()



def mostrar2(af,al):
    rego=Operaciones()
    t=os.path.getsize(af)
    al.seek(0)
    if t== 0:
        print("No hay nda")
    else:
        while al.tell() < t:
            rego=pickle.load(al)
            print(rego)
            print(rego.patente,rego.fechacupo,rego.estado)
mostrar2(afo,alo)
# modificada funcion busqueda_sec_op(registro,patente) ahora tiene 2 parametros y solamente busca si la patente existe
# ahora se puede usar tambien en registrar calidad
# busqueda_sec_op(rego,pat) ahora retorna un indice
# ordenamiento decreciente por codigo del archivo rubros.dat
# busqueda dicotomica
def mostrar3(af,al):
    regr=Rubros()
    t=os.path.getsize(af)
    al.seek(0)
    if t== 0:
        print("No hay nda")
    else:
        while al.tell() < t:
            regr=pickle.load(al)
            print(regr.cod,regr.nombre)
mostrar3(afr,alr)