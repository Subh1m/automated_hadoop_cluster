#! /usr/bin/python2

import os 

print ("\nSorting based on Disk Space . . .\n")

f = open("/root/Desktop/Outputs/preparedIPs.txt","r");

for i in f.readlines():
	
	i=i.strip()

	print i

	###Creating file with IPs + Hard Disk Space in new lines
	os.system("sshpass -p 'redhat' ssh -o StrictHostKeyChecking=no -X root@"+str(i)+" \" ip a | grep global | grep -v virbr0 | awk '{print $2}' | cut -f1 -d'/' | grep -v : | grep -v 199.*| grep -v 200.* | cut -d ' ' -f6 ; df -k | grep -w / | tr -s ' ' | cut -d' ' -f4 \" >> /root/Desktop/Outputs/temp_hdd.txt")

### Formatting the List as <IP> <HDD> in one line per IP
os.system("paste - - < /root/Desktop/Outputs/temp_hdd.txt > /root/Desktop/Outputs/t_hdd.txt ; rm -r /root/Desktop/Outputs/temp_hdd.txt")

###Sorting the created List
os.system("sort -k2 -rn /root/Desktop/Outputs/t_hdd.txt > /root/Desktop/Outputs/hdd.txt ; rm -r /root/Desktop/Outputs/t_hdd.txt") 

###Creating IP only list
os.system("cat /root/Desktop/Outputs/hdd.txt | cut -f1 > /root/Desktop/Outputs/u_hdd.txt")

###Separating Name and Data Nodes
os.system("cat /root/Desktop/Outputs/u_hdd.txt | head -n -1 > /root/Desktop/Outputs/datanodes.txt")
os.system("cat /root/Desktop/Outputs/u_hdd.txt | tail -n -1 > /root/Desktop/Outputs/namenode.txt")

raw_input("Done.")
