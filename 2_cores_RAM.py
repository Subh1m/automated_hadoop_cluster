#!/usr/bin/python2

import os;

print ("\nSorting based on Cores and RAM . . .\n")

f = open("/root/Desktop/Outputs/preparedIPs.txt","r");

for i in f.readlines():
	
	i=i.strip()

	print i

	###Creating file with IPs + Cores + RAM in new lines
	os.system("sshpass -p 'redhat' ssh -o StrictHostKeyChecking=no -X root@"+str(i)+" \" ip a | grep global | grep -v virbr0 | awk '{print $2}' | cut -f1 -d'/' | grep -v : | grep -v 199.*| grep -v 200.* | cut -d ' ' -f6 ; nproc --all ; cat /proc/meminfo | grep MemFree | awk '{print $2}' | cut -d ' ' -f2- | grep -o [0-9]*\" >> /root/Desktop/Outputs/temp_cores_RAM.txt")


### Formatting the List as <IP> <Cores> <RAM> in one line per IP
os.system("paste - - - < /root/Desktop/Outputs/temp_cores_RAM.txt > /root/Desktop/Outputs/t_cores_RAM.txt ;rm -r /root/Desktop/Outputs/temp_cores_RAM.txt")

###Sorting the created List
os.system("sort -k2 -k3 -rn /root/Desktop/Outputs/t_cores_RAM.txt > /root/Desktop/Outputs/cores_RAM.txt ; rm -r /root/Desktop/Outputs/t_cores_RAM.txt") 

###Creating IP only list
os.system("cat /root/Desktop/Outputs/cores_RAM.txt | cut -f1 > /root/Desktop/Outputs/u_cores_RAM.txt")

###Separating JOB and Task Trackers
os.system("cat /root/Desktop/Outputs/u_cores_RAM.txt | head -n -1 > /root/Desktop/Outputs/tasktrackers.txt")
os.system("cat /root/Desktop/Outputs/u_cores_RAM.txt | tail -n -1 > /root/Desktop/Outputs/jobtracker.txt")


raw_input("Done.")

