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
    print()
    print("ENTER GAME STATE AND PARAMETERS")
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

    gsSplit = gsMsg.split()
    if (gsSplit[0] == "halt"):
        pass
    elif (gsSplit[0] == "stop"):
        pass
    elif (gsSplit[0] == "running"):
        pass
    elif (gsSplit[0] == "freekick"):
        if (len(gsSplit) != 2):
            print("invalid arguments")
            continue
        if (gsSplit[1] != "blue" and gsSplit[1] != "yellow"):
            print("invalid arguments")
            continue
    elif (gsSplit[0] == "kickoff"):
        if (len(gsSplit) != 2):
            print("invalid arguments")
            continue
        if (gsSplit[1] != "blue" and gsSplit[1] != "yellow"):
            print("invalid arguments")
            continue
    elif (gsSplit[0] == "penalty"):
        pass
    elif (gsSplit[0] == "timeout"):
        pass
    elif (gsSplit[0] == "ballplacement"):
        if (len(gsSplit) != 4):
            print("invalid arguments")
            continue
        if (gsSplit[1] != "blue" and gsSplit[1] != "yellow"):
            print("invalid arguments")
            continue
        try:
            float(gsSplit[2])
            float(gsSplit[3])
        except ValueError:
            print("invalid arguments")
            continue
    else:
        print("invalid game state")
        continue

    print("Sending gamestate and parameters", gsMsg)

    s0.sendall(gsMsg.encode())
    s1.sendall(gsMsg.encode())