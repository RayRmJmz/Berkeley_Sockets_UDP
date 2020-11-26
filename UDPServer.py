import socket

 

localIP     = "127.0.0.1"

localPort   = 20001

bufferSize  = 1024

 

msgFromServer       = "Hello UDP Client"

bytesToSend         = str.encode(msgFromServer)

 

# Create a datagram socket
# socket (domain, type, protocol)

UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

 

# Bind to address and ip

UDPServerSocket.bind((localIP, localPort))

 

print("\n UDP server up and listening\n")

 

# Listen for incoming datagrams

while(True):

    bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)

    # [0=>message, 1=>address]

    message = bytesAddressPair[0]

    address = bytesAddressPair[1]

    print( bytesAddressPair)
    clientMsg = "Message from Client:{}".format(message)
    clientIP  = "Client IP Address:{}".format(address)
    
    print(clientMsg)
    print(clientIP)
   
    print("\n******************************")
    print("UDP Server listening....")
    print("****************************** \n")

   

    # Sending a reply to client

    UDPServerSocket.sendto(bytesToSend, address)