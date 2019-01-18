#esta aplicaion se hace con el fin de organizar la empresa de publicidad
#cuando condiferentes modulos,los cuales son las vallas, los sitios y los clientes
#se podran hacer funciones tradicionales como lo son consultar,crear,modificar y eliminar
#
#
#
#esta aplicacion tiene su manejo de datos en archivos planos
import tkinter as tk
from tkinter import messagebox,ttk
import ast
import time,calendar,ctypes

#https://es.wikibooks.org/wiki/Python/Interfaz_gr%C3%A1fica_con_Tkinter/Gesti%C3%B3n_de_ventanas
# informacion super buena del manejo de vnentanas
#ubicacion 0 menu,1 menu valla,valla especifico: vallasT=2,vDisponible=3,vReservado=4,vOcupado=5,acumuladoVallas=6
    
def leerArchivos():
    """
    Lee el archivo correspondiente a los datos generales de las vallas, no especifica su estado en el mercado
    """
    global vallasNorte,vallasSur,vallasOeste,vallasCentro,vallasOriente,vallasBuenaventura,vallasTotal
    #archivo= open(r"C:\Users\usuario\Desktop\Proyecto empresa\tkinter\datos\datosVallas1.txt")
    #lineas= archivo.readlines()
    vn=open(r"C:\Users\usuario\Desktop\Proyecto empresa\tkinter\datos\Vallas Norte.txt")
    vallasNorte=vn.readlines()
    vn.close()
    vs=open(r"C:\Users\usuario\Desktop\Proyecto empresa\tkinter\datos\Vallas Sur.txt")
    vallasSur=vs.readlines()
    vs.close()
    vc=open(r"C:\Users\usuario\Desktop\Proyecto empresa\tkinter\datos\Vallas Centro.txt")
    vallasCentro=vc.readlines()
    vc.close()
    vo=open(r"C:\Users\usuario\Desktop\Proyecto empresa\tkinter\datos\Vallas Oeste.txt")
    vallasOeste=vo.readlines()
    vo.close()
    vOr=open(r"C:\Users\usuario\Desktop\Proyecto empresa\tkinter\datos\Vallas Oriente.txt")
    vallasOriente=vOr.readlines()
    vOr.close()
    vb=open(r"C:\Users\usuario\Desktop\Proyecto empresa\tkinter\datos\Vallas Buenaventura.txt")
    vallasBuenaventura= vb.readlines()
    vb.close()
    vm=open(r"C:\Users\usuario\Desktop\Proyecto empresa\tkinter\datos\Vallas Medellin.txt")
    vallasMedellin=vm.readlines()
    vm.close()
    vallasTotal={"vallasT":""}
 
    i=0
    for ele in vallasNorte:
        ele=ele.strip('\n')##1
        ele=ele.split(',')
        vallasNorte[i]=ele
        i+=1
    i=0
    for ele in vallasOeste:
        ele=ele.strip('\n')###2
        ele=ele.split(',')
        vallasOeste[i]=ele
        i+=1
    i=0
    for ele in vallasOriente:
        ele=ele.strip('\n')###3
        ele=ele.split(',')
        vallasOriente[i]=ele
        i+=1
    i=0
    for ele in vallasCentro:
        ele=ele.strip('\n')###4
        ele=ele.split(',')
        vallasCentro[i]=ele
        i+=1
    i=0
    for ele in vallasSur:
        ele=str(ele).strip('\n')###5
        ele=ele.split(',')
        vallasSur[i]=ele
        i+=1
    i=0
    for ele in vallasBuenaventura:
        ele=ele.strip('\n')###6
        ele=ele.split(',')
        vallasBuenaventura[i]=ele
        i+=1
    i=0
    for ele in vallasMedellin:
        ele=ele.strip('\n')##1
        ele=ele.split(',')
        vallasMedellin[i]=ele
        i+=1

    
    vallasTotal["vallasT"]= vallasNorte + vallasSur+vallasCentro+vallasOeste+vallasOriente+vallasBuenaventura+ vallasMedellin
    
