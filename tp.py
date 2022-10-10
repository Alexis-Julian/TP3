from array import array
from distutils.log import error
from fileinput import close
import os 
import pickle
import os.path
import datetime
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
        self.neto=0
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
        self.cod=0
        self.stock=0
class Reportes():
    def __init__(self):
        self.cupos_entregados = 0
        self.camiones_arribados = 0
        self.nom_prods = []
        self.cod_prods = []
        self.cant_cam_prods = []
        self.neto_tot = []
        self.prom_neto_prods = []
        self.pat_men = []
        


#-------------------------------Funcionales---------------------#          
def validar_patente(patent):
    espacios = " " in patent
    print(patent)
    while not(len(patent) >=6 and len(patent) <=7) or espacios :
        if(espacios):
            print("Error. La patente no debe contener espacios.")
        if not(len(patent) >=6 and len(patent) <=7):
            print("Error. La patente debe tener entre 6 y 7 caracteres de longitud.")
        print("Intente nuevamente...")
        patent = input("Ingrese patente: ")
    return patent.upper()

def validar_tipo(tipo,opc,desde,hasta):
    try:
        espacios = " " in opc
        opc=tipo(opc)
        while not(opc >= desde and opc <= hasta) or espacios or opc =="":
            print("Error. El numero ingresado debe estar entre",desde,"y",hasta)
            opc = tipo(input("Intente nuevamente: "))
    except:
        print("Error. Debe ingresar un numero.")
        opc = input("Intente nuevamente: ")
        validar_tipo(tipo,opc,desde,hasta)
    return opc

def validar_longitud(mensaje,hasta):
    try:
        opc = input(mensaje)
        espacios = " " in opc
        while len(opc) > hasta or espacios or opc =="":
            print("Error. La longitud del codigo/nombre debe ser menor a",hasta,"caracteres. Sin espacios.")
            opc = input("Intente nuevamente: ")
            espacios = " " in opc
    except:
        print("Error")
        validar_longitud(mensaje,hasta)
    return opc

def validar_salida():
        opc=input("Presione [C] para Continuar o [S] para Salir: ").upper()
        while opc != "S" and opc != "C":
            opc=input("Error. [C] para Continuar o [S] para Salir: ").upper()
        return opc
        
def formatear(obj,b):
    if b==0: # PRODUCTOS || RUBROS
        obj.cod=str(obj.cod).ljust(10," ")
        obj.nombre=obj.nombre.ljust(20," ")
    elif b==1: # RUBROSXPRODUCTO
        obj.codpro=str(obj.codpro).ljust(10," ")
        obj.codrubro=str(obj.codrubro).ljust(10," ")
        obj.valin=str(obj.valmin).ljust(5," ")
        obj.valmax=str(obj.valmax).ljust(5," ")
    elif b==3: # SILOS
        obj.codsilo=str(obj.codsilo).ljust(10," ")
        obj.nombre=obj.nombre.ljust(10," ")
        obj.cod=str(obj.cod).ljust(10," ")
        obj.stock=str(obj.stock).ljust(10," ")
    elif b==4: # OPERACIONES
        obj.patente=obj.patente.ljust(10," ")
        obj.fechacupo=obj.fechacupo.ljust(10," ")
        obj.estado=obj.estado.ljust(1," ")
        obj.codpro=str(obj.codpro).ljust(10," ")
        obj.bruto=str(obj.bruto).ljust(10," ")
        obj.tara=str(obj.tara).ljust(10," ")
        obj.neto=str(obj.neto).ljust(10," ")

def busqueda_secuencial(al,af,bus,cod):
    encontrado = False
    al.seek(0)
    t=os.path.getsize(af)
    while al.tell() <t and encontrado == False:
        pos = al.tell()
        bus = pickle.load(al)
        if bus.cod.strip() == str(cod):
            encontrado = True
    if encontrado:
        return pos
    else:
        return -1

def busq_sec_nom_prod_rub(al,af,reg,opc):
    t=os.path.getsize(af)
    al.seek(0)
    encontrado=False
    while al.tell() < t and encontrado != False :
        pos=al.tell()
        reg=pickle.load(al)
        if reg.nombre.strip()==opc:
            encontrado=True
        if encontrado:
            return pos
        else:
            return -1

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

