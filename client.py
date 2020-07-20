import socket,sys

try:
    ip = str(sys.argv[1])
    port = int(sys.argv[2])
    message = str(sys.argv[3])
except IndexError:
    print("Must Provide an IP and port and message")
    exit(2)
except ValueError:
    print("Port must be an integer")
    exit(2)

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = (ip, port)
#print('connecting to %s port %s' % server_address)
sock.connect(server_address)

try:
    # Send data
    #message = 'Alive'
    #print('sending "%s"' % message)
    sock.sendall(message.encode())

    # Look for the response
    amount_received = 0
    amount_expected = len(message)

    while amount_received < amount_expected:
        data = sock.recv(16)
        amount_received += len(data)
        print('received "%s"' % data.decode())

finally:
    #print('closing socket')
    sock.close()
