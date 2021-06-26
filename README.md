# GETreqt: Multithreaded Slow DoS Attack

## Description
This is a Low & Slow Denial-of-Service attack based on incomplete and unterminated GET requests. [[Documentation in progress]]

<div align="center">
<img src="https://raw.githubusercontent.com/SHUR1K-N/GETreqt-Multithreaded-Slow-DoS-Attack/main/Images/Example%20Execution.png" >
<p>Example Execution</p>
</div>

This project was created in Python, for research purposes.

## Features


## Usage
`GETreqt.py --target example.com --port 80 --length 1024 --threads 6000 --wait`

`GETreqt.py -x example.com -p 80 -l 1024 -t 6000 -w`


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
