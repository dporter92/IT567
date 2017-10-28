# IT567
portscanner.py

This file runs as follows:

python portscanner.py -h
  Displays the options

python portscanner.py -t 192.168.0.111 -p 22
  Runs for target 192.168.0.111 and checks only port 22

python portscanner.py -t 192.168.0.111,192.168.0.1 -p 22,80,445
  Runs for both targets and the ports specified. NO SPACES BETWEEN PORTS OR TARGETS, JUST THE COMMA

python portscanner.py -t 192.168.0.111 -r
  Runs for the target(s) and goes into the range option. Will ask for a range that you will type in
  ex. Start port: 0
      End port: 1000
