import socket

def is_valid_ip(ip):
    try:
        socket.inet_aton(ip)
        return True
    except socket.error:
        return False

ip_address = input("Enter an IP address: ")

if is_valid_ip(ip_address):
    print("Valid IP Address.")
else:
    print("Invalid IP Address.")