def irVallas():
    """
    Muestra los distintos submodulos que contiene el modulo de vallas,logrando que se pueda reservar,consultar y demas funciones basicas
    Ademas de dar la opcion de mirar las ganacias acumuladas de las vallas en distintos años
    """
    global photo, ubicacion, window,Vallas
    ubicacion=1 #menu de vallas
    photo=tk.PhotoImage(file= 'imagenes\LogoM.gif')
    window.withdraw()
    Vallas=tk.Toplevel()
    Vallas.geometry("800x600+300+150")
    Vallas.title("Vallas")
    Vallas.configure(background='white')
    e=tk.Label(Vallas,image=photo,width="300",height="150").place(x=0,y=0)
    tVallas =tk.Button(Vallas, text= " todas las vallas",width=12,height=2,relief="raised",font=("Helveltica" , 12), command= vallasT).place(x=80,y=220)
    vallasD= tk.Button(Vallas, text= "Vallas disponibles",width=14,height=2,relief="raised",font=("Helveltica" , 12),  command= vDisponible).place(x=210,y=220)
    vallasR = tk.Button(Vallas, text= "Vallas reservadas",width=14,height=2,relief="raised",font=("Helveltica" , 12),  command= vReservado).place(x=360,y=220)
    vallasA = tk.Button(Vallas, text= "Vallas arrendadas",width=14,height=2,relief="raised",font=("Helveltica" , 12),  command= vOcupado).place(x=510,y=220)
    aVallas=tk.Button(Vallas, text= "Acumulado Vallas",width=14,height=2,relief="raised",font=("Helveltica" , 12),  command= acumuladoVallas).place(x=290,y=330) # muestra un acumulado de las ganacias netas del total de vallas
    Volver=tk.Button(Vallas, text="volver",relief="raised",command=volver,font=("helvetica",16)).place(x=0,y=500)# la funcion de volver tendra diferentes condicionales dependiendo de donde se encuentre el usuario

def vallasT():
    """
    Muestra todas las vallas con las que se cuenta para ofrecer al mercado
    NO muestra en que estado se encuetra la valla
    """
    global Vallas,photo,vallasTotal,ubicacion,tVallas,combo
    ubicacion=2
    Vallas.withdraw()
    tVallas=tk.Toplevel()
    tVallas.geometry("1000x600+200+150")
    tVallas.title("Todas las vallas")
    tVallas.configure(background='white')
    ###### botones y etiquetas####
    e=tk.Label(tVallas,image=photo,width="300",height="150").place(x=0,y=0)
    label=tk.Label(tVallas, text="Listado de Vallas",relief="flat",font=("Helveltica" , 18),bg="white").place(x=250,y=205)
    Ver= tk.Button(tVallas, text=" Ver mas ",relief="raised", font=("Helveltica" , 12), command=datosValla).place(x=820,y=280)
    Mapa= tk.Button(tVallas, text=" Ver Galeria ",relief="raised",font=("Helveltica" , 12), command=mapa).place(x=20,y=320)
    reservar= tk.Button(tVallas, text=" Reservar Valla ", relief="raised",font=("helvetica",12),command=reservarValla).place(x=200,y=500)
    arrendar= tk.Button(tVallas, text=" Arrendar Valla ", relief="raised",font=("helvetica",12),command=arrendarValla).place(x=450,y=500)
    combo=ttk.Combobox(tVallas,width=108,height=10,font=("helvetica",10))
    combo.place(x=20,y=280)
    Volver=tk.Button(tVallas, text="volver",relief="raised",command=volver,font=("helvetica",16)).place(x=0,y=500)
    
    ### ciclo para mostrar las vallas en el combobox ###
    for i in vallasTotal["vallasT"]:
        i[0]="Dirección: ,"+ str(i[0]+",")
        i[1]="Referencia: ," +str(i[1]+",")
        i[2]="Sentido: ,"+ str(i[2]+",")
        i[5]="Valor: ,"+ str(i[5]+",")
    combo["values"]=vallasTotal["vallasT"]

def obtenerReferencia():
    global referencia,combo
    # este codigo sirve para obtener la referencia del combobox
    valla=combo.get()
    if valla!="":
        valla=valla.split(',')
        referencia=valla[3]
    # fin del codigo
#### detalles de paginas  ####
def mapa():
    global photo,sol,luna,punto,mapa,eliminar,referencia,vallasTotal
    
    obtenerReferencia()
    if referencia!="":
        eliminar=1
        user32 = ctypes.windll.user32 # con estas tres lineas se obtiene l tamaño de la pantalla
        user32.SetProcessDPIAware()
        ancho, alto = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
        mapa=tk.Toplevel()
        mapa.geometry(str(ancho)+"x"+str(alto))
        mapa.title("Galeria")
        mapa.configure(background='white')
        e=tk.Label(mapa,image=photo,width="300",height="150").place(x=0,y=0)
        label=tk.Label(mapa,text="Galeria de fotos",font=("Helveltica" , 35),bg="white").place(x=800,y=20)
        notebook=ttk.Notebook(mapa,height="600",width="1500")
        notebook.place(x=200,y=200)
        maps=ttk.Frame(notebook,width="200",height="150")
        foto1=ttk.Frame(notebook,width="200",height="150")
        foto2=ttk.Frame(notebook,width="200",height="150")
        notebook.add(maps,text="Ubicación",image=punto,compound="left")
        notebook.add(foto1,text="Foto dia",image=sol,compound="left")
        notebook.add(foto2,text="Foto noche",image=luna,compound="left")
        mImagen=tk.Label(foto1,image=sol, width="500",height="500").place(x=0,y=0)
        cerrar=tk.Button(mapa,text="cerrar", relief="raised",font=("helvetica",14),command=cerrarVentana).place(x=20,y=500)
    else:
        messagebox.showwarning("Alerta","Debe escoger alguna opcion para continuar")
        

