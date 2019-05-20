class Interface(object): # contains read() and write(msg)
    """Represents Interface for IO read and write. """

    def read(self):
        return raw_input(">>> ")

    def write(self, msg):
        print msg
