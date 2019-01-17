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
import time,calendar


ubicacion=0  #ubicacion 0 menu,1 menu valla,2 valla especifico,
    
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
    ubicacion=1
    photo=tk.PhotoImage(file= 'imagenes\LogoM.gif')
    window.withdraw()
    Vallas=tk.Toplevel()
    Vallas.geometry("800x600+300+150")
    Vallas.title("Vallas")
    Vallas.configure(background='white')
    e=tk.Label(Vallas,image=photo,width="300",height="150").place(x=0,y=0)
    tVallas =tk.Button(Vallas, text= " todas las vallas",width=12,height=2,font=("Helveltica" , 12), command= vallasT).place(x=80,y=220)
    vallasD= tk.Button(Vallas, text= "Vallas disponibles",width=14,height=2,font=("Helveltica" , 12),  command= vDisponible).place(x=210,y=220)
    vallasR = tk.Button(Vallas, text= "Vallas reservadas",width=14,height=2,font=("Helveltica" , 12),  command= vReservado).place(x=360,y=220)
    vallasA = tk.Button(Vallas, text= "Vallas arrendadas",width=14,height=2,font=("Helveltica" , 12),  command= vOcupado).place(x=510,y=220)
    aVallas=tk.Button(Vallas, text= "Acumulado Vallas",width=14,height=2,font=("Helveltica" , 12),  command= acumuladoVallas).place(x=290,y=330) # muestra un acumulado de las ganacias netas del total de vallas
    Volver=tk.Button(Vallas, text="volver",command=volver).place(x=0,y=500)# la funcion de volver tendra diferentes condicionales dependiendo de donde se encuentre el usuario

def vallasT():
    """
    Muestra todas las vallas con las que se cuenta para ofrecer al mercado
    NO muestra en que estado se encuetra la valla
    """
    global Vallas,photo,vallasTotal
    Vallas.withdraw()
    tVallas=tk.Toplevel()
    tVallas.geometry("800x600+300+150")
    tVallas.title("Todas las vallas")
    tVallas.configure(background='white')
    ###### botones y etiquetas####
    e=tk.Label(tVallas,image=photo,width="300",height="150").place(x=0,y=0)
    label=tk.Label(tVallas, text="Listado de Vallas",font=("Helveltica" , 18),bg="white").place(x=250,y=205)
    Ver= tk.Button(tVallas, text=" Ver mas ", font=("Helveltica" , 12), command=datosValla).place(x=700,y=280)
    Mapa= tk.Button(tVallas, text=" Ver mapa ",font=("Helveltica" , 12), command=mapa).place(x=20,y=320)
    reservar= tk.Button(tVallas, text=" Reservar Valla ", font=("helvetica",12),command=reservarValla).place(x=200,y=500)
    arrendar= tk.Button(tVallas, text=" Arrendar Valla ", font=("helvetica",12),command=arrendarValla).place(x=450,y=500)
    combo=ttk.Combobox(tVallas,width=108,height=10)
    combo.place(x=20,y=280)
    ### ciclo para mostrar las vallas en el combobox ###
    for i in vallasTotal["vallasT"]:
        i[0]="Dirección: "+ str(i[0])
        i[1]="Referencia: " +str(i[1])
        i[2]="Sentido: "+ str(i[2])
        i[5]="Valor: "+ str(i[5])
    combo["values"]=vallasTotal["vallasT"]
    
#### detalles de paginas  ####
def mapa():
    pass
def datosValla():
    pass
def reservarValla():
    pass
def arrendarValla():
    pass
def eliminarR():
    pass
def eliminarP():
    pass
def renovarP():
    pass
def añadirValla():
    pass
def quitarValla():
    pass


def vDisponible():
    """
    Muestra las vallas disponibles con las que cuenta la empresa
    """
    global Vallas,photo
    Vallas.withdraw()
    vDisponible=tk.Toplevel()
    vDisponible.geometry("800x600+300+150")
    vDisponible.title("Vallas disponibles")
    vDisponible.configure(background='white')
    e=tk.Label(vDisponible,image=photo,width="300",height="150").place(x=0,y=0)

    label=tk.Label(vDisponible, text="Vallas Disponibles",font=("Helveltica" , 18),bg="white").place(x=250,y=205)
    Ver= tk.Button(vDisponible, text=" Ver mas ", font=("Helveltica" , 12), command=datosValla).place(x=700,y=280)
    Mapa= tk.Button(vDisponible, text=" Ver mapa ",font=("Helveltica" , 12), command=mapa).place(x=20,y=320)
    reservar= tk.Button(vDisponible, text=" Reservar Valla ", font=("helvetica",12),command=reservarValla).place(x=200,y=500)
    arrendar= tk.Button(vDisponible, text=" Arrendar Valla ", font=("helvetica",12),command=arrendarValla).place(x=450,y=500)
    combo=ttk.Combobox(vDisponible,width=108,height=10)
    combo.place(x=20,y=280)


    