def cerrarVentana():
    global mapa,permiso,eliminar
    if eliminar==1:
        mapa.destroy()
    elif eliminar==2:
        permiso.destroy()

    
def datosValla():
    """
    se encarga de mostrar todos los datos de una valla
    """
    global ubicacion,vAcumulado,vOcupado,vReservado,vDisponible,tVallas,infoValla,referencia,vallasTotal
    
    
    obtenerReferencia()
    if referencia!="":
        if ubicacion==3:
            vDisponible.withdraw()
            ubicacion=3.1
        elif ubicacion==4:
            vReservado.withdraw()
            ubicacion=4.1
        elif ubicacion==5:
            vOcupado.withdraw()
            ubicacion=5.1
        elif ubicacion==6:
            vAcumulado.withdraw()
            ubicacion=6.1
        elif ubicacion==2:
            tVallas.withdraw()
            ubicacion=2.1
        
        infoValla=tk.Toplevel()
        user32 = ctypes.windll.user32 # con estas tres lineas se obtiene l tamaño de la pantalla
        user32.SetProcessDPIAware()
        ancho, alto = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
        infoValla.geometry(str(ancho)+"x"+str(alto))
        infoValla.title("informacion Valla "+str(referencia)) 
        infoValla.configure(background='white')
        e=tk.Label(infoValla,image=photo,width="300",height="150").place(x=0,y=0)
        datosGen=tk.Frame(infoValla,width="1300",height="333.333",bg="gray93").place(x=303,y=0)
        datosPauta=tk.Frame(infoValla,width="1300",height="333.333",bg="gray95").place(x=303,y=333.33)
        datosSitio=tk.Frame(infoValla,width="1300",height="333.333",bg="gray97").place(x=303,y=666.666)

        label1=tk.Label(infoValla,text="Datos generales de la valla",font=("helvetica",22)).place(x=750,y=25)# titulos de frames
        label2=tk.Label(infoValla,text="Datos de la Pauta o reserva",font=("helvetica",22)).place(x=750,y=358)
        label2=tk.Label(infoValla,text="Datos del sitio",font=("helvetica",22)).place(x=820,y=688)
        #etiquetas primer frame
        e1=tk.Label(infoValla,text="Direccion de la valla: ",relief="raised",font=("helvetica",16)).place(x=350,y=100)
        e2=tk.Label(infoValla,text="Referencia de la valla: ",relief="raised",font=("helvetica",16)).place(x=350,y=150)
        e3=tk.Label(infoValla,text="Sentido de la via: ",relief="raised",font=("helvetica",16)).place(x=350,y=200)
        e4=tk.Label(infoValla,text="Estrato: ",relief="raised",font=("helvetica",16)).place(x=900,y=100)
        e5=tk.Label(infoValla,text="Medidas: ",relief="raised",font=("helvetica",16)).place(x=900,y=150)
        e6=tk.Label(infoValla,text="Valor mensual sin descuentos: ",relief="raised",font=("helvetica",16)).place(x=900,y=200)
        #Datos de la Valla
        i=0
        for elem in vallasTotal["vallasT"]:
            if referencia in elem[1]:
                break
            else:
                i+=1
        datos=vallasTotal["vallasT"][i]
        direc= datos[0].split(',')
        direc=direc[1].strip(',')
        sen=datos[2].split(',')
        sen=sen[1].strip(',')
        est=datos[3]
        med=datos[4]
        vlr=datos[5].split(',')
        vlr=vlr[1].strip(',')
        r1=tk.Label(infoValla,text=direc,font=("helvetica",16)).place(x=600,y=100) #direccion
        r2=tk.Label(infoValla,text=referencia,font=("helvetica",16)).place(x=600,y=150) #referencia
        r3=tk.Label(infoValla,text=sen,font=("helvetica",16)).place(x=550,y=200) #sentido de la via
        r4=tk.Label(infoValla,text=est,font=("helvetica",16)).place(x=1000,y=100) #estrato
        r5=tk.Label(infoValla,text=med,font=("helvetica",16)).place(x=1000,y=150) #medidas
        r6=tk.Label(infoValla,text=vlr,font=("helvetica",16)).place(x=1200,y=200) #Valor sin descuento
        r7=tk.Button(infoValla,text=" Ver permiso ", relief="raised",font=("helvetica",17),command=mostrarPermiso).place(x=680,y=250)
        #condicional para mostrar informacion de pauta
    ##    if referencia in (vallasReservadas or vallasArrendadas):
    ##        #etiquetas de pauta
    ##        p1=tk.Label(infoValla,text="Cliente: ",relief="raised",font=("helvetica",16)).place(x=350,y=433)
    ##        p2=tk.Label(infoValla,text="Agencia: ",relief="raised",font=("helvetica",16)).place(x=350,y=483)
    ##        p3=tk.Label(infoValla,text="Valor pauta: ",relief="raised",font=("helvetica",16)).place(x=350,y=533)
    ##        p4=tk.Label(infoValla,text="Valor con descuento: ",relief="raised",font=("helvetica",16)).place(x=900,y=433)
    ##        p5=tk.Label(infoValla,text="Duracion: ",relief="raised",font=("helvetica",16)).place(x=900,y=483)
    ##        p6=tk.Label(infoValla,text="Fecha inicio: ",relief="raised",font=("helvetica",16)).place(x=900,y=533)
    ##        p7=tk.Label(infoValla,text="Fecha final: ",relief="raised",font=("helvetica",16)).place(x=900,y=583)
    ##        a = "hoola"
    ##        t1=tk.Label(infoValla,text=a,font=("helvetica",16)).place(x=475,y=433)
    ##        t2=tk.Label(infoValla,text=a,font=("helvetica",16)).place(x=475,y=483)
    ##        t3=tk.Label(infoValla,text=a,font=("helvetica",16)).place(x=480,y=533)
    ##        t4=tk.Label(infoValla,text=a,font=("helvetica",16)).place(x=1120,y=433)
    ##        t5=tk.Label(infoValla,text=a,font=("helvetica",16)).place(x=1038,y=483)
    ##        t6=tk.Label(infoValla,text=a,font=("helvetica",16)).place(x=1043,y=533)
    ##        t7=tk.Label(infoValla,text=a,font=("helvetica",16)).place(x=1035,y=583)
    ##    else:
    ##        d1=tk.Label(infoValla,text=" Se encuentra disponible ",font=("helveltica",22),fg="red").place(x=725,y=483)
        #etiquetas para sitio
        s1=tk.Label(infoValla,text="Nombre propietario: ",relief="raised",font=("helvetica",16)).place(x=350,y=763)
        s2=tk.Label(infoValla,text="Valor contrato: ",relief="raised",font=("helvetica",16)).place(x=350,y=813)
        s3=tk.Label(infoValla,text="Canon arrendamiento: ",relief="raised",font=("helvetica",16)).place(x=350,y=863)
        s4=tk.Label(infoValla,text="Inicio contrato: ",relief="raised",font=("helvetica",16)).place(x=900,y=763)
        s5=tk.Label(infoValla,text="Duracion contrato: ",relief="raised",font=("helvetica",16)).place(x=900,y=813)
        s6=tk.Label(infoValla,text="Fecha de pago: ",relief="raised",font=("helvetica",16)).place(x=900,y=863)
        s7=tk.Label(infoValla,text="valor pago: ",relief="raised",font=("helvetica",16)).place(x=900,y=916)
        a = "hoola"
        d1=tk.Label(infoValla,text=a,font=("helvetica",16)).place(x=580,y=763)
        d2=tk.Label(infoValla,text=a,font=("helvetica",16)).place(x=550,y=813)
        d3=tk.Label(infoValla,text=a,font=("helvetica",16)).place(x=584,y=863)
        d4=tk.Label(infoValla,text=a,font=("helvetica",16)).place(x=1068,y=763)
        d5=tk.Label(infoValla,text=a,font=("helvetica",16)).place(x=1100,y=813)
        d6=tk.Label(infoValla,text=a,font=("helvetica",16)).place(x=1090,y=863)
        d7=tk.Label(infoValla,text=a,font=("helvetica",16)).place(x=1035,y=916)

        #boton de regresar
        Volver=tk.Button(infoValla, text="volver",relief="raised",command=volver,font=("helvetica",16)).place(x=0,y=500)
    else:
        messagebox.showwarning("Alerta","Debe escoger alguna opcion para continuar")
        
        
        

    
