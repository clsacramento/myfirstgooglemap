import socket
import ssl

CONNECTION_TIMEOUT = 5
CHUNK_SIZE = 1024
HTTP_VERSION = 1.0
CRLF = "\r\n\r\n"

HOST = 'cloud.google.com'
URL_PATH ='/compute/docs/regions-zones/'

socket.setdefaulttimeout(CONNECTION_TIMEOUT)


def receive_allx(sock, chunk_size=CHUNK_SIZE):
    '''
    Gather all the data from a request.
    '''
    chunks = []
    while True:
        chunk = sock.recv(int(chunk_size))
        if chunk:
            chunks.append(chunk)
        else:
            break

    return ''.join(chunks)
 
def receive_all(sock):
    f = sock.makefile()
    data =  [] 
    for l in f:
        if '<td>' in l and '</code>' not in l and not 'b, c' in l: 
           location = l.strip().replace('<td>','').replace('</td>','').split(',')
           city = location[0]
           country = location[-1]
           data.append((city,country))
        if '/table' in l:
            break
    return data


def get_zones_locations():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(10)

    context = ssl._create_unverified_context()

    addr = (HOST, 443)

    s.connect(addr)

    ss = context.wrap_socket(s)

    ss.send('GET '+URL_PATH+' HTTP/1.0\r\nHost: '+HOST+'\r\nAccept-Charset: utf-8'+CRLF)

    data = receive_all(ss)
    ss.close()
    return data


def print_locations(table):
    for (city,country) in table:
        print city+country

print_locations(get_zones_locations())

