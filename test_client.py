import socket
print "Hello World!!!"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', 8081))
s.send("Happy Hacking!!")
data = s.recv(4096)
s.close()
print "Data Received:"
print data
