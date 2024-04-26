import socket


if __name__ == '__main__':
    mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # host, port
    mysocket.connect(('data.pr4e.org', 80))

    # Page1
    # cmd = 'GET http://data.pr4e.org/page1.htm HTTP/1.0\r\n\r\n'.encode()

    # Page2 -> .encode() to translate from unicode to utf-8
    cmd = 'GET http://data.pr4e.org/page2.htm HTTP/1.0\r\n\r\n'.encode()
    mysocket.send(cmd)

    while True:
        data = mysocket.recv(512)
        if len(data) < 1:
            break

        # .decode() to transfer from utf-8 to unicode
        print(data.decode(), end='')

    mysocket.close()