def mostrarPermiso():
    global eliminar,permiso,referencia,permisoImage,referencia
    
    eliminar=2
    ref=('\\'+str(referencia))
    permiso=tk.Toplevel()
    permisoImage=tk.PhotoImage(file= 'imagenes\permisos'+ref+".png")
    permiso.geometry("600x800+300+150")
    label=tk.Label(permiso,image=permisoImage).place(x=0,y=0)
    cerrar=tk.Button(permiso,text="cerrar", relief="raised",font=("helvetica",14),command=cerrarVentana).place(x=525,y=750)

      
def reservarValla():
    global ubicacion,vAcumulado,vOcupado,vReservado,vDisponible,tVallas,infoValla,reservar,cliente,agencia,valorT,valorD,duracion,fechaIni,fechaFin,referencia
    obtenerReferencia()
    if referencia!="":
        if ubicacion==3:
            vDisponible.withdraw()
            ubicacion=3.2
        elif ubicacion==4:
            vReservado.withdraw()
            ubicacion=4.2
        elif ubicacion==5:
            vOcupado.withdraw()
            ubicacion=5.2
        elif ubicacion==6:
            vAcumulado.withdraw()
            ubicacion=6.2
        elif ubicacion==2:
            tVallas.withdraw()
            ubicacion=2.2
        
        reservar=tk.Toplevel()
        reservar.geometry("1000x600+300+150")
        reservar.title("reservar valla ")
        reservar.configure(background='white')
        fondo=tk.Frame(reservar,width="950",height="320",bg="gray93").place(x=10,y=170)
        e=tk.Label(reservar,image=photo,width="300",height="150").place(x=0,y=0)
        e1=tk.Label(reservar,text=("Gestion reserva de la valla "+'\n'+str(referencia)),font=("helvetica",19),bg="white").place(x=350,y=40)
        #creacion labels
        p1=tk.Label(reservar,text="Cliente: ",relief="raised",font=("helvetica",16)).place(x=50,y=200)
        p2=tk.Label(reservar,text="Agencia: ",relief="raised",font=("helvetica",16)).place(x=50,y=250)
        p3=tk.Label(reservar,text="Valor pauta: ",relief="raised",font=("helvetica",16)).place(x=50,y=300)
        p4=tk.Label(reservar,text="Valor con descuento: ",relief="raised",font=("helvetica",16)).place(x=420,y=200)
        p5=tk.Label(reservar,text="Duracion: ",relief="raised",font=("helvetica",16)).place(x=420,y=250)
        p6=tk.Label(reservar,text="Fecha inicio: ",relief="raised",font=("helvetica",16)).place(x=420,y=300)
        p7=tk.Label(reservar,text="Fecha final: ",relief="raised",font=("helvetica",16)).place(x=420,y=350)
        #creacion campos de entrada
        cliente=tk.Entry(reservar,font=("helvetica",14))
        #cliente.pack()
        cliente.place(x=150,y=200)
        
        agencia=tk.Entry(reservar,font=("helvetica",14))
        agencia.place(x=150,y=250)
        valorT=tk.Entry(reservar,font=("helvetica",14))
        valorT.place(x=180,y=300)
        valorD=tk.Entry(reservar,font=("helvetica",14))
        valorD.place(x=640,y=200)
        duracion=tk.Entry(reservar,font=("helvetica",14))
        duracion.place(x=550,y=250)
        fechaIni=tk.Entry(reservar,font=("helvetica",14))
        fechaIni.place(x=570,y=300)
        fechaFin=tk.Entry(reservar,font=("helvetica",14))
        fechaFin.place(x=570,y=350)


        confirmar=tk.Button(reservar, text=" Reservar ",relief="raised",font=("helvetica",16),command=hacerReserva).place(x=420,y=430)
        Volver=tk.Button(reservar, text="volver",relief="raised",command=volver,font=("helvetica",16)).place(x=50,y=430)

    else:
        messagebox.showwarning("Alerta","Debe escoger alguna opcion para continuar")
    

