import sys
print sys.argv[0]
HOST, PORT = sys.argv[0].split(':')[0],  sys.argv[0].split(':')[1]
print "Host: ", HOST
print "Port: ", PORT
