#DANIEL HENGSTENBERG 17201    |       LUIS ROBERTO 17337
#PROYECTO NUMERO 2
#MICROCONTROLADORES
#

#-----Importamos_librerias-----
from tkinter import *
import serial
import time
import sys

bandera = False
#############################3 serial####################
#ser = serial.Serial(port='COM4',baudrate=9600,parity=serial.PARITY_NONE,stopbits=serial.STOPBITS_ONE,bytesize=serial.EIGHTBITS,timeout=0)
#--------VARIABLES
servoM=0            # datos del angulo actual
voltaje_pic = 0
procesado=chr(0)

#-------------ventana 
ventana=Tk()

#-------------Icono 
bit=ventana.iconbitmap("icono3.ico")

#------------Titulo------------
ventana.title("--PROYECTO--")


#------------Tamanio 
ventana.resizable(0,0)
ventana.geometry("400x400")


#------------Frame 

frame=Frame()
frame.pack()
frame.config(width="400",height="400")

#-----------Fondo 
imagen=PhotoImage(file="fondo4.gif")
fondo=Label(frame,image=imagen).place(x=-2,y=-2)

#------------label
nombres=Label(frame,text="Daniel Hengstenberg 17201 - Luis Roberto Salazar 17337",fg="white",bg="black")
nombres.place(x=0,y=0)

voltajeservo=Label(frame,text="Voltaje servo-motorD",font="times",fg="white",bg="black")
voltajeservo.place(x=10,y=170)

#-------------cuadro de voltaje
servo=Label(frame,text="0",font=("impact",50),fg="green",bg="black")    #servo=Label(frame,text=str(salida),font=("impact",50),fg="green",bg="black")  /textvariable
servo.place(x=30,y=210)


#-----------Funcion de Botones 

def codigoBoton():
    angulo=anguloNuevo.get()    #agarra la variable ingresada en el cuadro de angulo 
    grados=int(angulo)

    mapeo = (grados*33/180)
    print (mapeo)
    mapeoGrados = int(mapeo)
    procesado = chr(mapeoGrados)
    ser.write(procesado)
    print("se ha procesado el nuevo Ángulo")

def grabar():
    archivo = open("datos.txt", "w")
    bandera = True
    while bandera:
        ser.flushInput()
        ser.flushOutput()
        time.sleep(.3)
        recibido = ser.read()
        #ser.write(recibido)
        numero = ord(recibido)
        archivo.write(str(numero))
    archivo.close()

def parar():
    bandera = False

def simular():
    archivo = open("datos.txt", "r")
    for line in arhivo:
        numero = ord(line)
          
        

def on1():
    print("Estado: On")

def off1():
    print("Estado: off")

        
#-----------checkeo de botones
on=Radiobutton(frame,text="On",value=1,variable=1,command=on1,font="times",fg="green",bg="black")
on.place(x=20,y=50)
off=Radiobutton(frame,text="OFF",value=2,variable=1,command=off1,font="times",fg="red",bg="black")
off.place(x=20,y=90)

#---------------Botones
grabar=Button(frame,text="Grabar",command=grabar,font=("impact",20),fg="green",bg="black")
grabar.place(x=100,y=50)
parar=Button(frame,text="Parar",command=parar,font=("impact",20),fg="green",bg="black")
parar.place(x=200,y=50)
simular=Button(frame,text="Simular",command=simular,font=("impact",20),fg="green",bg="black")
simular.place(x=285,y=50)

#COMUNICACION SERIAL DE PIC CON LA CUMPU
#ser= serial.Serial(port='COM4',baudrate=9600, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE,bytesize=serial.EIGHTBITS, timeout=0)
#while 1:
#    ser.flushInput()
#    ser.flushOutput()
#    time.sleep(.3)
#    recibido1=ser.read()
#    try:
#        numero =ord(recibido1)
#        numero =float(numero)
#        numero =(numero*5.0)/31.0          
#        servo.config(text=numero)
#        print(round(numero,2))
#        
#
#    except TypeError:
#        print("error")
    
ventana.update()