def hacerReserva():
    global reservar,cliente,agencia,valorT,valorD,duracion,fechaIni,fechaFin,referencia
    #obtencion de datos campos de entrada
    clienteR=cliente.get()
    agenciaR=agencia.get()
    valorSinDescuento=valorT.get()
    valorConDescuento=valorD.get()
    duracionR=duracion.get()
    fechaInicio=fechaIni.get()
    fechaFinal=fechaFin.get()
    if (clienteR and agenciaR and valorSinDescuento and valorConDescuento and duracionR and fechaInicio and fechaFinal)!="":
        arrendar.withdraw()
        #en esta funcion debemos abrir el archivo de reservas y escribir esta reserva
        #tener en cuenta que van tanto los datos del cliente como los datos de la valla (en este caso la referencia es la union)
        #podemos direccionarlo al menu de vallas y mostrarle un message box diciendo que la pauta fue exitosa
        Vallas.deiconify()
    else:
        messagebox.showwarning("Informacion incompleta","Debe llenar todos los campos para continuar")

def arrendarValla():
    global ubicacion,vAcumulado,vOcupado,vReservado,vDisponible,tVallas,infoValla,arrendar,cliente,agencia,valorT,valorD,duracion,fechaIni,fechaFin,referencia
    obtenerReferencia()
    if referencia!="":
        if ubicacion==3:
            vDisponible.withdraw()
            ubicacion=3.3
        elif ubicacion==4:
            vReservado.withdraw()
            ubicacion=4.3
        elif ubicacion==5:
            vOcupado.withdraw()
            ubicacion=5.3
        elif ubicacion==6:
            vAcumulado.withdraw()
            ubicacion=6.3
        elif ubicacion==2:
            tVallas.withdraw()
            ubicacion=2.3
        arrendar=tk.Toplevel()
        arrendar.geometry("1000x600+300+150")
        arrendar.title("reservar valla")
        arrendar.configure(background='white')
        fondo=tk.Frame(arrendar,width="950",height="320",bg="gray93").place(x=10,y=170)
        e=tk.Label(arrendar,image=photo,width="300",height="150").place(x=0,y=0)
        e1=tk.Label(arrendar,text=("Gestion arriendo de la valla "+'\n'+str(referencia)),font=("helvetica",19),bg="white").place(x=350,y=40)
        #creacion labels
        p1=tk.Label(arrendar,text="Cliente: ",relief="raised",font=("helvetica",16)).place(x=50,y=200)
        p2=tk.Label(arrendar,text="Agencia: ",relief="raised",font=("helvetica",16)).place(x=50,y=250)
        p3=tk.Label(arrendar,text="Valor pauta: ",relief="raised",font=("helvetica",16)).place(x=50,y=300)
        p4=tk.Label(arrendar,text="Valor con descuento: ",relief="raised",font=("helvetica",16)).place(x=420,y=200)
        p5=tk.Label(arrendar,text="Duracion: ",relief="raised",font=("helvetica",16)).place(x=420,y=250)
        p6=tk.Label(arrendar,text="Fecha inicio: ",relief="raised",font=("helvetica",16)).place(x=420,y=300)
        p7=tk.Label(arrendar,text="Fecha final: ",relief="raised",font=("helvetica",16)).place(x=420,y=350)
        #creacion campos de entrada
        cliente=tk.Entry(arrendar,font=("helvetica",14))
        cliente.place(x=150,y=200)
        agencia=tk.Entry(arrendar,font=("helvetica",14))
        agencia.place(x=150,y=250)
        valorT=tk.Entry(arrendar,font=("helvetica",14))
        valorT.place(x=180,y=300)
        valorD=tk.Entry(arrendar,font=("helvetica",14))
        valorD.place(x=640,y=200)
        duracion=tk.Entry(arrendar,font=("helvetica",14))
        duracion.place(x=550,y=250)
        fechaIni=tk.Entry(arrendar,font=("helvetica",14))
        fechaIni.place(x=570,y=300)
        fechaFin=tk.Entry(arrendar,font=("helvetica",14))
        fechaFin.place(x=570,y=350)
       

        #botones de manejo de pagina
        confirmar=tk.Button(arrendar, text=" Arrendar ",relief="raised",font=("helvetica",16),command=hacerPauta).place(x=420,y=430)
        Volver=tk.Button(arrendar, text="volver",relief="raised",command=volver,font=("helvetica",16)).place(x=50,y=430)

    else:
        messagebox.showwarning("Alerta","Debe escoger alguna opcion para continuar")
