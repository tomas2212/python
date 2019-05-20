import xmlrpclib
import time
import subprocess

client = xmlrpclib.ServerProxy("http://localhost:8001", allow_none=True)
print client.foo_handler()
print client.bar_handler()


import SocketServer
import SimpleXMLRPCServer


class SimpleThreadedXMLRPCServer(SocketServer.ThreadingMixIn, SimpleXMLRPCServer.SimpleXMLRPCServer):
    pass
  
class HandlerClass(object):
    def getTime(self):
        return time.time()

server = SimpleThreadedXMLRPCServer(("localhost",8080), allow_none = True)
server.register_introspection_functions()
server.register_instance(HandlerClass())

server.serve_forever()


def t():
    subprocess.call("date")



def fib(n):    # write Fibonacci series up to n
    a, b = 0, 1
    while b < n:
        print b,
        a, b = b, a+b

def fib2(n): # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a+b
    return result


def nova():
    print "hello"


def zorad(a,b):
    if a>b:
       return b,a
    return a,b


    
