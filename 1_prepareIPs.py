#! /usr/bin/python2

import os

###Create an Outputs Folder to store the intermediate data
#os.system("mkdir /root/Desktop/Outputs")

###Checking for NMAP and SSHPASS installation. Install if not.
n=os.system("rpm -q nmap sshpass")
if n != 0:
	os.system("yum install nmap sshpass -y")

os.system("rm -rf Outputs/ ;mkdir /root/Desktop/Outputs")

###Mapping all IPs
os.system("""nmap -sP 192.168.0.0/24 | grep 192* | awk '{print $6}' | cut -f2 -d"(" | cut -f1 -d")" | grep 192* > /root/Desktop/Outputs/ALL_IPs.txt""")

print ("Output File Generated ...\nFiltering IPs ...")

f=open('/root/Desktop/Outputs/ALL_IPs.txt','r')
f.seek(0)


###Checking if ssh works for the IPs in ALL_IPs.txt 
###They should have eth0 named LAN card
for i in f.readlines():
	
	i=i.strip()
	a=os.system("sshpass -p 'redhat' ssh -o StrictHostKeyChecking=no root@"+str(i)+" ifconfig eth0")
	
	#If yes, then store them in preparedIPs.txt
	if a == 0 :
		
		g=open("/root/Desktop/Outputs/preparedIPs.txt","a+")
		g.write(i+"\n")
		g.close()

###Displaying all the available IP Addresses
os.system("clear")
h=open('/root/Desktop/Outputs/preparedIPs.txt','r')
h.seek(0)
for i in h.readlines():
	i.split()	
	print i

raw_input("... are the IPs that are currently available for use.")
