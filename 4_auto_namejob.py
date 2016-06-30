#! /usr/bin/python2

import os 

### Configuring the Namenode
f = open("/root/Desktop/Outputs/namenode.txt","r");

for i in f.readlines():
	
	i=i.strip()
	
	###Copying to target PC
	b = os.system("sshpass -p 'redhat' scp /root/Desktop/namenode.py /root/Desktop/Outputs/namenode.txt root@"+str(i)+":/root/Desktop")
	
	if b == 0 :	
		print ("\n*****  COPIED TO "+i)
	
	###Running Config Script on target PC	
	a = os.system("sshpass -p 'redhat' ssh -o StrictHostKeyChecking=no -X root@"+str(i)+" \"python /root/Desktop/namenode.py\"")
	
	if a == 0 :	
		print("\n\n*****  "+i+" IS NOW A NAMENODE . . .")
	else :
		print("Please Try Again Later . . .")
		exit()


### Configuring the Job Tracker		
f = open("/root/Desktop/Outputs/jobtracker.txt","r");

for i in f.readlines():
	
	i=i.strip()
	
	###Copying to target PC
	b = os.system("sshpass -p 'redhat' scp /root/Desktop/jobtracker.py /root/Desktop/Outputs/namenode.txt /root/Desktop/Outputs/jobtracker.txt root@"+str(i)+":/root/Desktop")
	
	if b == 0 :	
		print ("\n*****  COPIED TO "+i)
	
	###Running Config Script on target PC	
	a = os.system("sshpass -p 'redhat' ssh -o StrictHostKeyChecking=no -X root@"+str(i)+" \"python /root/Desktop/jobtracker.py\"")
	
	if a == 0 :	
		print("\n\n*****  "+i+" IS NOW A JOB TRACKER . . .")

raw_input("#####  CONFIGURED NAME NODE & JOB TRACKER  #####")
