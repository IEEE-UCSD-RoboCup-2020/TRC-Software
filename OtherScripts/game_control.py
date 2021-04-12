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
    print("HALT")
    print("STOP")
    print("NORMAL_START")
    print("FORCE_START")
    print("PREPARE_KICKOFF_YELLOW")
    print("PREPARE_KICKOFF_BLUE")
    print("PREPARE_PENALTY_YELLOW")
    print("PREPARE_PENALTY_BLUE")
    print("DIRECT_FREE_YELLOW")
    print("DIRECT_FREE_BLUE")
    print("INDIRECT_FREE_YELLOW")
    print("INDIRECT_FREE_BLUE")
    print("TIMEOUT_YELLOW")
    print("TIMEOUT_BLUE")
    print("BALL_PLACEMENT_BLUE <target pos x> <target pos y>")
    print("BALL_PLACEMENT_YELLOW <target pos x> <target pos y>")
    print(">>> ", end='')
    
    gsMsg = input() + '\n'

    gsSplit = gsMsg.split()
    if (gsSplit[0] == "HALT"):
        pass
    elif (gsSplit[0] == "STOP"):
        pass
    elif (gsSplit[0] == "NORMAL_START"):
        pass
    elif (gsSplit[0] == "FORCE_START"):
        pass
    elif (gsSplit[0] == "PREPARE_KICKOFF_YELLOW"):
        pass
    elif (gsSplit[0] == "PREPARE_KICKOFF_BLUE"):
        pass
    elif (gsSplit[0] == "PREPARE_PENALTY_YELLOW"):
        pass
    elif (gsSplit[0] == "PREPARE_PENALTY_BLUE"):
        pass
    elif (gsSplit[0] == "DIRECT_FREE_YELLOW"):
        pass
    elif (gsSplit[0] == "DIRECT_FREE_BLUE"):
        pass
    elif (gsSplit[0] == "INDIRECT_FREE_YELLOW"):
        pass
    elif (gsSplit[0] == "INDIRECT_FREE_BLUE"):
        pass
    elif (gsSplit[0] == "TIMEOUT_YELLOW"):
        pass
    elif (gsSplit[0] == "TIMEOUT_BLUE"):
        pass
    elif (gsSplit[0] == "BALL_PLACEMENT_BLUE"):
        if (len(gsSplit) != 3):
            print("invalid arguments")
            continue
        try:
            float(gsSplit[1])
            float(gsSplit[2])
        except ValueError:
            print("invalid arguments")
            continue
    elif (gsSplit[0] == "BALL_PLACEMENT_YELLOW"):
        if (len(gsSplit) != 3):
            print("invalid arguments")
            continue
        try:
            float(gsSplit[1])
            float(gsSplit[2])
        except ValueError:
            print("invalid arguments")
            continue
    else:
        print("invalid game state")
        continue

    print("Sending gamestate and parameters", gsMsg)

    s0.sendall(gsMsg.encode())
    s1.sendall(gsMsg.encode())