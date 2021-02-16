import socket

HOST_0 = 'localhost'
HOST_1 = 'localhost'

PORT_0 = 6543
PORT_1 = 6544

s0 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s0.connect((HOST_0, PORT_0))
s1.connect((HOST_1, PORT_1))

while True:
    print("ENTER GAME STATE AND PARAMETERS\n")
    print("halt")
    print("stop")
    print("running")
    print("freekick <team>")
    print("kickoff <team>")
    print("penalty")
    print("timeout")
    print("ballplacement <team> <target pos x> <target pos y>")
    print(">>> ", end='')
    
    gsMsg = input() + '\n'

    print("Sending gamestate and parameters", gsMsg)

    s0.sendall(gsMsg.encode())
    s1.sendall(gsMsg.encode())