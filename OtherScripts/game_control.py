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
    print("Enter game state (halt, stop, running, freekick, kickoff, penalty, timeout, ballplacement):")
    gs = input() + '\n'
    print("Setting game state to ", gs)

    s0.sendall(gs.encode())
    s1.sendall(gs.encode())