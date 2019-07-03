import socket
import sys
import traceback


def server(log_buffer=sys.stderr):
    # set an address for our server
    address = ('127.0.0.1', 10000)
    with socket.socket(socket.AF_INET,
                       socket.SOCK_STREAM,
                       socket.IPPROTO_TCP) as sock:

        print("making a server on {0}:{1}".format(*address), file=log_buffer)

        sock.bind(address)
        sock.listen(1)

        try:
            while True:
                print('waiting for a connection', file=log_buffer)
                conn, addr = sock.accept()
                try:
                    while True:
                        data = conn.recv(16)
                        print('received "{0}"'.format(data.decode('utf8')))

                        conn.sendall(data)
                        print('sent "{0}"'.format(data.decode('utf8')))

                        if len(data) < 16:
                            break

                except Exception as e:
                    traceback.print_exc()
                    sys.exit(1)

                finally:
                    conn.close()
                    print(
                        'echo complete, client connection closed', file=log_buffer
                    )

        except KeyboardInterrupt:
            sock.close()
            print('quitting echo server', file=log_buffer)


if __name__ == '__main__':
    server()
    sys.exit(0)
