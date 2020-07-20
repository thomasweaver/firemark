import socket,sys

try:
    port = int(sys.argv[1])
except IndexError as e:
    print("Must Provide port to listen on")
    exit(2)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


server_address = ('0.0.0.0', port)
print('starting up on %s port %s' % server_address)

sock.bind(server_address)

sock.listen(1)

while True:
    # Wait for a connection
    print('waiting for a connection')
    connection, client_address = sock.accept()
    try:
        print('connection from', client_address)

        # Receive the data in small chunks and retransmit it
        while True:
            data = connection.recv(16)
            print('received "%s"' % data)
            if data:
                print('sending data back to the client')
                connection.sendall(data)
            else:
                print('no more data from', client_address)
                break
    finally:
        # Clean up the connection
        connection.close()
