

# @sio.event
# def message(data):
    # print("got a message")

def connected(sio):
    @sio.event
    def connect():
        print("Conexión exitosa.")

# @sio.event
# def connect_error(data):
    # print("The connection failed!")

# @sio.event
# def disconnect():
    # print("I'm disconnected!")


