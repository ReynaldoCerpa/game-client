import socketio
from eventHandlers.events import sioEvents

ipaddress = input("Ingrese la ip del servidor: ")
port = input("ingrese el puerto del servidor: ")

sio = socketio.Client()

sioEvents(sio)

sio.connect("http://"+ipaddress+":"+port)