def hacerPauta():
    global arrendar,cliente,agencia,valorT,valorD,duracion,fechaIni,fechaFin,referencia
    #obtencion de datos campos de entrada
    clienteR=cliente.get()
    agenciaR=agencia.get()
    valorSinDescuento=valorT.get()
    valorConDescuento=valorD.get()
    duracionR=duracion.get()
    fechaInicio=fechaIni.get()
    fechaFinal=fechaFin.get()
    if (clienteR and agenciaR and valorSinDescuento and valorConDescuento and duracionR and fechaInicio and fechaFinal)!="":
        arrendar.withdraw()
        #en esta funcion debemos abrir el archivo de reservas y escribir esta reserva
        #tener en cuenta que van tanto los datos del cliente como los datos de la valla (en este caso la referencia es la union)
        #podemos direccionarlo al menu de vallas y mostrarle un message box diciendo que la pauta fue exitosa
        Vallas.deiconify()
    else:
        messagebox.showwarning("Informacion incompleta","Debe llenar todos los campos para continuar")
     
    

def eliminarReservas():
    pass
def eliminarPautas():
    pass
def renovarPautas():
    pass
def añadirValla():
    pass
def quitarValla():
    pass


def vDisponible():
    """
    Muestra las vallas disponibles con las que cuenta la empresa
    """
    global Vallas,photo,ubicacion,vDisponible
    ubicacion=3
    Vallas.withdraw()
    vDisponible=tk.Toplevel()
    vDisponible.geometry("800x600+300+150")
    vDisponible.title("Vallas disponibles")
    vDisponible.configure(background='white')
    e=tk.Label(vDisponible,image=photo,width="300",height="150").place(x=0,y=0)

    label=tk.Label(vDisponible, text="Vallas Disponibles",relief="raised",font=("Helveltica" , 18),bg="white").place(x=250,y=205)
    Ver= tk.Button(vDisponible, text=" Ver mas ", relief="raised",font=("Helveltica" , 12), command=datosValla).place(x=700,y=280)
    Mapa= tk.Button(vDisponible, text=" Ver Galeria ",relief="raised",font=("Helveltica" , 12), command=mapa).place(x=20,y=320)
    reservar= tk.Button(vDisponible, text=" Reservar Valla ",relief="raised", font=("helvetica",12),command=reservarValla).place(x=200,y=500)
    arrendar= tk.Button(vDisponible, text=" Arrendar Valla ",relief="raised", font=("helvetica",12),command=arrendarValla).place(x=450,y=500)
    combo=ttk.Combobox(vDisponible,width=108,height=10)
    combo.place(x=20,y=280)
    Volver=tk.Button(vDisponible, text="volver",relief="raised",command=volver,font=("helvetica",16)).place(x=0,y=500)


    