def ingreso_fecha():
    print("La fecha debe escribirse en el formato dia-mes-ano. Ejemplo: "+"'"+ datetime.datetime.now().strftime("%d-%m-%Y")+"'.")
    ban = True
    while ban:
        try:
            fecha = input("Ingrese fecha en formato DD-MM-AAAA: ")
            datetime.datetime.strptime(fecha, '%d-%m-%Y')
            ban = False
        except ValueError:
            print("Fecha Invalida")
    return fecha

def mostrar(vr,archf,archl):
    t=os.path.getsize(archf)
    archl.seek(0)
    if t== 0:
        print("Archivo Vacio")
    else:
        while archl.tell() < t:
            vr=pickle.load(archl)
            print(vr.cod,vr.nombre)

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

def crear_archivos(archivo):
    if not os.path.exists(archivo):
        logico=open(archivo,"w+b")
    else:
        logico=open(archivo,"r+b")
    return logico

def cerrar_archivos():
    alo.close()
    alp.close()
    alr.close()
    alrxp.close()
    als.close()
#-----------------------Archivos
afo="C:\\TP3\\operaciones.dat"
afp="C:\\TP3\\productos.dat"
afr="C:\\TP3\\rubros.dat"
afrxp="C:\\TP3\\rubrosxproductos.dat"
afs="C:\\TP3\\silos.dat"

alo=crear_archivos(afo)
alp=crear_archivos(afp)
alr=crear_archivos(afr)
alrxp=crear_archivos(afrxp)
als=crear_archivos(afs)


def construccion():
    print("Esta funcionalidad esta construccion")
    clear("pause")


#-------------------------------Alta baja consulta modificacion de productos y rubros ---------------------#       
def alta_producto_rubro(car,nombre,al,af):
    clear("cls")
    print("---------Alta---------")
    t=os.path.getsize(af)
    al.seek(t)
    continuar = "C"
    while continuar != "S":
        print("Seleccione codigo de "+nombre+".")
        codigo = validar_tipo(int,input("Codigo: "),0,1000)
        idx=busqueda_secuencial(al,af,car,codigo)
        if idx != -1:
            al.seek(idx)
            car=pickle.load(al)
            if car.estado=="B":
                car.estado="A"    
                al.seek(idx)
                pickle.dump(car,al)
                al.flush()
                print("El "+nombre+" ha sido dado de alta nuevamente")
            else:
                print("Error. El codigo de",nombre,"ingresado ya se encuentra en uso.")
        else:
            mensaje = "Ingrese el nombre del "+ nombre +": "
            car.nombre = validar_longitud(mensaje,20)   
            car.cod = codigo
            formatear(car,0)
            pickle.dump(car,al)
            al.flush()
        continuar = validar_salida()
        
    mostrar(car,af,al)
    clear("pause")

def baja_producto(af,al,car):
    clear("cls")
    car=Productos()
    conti = "C"
    t=os.path.getsize(af)
    if(t==0):
        conti="S"
        print("Error. El archivo productos.dat no posee ningun producto.")
        clear("pause")
    while conti !="S":
        consulta_producto(afp,alp,car,"Producto")
        codigo = validar_tipo(int,input("Ingrese el Codigo de producto que desea dar de baja: "),0,1000)
        idx=busqueda_secuencial(al,af,car,codigo)
        if idx !=-1:
            al.seek(idx)
            car=pickle.load(al)
            car.estado="B"
            al.seek(idx)
            pickle.dump(car,al)
            al.flush()
        else:
            print("Error. El codigo ingresado no existe")
        conti = validar_salida()
        
def consulta_producto(af,al,car,nombre):
    clear("cls")
    t=os.path.getsize(af)
    al.seek(0)
    salida=""
    salida+="{:<24}".format(nombre)
    salida+="{:<30}".format("Codigo")
    salida+="{:<25}".format("Estado")
    print(salida)
    print("---------------------------------------------------------------")
    while al.tell() < t:
        car=pickle.load(al)
        salida=" "
        salida+="{:<25}".format(car.nombre)
        salida+="{:<30}".format(car.cod)
        salida+="{:<25}".format(car.estado)
        print(salida)
    clear("pause")

