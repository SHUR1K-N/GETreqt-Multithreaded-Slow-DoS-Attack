# GETreqt (Get-Wrecked): Multithreaded Slow DoS Attack

## Description
A unique, multithreaded Low & Slow denial-of-service (Slow DoS) attack against web servers that use vulnerable versions of thread-based web server software, that denies typical service to the web server’s legitimate clients by exhausting server resources at the cost of minimal bandwidth at the attacker's end.

This unique approach uses staggering amounts of concurrently generated HTTP GET requests even while the other sockets are being created and established on-the-go, and is effective even against poorly implemented mitigation mechanisms such as load balancing proxy servers.

<div align="center">
<img src="https://raw.githubusercontent.com/SHUR1K-N/GETreqt-Multithreaded-Slow-DoS-Attack/main/Images/Example%20Execution.png" >
<p>Example Execution</p>
</div>

This project was created in Python, to supplement my Computer Science engineering degree's final-year research project titled "Low & Slow: The Evil Twin of DDoS Attacks", which was an awareness-based project. This project received the title of "The Best Project of Its Year" by the university.

#### Web servers tested so far & confirmed as vulnerable:

- Apache 1.x
- Apache 2.x

#### Web servers untested so far & theoretically vulnerable:
- BeeWare WAF
- DenyAll WAF
- dhttpd
- Flask
- GoAhead WebServer
- Trapeze Wireless Web Portal
- WebSense "block pages"

#### Web servers theoretically invulnerable or not completely vulnerable:
- Cherokee
- Cisco CSS
- IIS6.0
- IIS7.0
- lighttpd
- Netscaler
- nginx
- Squid

*You may test other file extensions/types and report them as supported/unsupported to update this list in the future.*

## Usage
<div align="center">

`GETreqt.py --target example.com --port 80 --length 1024 --threads 6000 --wait`

`GETreqt.py -x example.com -p 80 -l 1024 -t 6000 -w`

OR

`GETreqt.py --target example.com --port 80 --length 1024 --threads 10000 --end`

`GETreqt.py -x example.com -p 80 -l 1024 -t 10000 -e`


|Option       |Description                                          |
|-------------|-----------------------------------------------------|
|target (-x)  | Target web server address (IP address or URL)       |
|port (-p)    | Target web server port (eg: 80)                     |
|length (-l)  | Total packet length (eg: 1000)                      |
|threads (-t) | Threads (sockets) to attack with (eg: 6000)         |
|wait (-w)    | Do not terminate requests (elegant slow DoS)        |
|end (-e)     | Terminate all requests correctly (blatant GET spam) |

</div>

## What GETreqt Does
### Using the `--wait` option
1. The specified number of client-side software threads (--threads) are created — these would serve as the individual sockets established between the client and server

2. *Unterminated* GET request headers are created to be sent via all these created sockets

3. As this large number of sockets are being created and established, the *unterminated* GET requests are concurrently sent to the target web server using whatever sockets are already established presently

4. When a socket dies or a server-side thread is freed up (unoccupied), additional sockets are concurrently created and established to maximize the number of occupied server-side threads

5. Steps #3 and #4 remain active until either the script is killed, or the specified length of the entire request (--length) reaches its end, or the server crashes

<div align="center">
<img src="https://raw.githubusercontent.com/SHUR1K-N/GETreqt-Multithreaded-Slow-DoS-Attack/main/Images/Unterminated.png" >
<p>Sending Unterminated Requests</p>
</div>

### Using the `--end` option
1. The specified number of client-side software threads (--threads) are created — these would serve as the individual sockets established between the client and server

2. *Terminated* GET request headers are created to be sent via all these created sockets

3. As this large number of sockets are being created and established, the *terminated* GET requests are concurrently sent to the target web server using whatever sockets are already established presently

4. When a socket dies or a server-side thread is freed up (unoccupied), additional sockets are concurrently created and established to maximize the number of occupied server-side threads

5. Steps #3 and #4 remain active until either the script is killed, or the specified length of the entire request (--length) reaches its end, or the server crashes

<div align="center">
<img src="https://raw.githubusercontent.com/SHUR1K-N/GETreqt-Multithreaded-Slow-DoS-Attack/main/Images/Terminated.png" >
<p>Sending Terminated Requests</p>
</div>

### Results
When the server-side threads that are explicitly assigned to be serving clients are completely occupied by GETreqt's flood of terminated or unterminated GET requests, a legitimate client would fail to connect with the web server due to an insufficient amount of available threads on the server-side to be serving this client. This will result in the "Waiting for \<target host\>" message as the web browser anticipates a connection but never establishes one:

<div align="center">
<img src="https://raw.githubusercontent.com/SHUR1K-N/GETreqt-Multithreaded-Slow-DoS-Attack/main/Images/Waiting.png" >
<p>Waiting...</p>
</div>

Further, upon waiting for a long enough amount of time, the web browser gives up as the server-side threads are completely occupied serving the attacker's requests. This is when the "ERR_CONNECTION_TIMED_OUT" error message is displayed:

<div align="center">
<img src="https://raw.githubusercontent.com/SHUR1K-N/GETreqt-Multithreaded-Slow-DoS-Attack/main/Images/ERR_CONNECTION_TIMED_OUT.png" >
<p>ERR_CONNECTION_TIMED_OUT</p>
</div>

## Disclaimer
GETreqt was created for the purposes of education, research, and inspiring awareness regarding organizations using vulnerable web server software versions. I neither endorse nor shall be held responsible for any potential unethical or malicious activity that is a result of *your* usage of GETreqt.

## Dependencies to PIP-Install
- **colorama** (for colors)
- **termcolor** (for colors)

------------

My website: https://TheComputerNoob.com
