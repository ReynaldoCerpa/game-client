import socketio
import eventHandlers.events as events

ipaddress = ""
port = ""
username = ""
sio = socketio.Client()

def serverAddress():
    global ipaddress, port, username, sio

    ipaddress = input("Ingrese la ip del servidor: ")
    port = input("ingrese el puerto del servidor: ")
    username = input("ingrese su nombre de usuario: ")

    try:
        events.connected(sio)
        sio.connect("http://"+ipaddress+":"+port)
    except:
        print("No se encontró el servidor...")
        serverAddress()

serverAddress()