def modificacion_productos(opc1):
    estado = True if opc1 == "B" else construccion()
    if estado:
        regp = Productos()
        conti = "C"
        t = os.path.getsize(afp)
        if t == 0:
            print("Error. El archivo productos.dat no posee ningun producto.")
            clear("pause")
            conti = "S"
        while conti != "S":
            clear("cls")
            consulta_producto(afp,alp,regp,"Producto")
            cambio = True
            cod = input("Ingrese codigo de producto que desea modificar: ")
            idx = busqueda_secuencial(alp,afp,regp,cod)
            if  idx == -1:
                print("Error. El codigo de producto ingresado no existe.")
                cambio = False
            else:
                alp.seek(idx)
                regp = pickle.load(alp)
                regp.nombre = validar_longitud("Ingrese el nuevo nombre de producto: ",20)

            if cambio and busq_sec_nom_prod_rub(alp,afp,regp,regp.nombre)==-1:
                print("Error. El nombre ingresado ya esta en uso.")
                cambio = False
            if cambio:
                formatear(regp,0)
                alp.seek(idx)
                pickle.dump(regp,alp)
                alp.flush()
            conti = validar_salida()    
#Alta de RubrosXProductos
def alta_rubroxproducto(af,al,car):
    rub=Rubros()
    pro=Productos()
    continuar = "C"
    while continuar != "S":
        t = os.path.getsize(af)
        conti = True
        codproducto = input("Ingrese codigo de producto: ")
        idx=busqueda_secuencial(alp,afp,pro,codproducto)
        if idx == -1:
            print("Error. El codigo de producto ingresado no existe.")
            conti = False
        else:
            alp.seek(idx)
            pro=pickle.load(alp)
            if pro.estado=="B":
                print("El producto esta dado de baja se le devolvera al menu")
                conti=False
            else:
                codrubro = input("Ingrese codigo de rubro: ")
        if conti and busqueda_secuencial(alr,afr,rub,codrubro) == -1:
            print("Error. El codigo de rubro ingresado no existe.")
            conti = False
        if conti:
            valmin = validar_tipo(int,input("Ingrese el valor minimo: "),0,100)
            valmax = validar_tipo(int,input("Ingrese el valor maximo: "),valmin,100)
            al.seek(t)
            car.codrubro = codrubro
            car.codpro = codproducto
            car.valmin = valmin
            car.valmax = valmax
            formatear(car,1)
            pickle.dump(car,al)
            al.flush()
            print("RubrosxProductos dado de alta con exito.")
        continuar = validar_salida()
#Alta de Silos
def alta_silos(af,al,car):
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
    al.seek(t)
    car.codsilo=codigo
    car.nombre=nombre
    car.cod=regp.cod
    print(car.cod)
    formatear(car,3)
    pickle.dump(car,al)
    al.flush()

#-------------------------------Menus---------------------#       
def administraciones():
    opc=""
    while opc != "V":
        clear("cls")
        print("A-Titulares\nB-Productos\nC-Rubros\nD-RubrosXProductos\nE-Silos\nF-Sucursales\nG-Productos\nV-Volver al menu")
        opc=input("Seleccione una opcion: ").upper()
        if opc == "B"  or opc == "C" or opc== "D" or opc == "E":
            submenu_administacion(opc)
        elif opc == "A" or opc =="F" or opc=="G":
            construccion()            
        elif opc != "V":
            print("Opcion invalida")
            clear("pause")

def submenu_administacion(opc1):
    opc=""
    while opc != "V":
        clear("cls")
        print("A-Alta\nB-Baja\nC-Consulta\nM-Modificaciones\nV-Volver al menu")
        opc=input("Seleccione una opcion: ").upper()
        match opc:
            case "A":
                altas(opc1)
            case "B":
                bajas(opc1)
            case "C":
                consultas(opc1)
            case "M":
                modificacion_productos(opc1)
            case "V":
                pass 
            case _:
                print("Opcion invalida")
                                
def altas(opc1):
    if opc1 == "B":
        car=Productos()
        alta_producto_rubro(car,"Producto",alp,afp)
    elif opc1== "C":
        rub=Rubros() 
        alta_producto_rubro(rub,"Rubro",alr,afr)
    elif opc1=="D":
        car=RubrosxProducto() 
        alta_rubroxproducto(afrxp,alrxp,car)
    elif opc1 =="E":
        sil=Silos()
        alta_silos(afs,als,sil)

def bajas(opc1):
    if opc1 == "B":
        car=Productos()
        baja_producto(afp,alp,car)
    elif opc1 =="C" or opc1 =="D" or opc1 =="E":
        construccion()

def consultas(opc1):
    if opc1 == "B":
        car=Productos()
        consulta_producto(afp,alp,car,"Producto")
    elif opc1 =="C" or opc1 =="D" or opc1 =="E":
        construccion()
       
