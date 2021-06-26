# GETreqt: Multithreaded Slow DoS Attack

## Description
A unique, multithreaded Low & Slow denial-of-service attack against vulnerable versions of Apache-based web servers, that exhausts server resources at the cost of minimal bandwidth at the attacker’s end while denying typical service to the web server’s legitimate clients. This unique approach uses staggering amounts of concurrently generated non-terminated HTTP GET requests, and works against even poorly implemented load balancing proxy servers as well! [[Documentation in progress]]

<div align="center">
<img src="https://raw.githubusercontent.com/SHUR1K-N/GETreqt-Multithreaded-Slow-DoS-Attack/main/Images/Example%20Execution.png" >
<p>Example Execution</p>
</div>

This project was created in Python, for research purposes.

## Features


## Usage
<div align="center">

`GETreqt.py --target example.com --port 80 --length 1024 --threads 6000 --wait`

`GETreqt.py -x example.com -p 80 -l 1024 -t 6000 -w`


|Option | What It Means|
|---|---|
|target | Target web server address (IP or URL)|
|port | Target web server port (eg: 80)|
length | Total packet length (eg: 1000)|
threads | Threads (sockets) to attack through (eg: 6000)|
end | Terminate all requests correctly (blatant GET spam)|
wait | Unterminated requests (elegant slow DoS)|

</div>

### What GETreqt Does
1. Creates the specified number of software threads simultaneously — these will be the sockets
2. Creates unterminated GET request headers to be sent via all these created sockets
3. Sends the unterminated GET requests to the target web server using all these created sockets simultaneously
4. When a socket dies or a thread is freed up on the server's side, more sockets are created and more GET requests are sent via them
5. This goes on until the script is killed or the specified length of the entire request reaches its end


## Dependencies to PIP-Install
- **colorama** (for colors)
- **termcolor** (for colors)

------------

My website: https://TheComputerNoob.com
