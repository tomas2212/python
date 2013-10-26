class Prumer(object):
    def __init__(self, value = 0):
        self.value = value
        self.counter = 0

    def __str__(self):
        return "Priemer je {self.value}/{self.counter}".format(self = self)     

    @property
    def my_attr(self):
        return self.value/self.counter

    @my_attr.setter
    def my_attr(self, value):
        self.value += value
        self.counter += 1