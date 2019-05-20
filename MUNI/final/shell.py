#! /usr/bin/env python2
from interface import Interface
from commands.listdir import listdir
from commands.quit import quit
from commands.titles import titles, MyThread

class Shell(object):

    COMMDICT = {}

    def __init__(self, inter):
        self.inter = inter
  
    def add_command(self, command_name, command_function):
        self.COMMDICT[command_name] = command_function

    def process(self, text):
        command, sep, arg  = text.partition(' ')
        if command in self.COMMDICT:
            return self.COMMDICT[command](arg)
        return text

    def run(self):
        while True:
            input = self.inter.read()
            try:
                result = self.process(input)
            except SystemExit:
                break
            except Exception as the_exception:
                result = "error: %s" % str(the_exception)
            if result != None:
                self.inter.write(result)

if __name__ == '__main__':
    i = Interface()
    s = Shell(i)
    myThread = MyThread(i)

    s.add_command("listdir", listdir)
    s.add_command("quit", quit)
    s.add_command("titles", titles)

    myThread.start()
    s.run()
    titles(None)
    myThread.join()




