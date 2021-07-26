# https://github.com/baptisteCanac/findWebsiteIp
import socket as s

host = input("entrez une adresse : ")
print("ip of", host, "is", s.gethostbyname_ex(host))