def vReservado():
    """
    Muestra las vallas reservadas de la empresa
    con opcion de ver mas informacion, como por el ejemplo los detalles de la pauta
    """
    global Vallas,photo
    Vallas.withdraw()
    vReservado=tk.Toplevel()
    vReservado.geometry("800x600+300+150")
    vReservado.title("Vallas reservadas")
    vReservado.configure(background='white')
    e=tk.Label(vReservado,image=photo,width="300",height="150").place(x=0,y=0)

    label=tk.Label(vReservado, text="Vallas Reservadas",font=("Helveltica" , 18),bg="white").place(x=250,y=205)
    Ver= tk.Button(vReservado, text=" Ver mas ", font=("Helveltica" , 12), command=datosValla).place(x=700,y=280)
    Mapa= tk.Button(vReservado, text=" Ver mapa ",font=("Helveltica" , 12), command=mapa).place(x=20,y=320)
    eliminarReserva= tk.Button(vReservado, text=" Eliminar reserva ", font=("helvetica",12),command= eliminarR).place(x=200,y=500)
    arrendar= tk.Button(vReservado, text=" Arrendar Valla ", font=("helvetica",12),command=arrendarValla).place(x=450,y=500)
    combo=ttk.Combobox(vReservado,width=108,height=10)
    combo.place(x=20,y=280)
def vOcupado():
    """
    Muestra las vallas Arrendadas de la empresa
    con opcion de ver mas informacion, como por el ejemplo los detalles de la pauta
    """
    global Vallas, photo
    Vallas.withdraw()
    vOcupado=tk.Toplevel()
    vOcupado.geometry("800x600+300+150")
    vOcupado.title("Vallas Arrendadas")
    vOcupado.configure(background='white')
    e=tk.Label(vOcupado,image=photo,width="300",height="150").place(x=0,y=0)

    label=tk.Label(vOcupado, text="Vallas Arrendadas",font=("Helveltica" , 18),bg="white").place(x=250,y=205)
    Ver= tk.Button(vOcupado, text=" Ver mas ", font=("Helveltica" , 12), command=datosValla).place(x=700,y=280)
    Mapa= tk.Button(vOcupado, text=" Ver mapa ",font=("Helveltica" , 12), command=mapa).place(x=20,y=320)
    eliminarPauta= tk.Button(vOcupado, text=" Eliminar pauta ", font=("helvetica",12),command= eliminarP).place(x=200,y=500)
    renovarPauta= tk.Button(vOcupado, text=" renovar pauta ", font=("helvetica",12),command=renovarP).place(x=450,y=500)
    combo=ttk.Combobox(vOcupado,width=108,height=10)
    combo.place(x=20,y=280)

    
def acumuladoVallas():
    """
    Muestra el total recaudo de las vallas basado en sus registros de pautas
    se pueden revisar de distintos años, aunque en algunos no hay informacion detallada
    """
    global Vallas,photo
    Vallas.withdraw()
    vAcumulado=tk.Toplevel()
    vAcumulado.geometry("800x600+300+150")
    vAcumulado.title("Vallas Arrendadas")
    vAcumulado.configure(background='white')
    e=tk.Label(vAcumulado,image=photo,width="300",height="150").place(x=0,y=0)
    numero=tk.Label(vAcumulado, text="numero de pautas").place(x=100,y=200)
    acumulado=tk.Label(vAcumulado, text="Dinero acumulado con descuentos").place(x=100,y=300)
    # se va a poder preguntar los acumulados de años previos a futuro se podria poner una meta y que el programa diga a cuanto se esta de dicha meta,puede ser mensual o como se quiera
def volver(): # esta funcion va a depender de donde se encuentre el usuario
    """
    Consiste en regresar a la ventana inmediatamente anterior, perdiendo los datos si no se han guardado previamente
    """
    global ubicacion
    inicio()
    
        

    
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
    global window
    window=tk.Tk()
    leerArchivos()
    photo=tk.PhotoImage(file= 'imagenes\Logo.gif')
    e=tk.Label(window,image=photo,width="142",height="71").place(x=0,y=0)
    window.title("Publicidad Latina SAS")
    window.geometry("400x400+600+300")
    window.configure(background='white')
    e1= tk.Label(window,text="Que desea consultar",fg="black",bg="white" ,font=("Helveltica" , 16)).place(x=100,y=100)
    vallas =tk.Button(window, text= "vallas",width=6,height=2,font=("Helveltica" , 12),  command= irVallas).place(x=70,y=170)
    clientes= tk.Button(window, text= "clientes",width=6,height=2,font=("Helveltica" , 12),  command= irClientes).place(x=170,y=170)
    sitios = tk.Button(window, text= "sitios",width=6,height=2,font=("Helveltica" , 12),  command= irSitios).place(x=270,y=170)
    window.mainloop()
inicio()

    




