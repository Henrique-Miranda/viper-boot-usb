from selectDevice import selectDevice

class App(object):
    def __init__(self):
        self.sDevice = selectDevice()
        self.dPath = self.sDevice['path']



app = App()