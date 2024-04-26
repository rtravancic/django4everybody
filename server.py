from socket import *


def create_server():
    serversocket = socket(AF_INET, SOCK_STREAM)

    try:
        serversocket.bind(('localhost', 9000)) # port 9000, localhost, ne moze vise bit na istom portu
        serversocket.listen(5) # hold up to 5 connections

        while(True):
            (clientsocket, address) = serversocket.accept() # ovo je blokirajuce sve dok ne primi tu stoji
            rd = clientsocket.recv(5000).decode() # samo kada je veza uspostavljena
            pieces = rd.split("\n")

            if len(pieces) > 0: print(pieces[0])

            data  = "HTTP/1.1 200 OK\r\n"
            data += "Content-Type: text/html; charset=utf-8\r\n"
            data += "\r\n"
            data += "<html><body> Aloha </body> </html>\r\n\r\n"
            clientsocket.sendall(data.encode())
            clientsocket.shutdown(SHUT_WR)

    except KeyboardInterrupt:
        print("Shutting down...")
    except Exception as exc:
        print("Error:\n")
        print(exc)

    serversocket.close()


print("Access http://localhost:9000")
create_server()