#-------------------------------Entrega de cupos---------------------#         
def entrega_cupos():
    regpro=Productos()
    rego=Operaciones()
    op="C"
    while op != "S":
        continuar = True
        pat = validar_patente(input("Ingrese patente: "))
        # verificar que la patente no tenga cupos en esa fecha
        print("Ingrese la fecha del cupo para recepcion.")
        fecha = ingreso_fecha()
        dia,mes,ano = fecha.split("-")
        diah,mesh,anoh = datetime.datetime.now().strftime('%d-%m-%Y').split("-")
        if int(ano)<int(anoh) or (int(ano)==int(anoh) and int(mes)<int(mesh)) or (int(ano)==int(anoh) and int(mes)==int(mesh) and int(dia)<int(diah)):
            print("Error. La fecha de recepcion no puede ser menor que la fecha actual")
            continuar = False
        else:
            print("Fecha ingresada con exito.")

        idx = busqueda_sec_op(rego,pat)
        if  idx != -1 and continuar:
            alo.seek(idx)
            rego = pickle.load(alo)
            if rego.fechacupo.strip() == fecha and rego.estado!="":
                print("Error. Cupo ya otorgado")
                continuar = False
        if continuar and idx == -1:
            idxp = busqueda_secuencial(alp,afp,regpro,input("Ingrese el codigo del producto: "))
            if idxp == -1:
                print("Error. El codigo de producto ingresado no existe.")
                continuar = False
            else:
                alp.seek(idxp)
                regpro = pickle.load(alp)
                if regpro.estado=="B":
                    print("El producto esta dado de baja se le devolvera al menu")
                    continuar=False   
        if continuar and idx == -1:
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

        op = validar_salida()
        