def vReservado():
    """
    Muestra las vallas reservadas de la empresa
    con opcion de ver mas informacion, como por el ejemplo los detalles de la pauta
    """
    global Vallas,photo,ubicacion,vReservado
    ubicacion=4
    Vallas.withdraw()
    vReservado=tk.Toplevel()
    vReservado.geometry("800x600+300+150")
    vReservado.title("Vallas reservadas")
    vReservado.configure(background='white')
    e=tk.Label(vReservado,image=photo,width="300",height="150").place(x=0,y=0)

    label=tk.Label(vReservado, text="Vallas Reservadas",font=("Helveltica" , 18),bg="white").place(x=250,y=205)
    Ver= tk.Button(vReservado, text=" Ver mas ",relief="raised", font=("Helveltica" , 12), command=datosValla).place(x=700,y=280)
    Mapa= tk.Button(vReservado, text=" Ver Galeria ",relief="raised",font=("Helveltica" , 12), command=mapa).place(x=20,y=320)
    eliminarReserva= tk.Button(vReservado, text=" Eliminar reserva ",relief="raised", font=("helvetica",12),command= eliminarReservas).place(x=200,y=500)
    arrendar= tk.Button(vReservado, text=" Arrendar Valla ",relief="raised", font=("helvetica",12),command=arrendarValla).place(x=450,y=500)
    combo=ttk.Combobox(vReservado,width=108,height=10)
    combo.place(x=20,y=280)
    Volver=tk.Button(vReservado, text="volver",relief="raised",command=volver,font=("helvetica",16)).place(x=0,y=500)

    
def vOcupado():
    """
    Muestra las vallas Arrendadas de la empresa
    con opcion de ver mas informacion, como por el ejemplo los detalles de la pauta
    """
    global Vallas, photo,ubicacion,vOcupado
    ubicacion=5
    Vallas.withdraw()
    vOcupado=tk.Toplevel()
    vOcupado.geometry("800x600+300+150")
    vOcupado.title("Vallas Arrendadas")
    vOcupado.configure(background='white')
    e=tk.Label(vOcupado,image=photo,width="300",height="150").place(x=0,y=0)

    label=tk.Label(vOcupado, text="Vallas Arrendadas",relief="raised",font=("Helveltica" , 18),bg="white").place(x=250,y=205)
    Ver= tk.Button(vOcupado, text=" Ver mas ",relief="raised", font=("Helveltica" , 12), command=datosValla).place(x=700,y=280)
    Mapa= tk.Button(vOcupado, text=" Ver Galeria ",relief="raised",font=("Helveltica" , 12), command=mapa).place(x=20,y=320)
    eliminarPauta= tk.Button(vOcupado, text=" Eliminar pauta ",relief="raised", font=("helvetica",12),command= eliminarPautas).place(x=200,y=500)
    renovarPauta= tk.Button(vOcupado, text=" renovar pauta ",relief="raised", font=("helvetica",12),command=renovarPautas).place(x=450,y=500)
    combo=ttk.Combobox(vOcupado,width=108,height=10)
    combo.place(x=20,y=280)
    Volver=tk.Button(vOcupado, text="volver",relief="raised",command=volver,font=("helvetica",16)).place(x=0,y=500)

    
def acumuladoVallas():
    """
    Muestra el total recaudo de las vallas basado en sus registros de pautas
    se pueden revisar de distintos años, aunque en algunos no hay informacion detallada
    """
    global Vallas,photo,ubicacion,vAcumulado
    ubicacion=6
    Vallas.withdraw()
    vAcumulado=tk.Toplevel()
    vAcumulado.geometry("800x600+300+150")
    vAcumulado.title("Vallas Arrendadas")
    vAcumulado.configure(background='white')
    e=tk.Label(vAcumulado,image=photo,width="300",height="150").place(x=0,y=0)
    numero=tk.Label(vAcumulado, text="numero de pautas").place(x=100,y=200)
    acumulado=tk.Label(vAcumulado, text="Dinero acumulado con descuentos").place(x=100,y=300)
    Volver=tk.Button(vAcumulado, text="volver",relief="raised",command=volver,font=("helvetica",16)).place(x=0,y=500)
    # se va a poder preguntar los acumulados de años previos a futuro se podria poner una meta y que el programa diga a cuanto se esta de dicha meta,puede ser mensual o como se quiera

