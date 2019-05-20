import socket

s = None
for (family, socktype, proto, canonname, sockaddr) in socket.getaddrinfo("www.fi.muni.cz", 80):
#getaddrinfo vrati list tych kombinacii 
    if (family != socket.AF_INET or socktype != socket.SOCK_STREAM):
        continue # a tu v tych ifoch si vyberieme ktoru adresu teda chceme
    s = socket.socket(family, socktype, proto) # tu sa napajame  na ten socket
    s.connect(sockaddr)
    break

f = s.makefile(mode="rw")
f.write("GET/HTTP/1.0\r\n\r\n")
f.flush()
print f.read()
#if (family in (AF_INET, AF_INET6) AND (socktype == SOCK_STREAM):
    
    


