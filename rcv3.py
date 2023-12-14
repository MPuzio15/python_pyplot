import socket


def rcv():
    # Create socket and bind to address
    UDPSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    UDPSock.bind(('', 1969))
    print("UDPSock", UDPSock)

    # Receive messages

    while True:
        data, addr = UDPSock.recvfrom(1969)
        if not data:
            print("Program has exited!")
            break
        else:
            print(data.decode('utf-8').ljust(50), addr[0])
        # end
    # end

    # Close socket
    UDPSock.close()


# end def

# Send messages

rcv()