def volver(): # esta funcion va a depender de donde se encuentre el usuario
    """
    Consiste en regresar a la ventana inmediatamente anterior, perdiendo los datos si no se han guardado previamente
    """
    global ubicacion,Vallas,vAcumulado,vOcupado,vReservado,vDisponible,tVallas,window,infoValla,reservar,arrendar
    #volver de paginas generales
    if ubicacion==1:
        Vallas.withdraw()
        window.deiconify()
    elif ubicacion==2:
        tVallas.withdraw()
        Vallas.deiconify()
        ubicacion=1
    elif ubicacion==3:
        vDisponible.withdraw()
        Vallas.deiconify()
        ubicacion=1
    elif ubicacion==4:
        vReservado.withdraw()
        Vallas.deiconify()
        ubicacion=1
    elif ubicacion==5:
        vOcupado.withdraw()
        Vallas.deiconify()
        ubicacion=1
    elif ubicacion==6:
        vAcumulado.withdraw()
        Vallas.deiconify()
        ubicacion=1
    #volver de informacion sobre la valla
    elif ubicacion==3.1:
        infoValla.destroy()
        vDisponible.deiconify()
        ubicacion=3
    elif ubicacion==4.1:
        infoValla.destroy()
        vReservado.deiconify()
        ubicacion=4
    elif ubicacion==5.1:
        infoValla.destroy()
        vOcupado.deiconify()
        ubicacion=5
    elif ubicacion==6.1:
        infoValla.destroy()
        vAcumulado.deiconify()
        ubicacion=6
    elif ubicacion==2.1:
        infoValla.destroy()
        tVallas.deiconify()
        ubicacion=2
    #volver de gestion reserva
    elif ubicacion==3.2:
        reservar.destroy()
        vDisponible.deiconify()
        ubicacion=3
    elif ubicacion==4.2:
        reservar.destroy()
        vReservado.deiconify()
        ubicacion=4
    elif ubicacion==5.2:
        reservar.destroy()
        vOcupado.deiconify()
        ubicacion=5
    elif ubicacion==6.2:
        reservar.destroy()
        vAcumulado.deiconify()
        ubicacion=6
    elif ubicacion==2.2:
        reservar.destroy()
        tVallas.deiconify()
        ubicacion=2
    #volver de gestion de pauta
    elif ubicacion==3.3:
        arrendar.destroy()
        vDisponible.deiconify()
        ubicacion=3
    elif ubicacion==4.3:
        arrendar.destroy()
        vReservado.deiconify()
        ubicacion=4
    elif ubicacion==5.3:
        arrendar.destroy()
        vOcupado.deiconify()
        ubicacion=5
    elif ubicacion==6.3:
        arrendar.destroy()
        vAcumulado.deiconify()
        ubicacion=6
    elif ubicacion==2.3:
        arrendar.destroy()
        tVallas.deiconify()
        ubicacion=2
        
    
def irClientes():
    window.withdraw()
    Clientes=tk.Toplevel()
    
def irSitios():
    window.withdraw()
    Sitios=tk.Toplevel()
def inicio():
    """
    construye la venatana incial y sirve de conexion con los diferentes modulos con los que cuenta la aplicación
    """
    global window,sol,luna,punto,ubicacion,referencia
    window=tk.Tk()
    leerArchivos()
    ubicacion=0
    referencia=""
    photo=tk.PhotoImage(file= 'imagenes\Logo.gif')
    sol=tk.PhotoImage(file="imagenes\sol.png")
    luna=tk.PhotoImage(file="imagenes\luna.png")
    punto=tk.PhotoImage(file=r"C:\Users\usuario\Desktop\Proyecto empresa\tkinter\imagenes\ubicacion.gif")
    e=tk.Label(window,image=photo,width="142",height="71").place(x=0,y=0)
    window.title("Publicidad Latina SAS")
    window.geometry("400x400+600+300")
    window.configure(background='white')
    e1= tk.Label(window,text="Que desea consultar",fg="black",bg="white" ,relief="flat",font=("Helveltica" , 16)).place(x=100,y=100)
    vallas =tk.Button(window, text= "vallas",width=6,height=2,relief="raised",font=("Helveltica" , 12),  command= irVallas).place(x=70,y=170)
    clientes= tk.Button(window, text= "clientes",width=6,height=2,relief="raised",font=("Helveltica" , 12),  command= irClientes).place(x=170,y=170)
    sitios = tk.Button(window, text= "sitios",width=6,height=2,relief="raised",font=("Helveltica" , 12),  command= irSitios).place(x=270,y=170)
    window.mainloop()
inicio()

    




