import socket


def ip2nome(ip):
    try:
        return socket.gethostbyaddr(".".join(ip))[0]
    except socket.herror:
        return None