
def sioEvents(sio):
    @sio.event
    def message(data):
        print("got a message")

    @sio.event
    def connect():
        print("I'm connected!")

    @sio.event
    def connect_error(data):
        print("The connection failed!")

    @sio.event
    def disconnect():
        print("I'm disconnected!")