#-------------------------------Recepcion---------------------#        
def recepcion():
    m = 0
    t = os.path.getsize(afo)
    if t!=0:
        alo.seek(0)
        pickle.load(alo)
        m = alo.tell()
    op = "C"
    while op != "S": 
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

        op = validar_salida()

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
    t = os.path.getsize(afr)
    encontrado = False
    tamano_registro = tamano_un_registro(afr,alr)
    if(tamano_registro!=0):
        inicio = 0
        final = (t//tamano_registro)-1
        while inicio <= final  and encontrado == False:
            medio = (inicio+final)//2
            alr.seek(medio*tamano_registro)
            regr = pickle.load(alr)
            if int(regr.cod) == int(regrxp.codrubro):
                encontrado = True
                print("Ahora hay que ingresar el valor de la calidad del archivo rxp")
                valor_calidad = validar_tipo(float,input("Ingrese el valor del control de calidad: "),0,100)
                if not(valor_calidad<=float(regrxp.valmax) and valor_calidad>=float(regrxp.valmin)):
                    made_in_china[0] += 1
            elif(int(regr.cod) < int(regrxp.codrubro)):
                final = medio-1
            else:
                inicio = medio+1
    return encontrado

def busqueda_validacion_rubros_en_rxp(rego,tam_rego):
    regr = Rubros()
    regrxp = RubrosxProducto()
    t = os.path.getsize(afrxp)
    alrxp.seek(0)
    encontrado = False
    made_in_china = [0]
    encontrado_dico = False
    while alrxp.tell()<t: # recorrido secuencial de rxp
        regrxp = pickle.load(alrxp)
        if (int(regrxp.codpro) == int(rego.codpro)):
            encontrado_dico = busqueda_dico_validacion_rubro_calidad(regr,regrxp,made_in_china)
            encontrado = True
    if made_in_china[0] > 1 and encontrado and encontrado_dico:
        rego.estado = "R"
        print("El producto no cumple con los estandares de calidad. Estado actualizado a [Rechazado].")
    elif encontrado and encontrado_dico:
        rego.estado = "C"
        print("El producto cumple con los estandares de calidad. Estado actualizado a [Con Calidad]")
    else:
        print("Error. El codigo de producto correspondiente a la patente ingresada no existe en el archivo de RubrosXProductos.")
    alo.seek(alo.tell()-tam_rego)
    pickle.dump(rego,alo)
    alo.flush()

#-------------------------------Registrar Calidad---------------------#  
def registrar_calidad():
    rego = Operaciones()
    tam_rego = tamano_un_registro(afo,alo)
    ordenamiento_decreciente_rubros() # ordenamiento del archivo rubros por codigos decreciente
    conti = "C"
    while conti != "S":
        patente = validar_patente(input("Ingrese patente: "))
        idx = busqueda_sec_op(rego,patente) 
        if idx != -1:
            alo.seek(idx)
            rego = pickle.load(alo)
            if rego.estado=="A":
                print("Patente encontrada con exito. El estado [Arribando] es correcto")
                busqueda_validacion_rubros_en_rxp(rego,tam_rego)
            else:
                print("Error. El estado NO es [Arribando]")
        elif rego.estado=="A":
            print("Error. La patente ingresada no fue encontrada.")  
        else:
            print("Error. El estado NO es [Arribando]")
        conti = validar_salida()

#-------------------------------Registrar Peso Bruto---------------------#  
def registrar_peso_bruto():
    rego = Operaciones()
    pat = validar_patente(input("Ingrese patente: "))
    idx = busqueda_sec_op(rego,pat)
    if idx !=-1:
        alo.seek(idx)
        rego=pickle.load(alo)
        if rego.estado=="C":
            rego.bruto=validar_tipo(int,input("Ingrese el peso bruto [Toneladas]: "),0,70)
            rego.estado= "B"
            alo.seek(idx)
            formatear(rego,4)
            pickle.dump(rego,alo)
            alo.flush()
            print("Estado actualizado a [Bruto]")
        else:
            print("Error. El estado debe ser [Con Calidad]")
    else:
        print("Error. La patente ingresada no se ha encontrado")
    clear("pause")

#-------------------------------Registrar Tara---------------------#  
def registrar_tara():
    regs=Silos()
    rego=Operaciones()
    pat = validar_patente(input("Ingrese patente: "))
    idx = busqueda_sec_op(rego,pat)
    if idx != -1:
        alo.seek(idx)
        rego=pickle.load(alo)
        if rego.estado == "B":    
            tara = validar_tipo(int,input("ingrese la tara: "),0,int(rego.bruto))
            rego.tara=tara
            peso_neto = int(rego.bruto) - tara
            rego.neto=peso_neto
            idxs=busqueda_secuencial(als,afs,regs,rego.codpro.strip())
            if idxs != -1:
                als.seek(idxs)
                regs=pickle.load(als)
                regs.stock=int(regs.stock)+peso_neto
                formatear(regs,3)
                als.seek(idxs)
                pickle.dump(regs,als)
                als.flush()
                alo.seek(idx)
                rego.estado="F"
                formatear(rego,4)
                pickle.dump(rego,alo)
                alo.flush()                
                print("Estado actualizado a [Finalizado]")    
            else:
                print("Error. No existe un silo para ese producto. Debe ser dado de alta")
        else:
            print("Error. El estado debe ser [Bruto]")
    else:
        print("La patente ingresada no ha sido encontrada")
    clear("pause")   

#-------------------------------Reportes---------------------#  
def reportes():
    registro_reportes = items_reportes()
    print("REPORTES")
    print("Cantidad de cupos otorgados:",registro_reportes.cupos_entregados) # camiones que pasaron satisfactoriamente por entrega de cupos
    print("Cantidad total de camiones recibidos:",registro_reportes.camiones_arribados) # camiones que pasaron satisfactoriamente por recepcion
    print("Cantidad total de camiones por cada producto: ")
    lista_por_producto(registro_reportes,registro_reportes.cant_cam_prods)
    print("Peso neto total de cada producto: ") # recorrer archivo silos
    lista_por_producto(registro_reportes,registro_reportes.neto_tot)
    print("Promedio del peso neto total de cada producto: ") # recorrer archivo silos
    lista_por_producto(registro_reportes,registro_reportes.prom_neto_prods)
    print("Patente del camion de cada producto que menor catidad de dicho producto descargo:")
    lista_por_producto(registro_reportes,registro_reportes.pat_men)

def items_reportes():
    regrep = Reportes()
    to=os.path.getsize(afo)
    if to != 0:
        u=tamano_un_registro(afo,alo)
        regrep.cupos_entregados=to//u
    #--------------------------------
    alo.seek(0)
    cont=0
    while alo.tell() < to:  # recorrido secuencial archivo operaciones.dat
        rego=pickle.load(alo)
        if rego.estado.strip()=="P":
            cont+=1
    regrep.camiones_arribados = regrep.cupos_entregados-cont
    #-------------------------------
    alp.seek(0)
    tp=os.path.getsize(afp)
    while alp.tell() < tp: # recorrido secuencial archivo productos.dat
        regp=pickle.load(alp)
        regrep.nom_prods.append(regp.nombre.strip())
        regrep.cod_prods.append(regp.cod.strip())
        regrep.cant_cam_prods.append(0)
        regrep.neto_tot.append(0)
        regrep.prom_neto_prods.append(0)
        regrep.pat_men.append("")
    alo.seek(0)
    busca_menor = True
    while alo.tell() < to: # recorrido secuencial archivo operaciones.dat
        rego=pickle.load(alo)
        encontrado = False
        regrep.prom_neto_prods.append(0)
        i = 0
        while  i  < len(regrep.cod_prods) and encontrado == False:
            if regrep.cod_prods[i] == rego.codpro.strip():
                regrep.cant_cam_prods[i] += 1
                encontrado = True
            else: 
                i += 1
    #------------------------------------------
    als.seek(0)
    ts = os.path.getsize(afs)
    while als.tell() < ts:  # recorrido secuencial del archivo silos.dat
        regs = pickle.load(als)
        print(als.tell())
        encontrado = False
        i = 0
        print(regrep.cod_prods)
        while  i < len(regrep.cod_prods) and encontrado == False:
            print(regs.cod.strip())
            if regrep.cod_prods[i] == regs.cod.strip():
                print(regrep.cod_prods[i] == regs.cod.strip())
                regrep.neto_tot[i] += int(regs.stock)
                if regrep.cant_cam_prods[i]!=0:
                    regrep.prom_neto_prods[i] = regrep.neto_tot[i]//regrep.cant_cam_prods[i]
                    encontrado = True
                else:
                    regrep.prom_neto_prods[i] = 0
                    encontrado = True
            else:
                i += 1
    for  x  in range(len(regrep.cod_prods)):
        busca_menor = True
        alo.seek(0)
        while alo.tell() < to: # recorrido secuencial archivo operaciones.dat
            rego = pickle.load(alo)
            print(alo.tell())
            if regrep.cod_prods[x] == rego.codpro.strip():
                print("te encontre")
                if int(rego.neto)!=0 and busca_menor:
                    men = int(rego.neto)
                    regrep.pat_men[x] = rego.patente.strip()
                    busca_menor = False
                if int(rego.neto)!=0 and busca_menor==False and men>int(rego.neto):
                    regrep.pat_men[x] = rego.patente.strip()
                
    return regrep

def lista_por_producto(regrep,array):
    ln = len(regrep.nom_prods)
    print(ln*"---------------")
    salida=""
    for x in range(ln):
        salida+="{:<15}".format(regrep.nom_prods[x])
    print(salida)
    print()
    salida="  "
    for x in range(ln):
        salida+="{:<15}".format(array[x])
    print(salida)
    print(ln*"---------------")

#-------------------------------Listado de silos rechazados y patente menor---------------------#  
def listado_silos_rechazos():
    maysilo = 0
    maystock = 0
    maycods = 0
    t = os.path.getsize(afs)
    als.seek(0)
    while als.tell() < t:
        regs = pickle.load(als)
        if int(regs.stock) > maystock:
            maystock = int(regs.stock)
            maysilo = regs.nombre
            maycods = regs.codsilo
    print("Silo con mayor stock:",maysilo)
    print("Codigo:",maycods)
    print("Stock:",maystock)
    print("Ingrese fecha para visualizar camiones rechazado.")
    fecha = ingreso_fecha()
    t = os.path.getsize(afo)
    alo.seek(0)
    cont = 0
    print("Patentes de camiones rechazados el dia de la fecha: ")
    while t > alo.tell():
        rego = pickle.load(alo)
        estado= (rego.fechacupo == fecha and rego.estado=="R")
        if estado:
            cont += 1
            print(rego.patente)
    if cont == 0:
        print("Ningun camion ha sido rechazado el dia de la fecha.")
    clear("pause")
                            
#-------------------------------Menu Principal---------------------#  
def menu():
    opc=""
    while opc != "0":
        clear("cls")
        print("[1] ADMINISTRACIONES \n[2] ENTREGA DE CUPOS \n[3] RECEPCION \n[4] REGISTRAR CALIDAD \n[5] REGISTRAR PESO BRUTO\n[6] REGISTRAR DESCARGA\n[7] REGISTRAR TARA\n[8] REPORTES\n[9] LISTADO DE SILOS Y RECHAZOS\n[0] Fin del programa")
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
                registrar_peso_bruto()
            case "6":
                print("Proceso en Construccion")
            case "7":
                registrar_tara()
            case "8":
                reportes()
                clear("pause")
            case "9":
                listado_silos_rechazos()
            case "0":
                #cerrar_archivos()                     
                print("Has salido") 
            case _:
                pass

menu()

