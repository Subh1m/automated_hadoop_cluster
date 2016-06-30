import os


###Shutting Down DataNodes

print("***** Shutting Down DataNodes")
f = open("/root/Desktop/Outputs/datanodes.txt","r");

for i in f.readlines():
	
	i=i.strip()
		
	os.system("sshpass -p 'redhat' ssh -o StrictHostKeyChecking=no -X root@"+str(i)+" \"hadoop-daemon.sh stop datanode ; rm -rf /root/Desktop/namenode.txt\"")

###Shutting Down TaskTrackers
print("***** Shutting Down TaskTrackers")
f = open("/root/Desktop/Outputs/tasktrackers.txt","r");

for i in f.readlines():
	
	i=i.strip()
		
	os.system("sshpass -p 'redhat' ssh -o StrictHostKeyChecking=no -X root@"+str(i)+" \"hadoop-daemon.sh stop tasktracker ; rm -rf /root/Desktop/jobtracker.txt\"")

###Shutting Down NameNodes
print("***** Shutting Down NameNodes")
f = open("/root/Desktop/Outputs/namenode.txt","r");

for i in f.readlines():
	
	i=i.strip()
		
	os.system("sshpass -p 'redhat' ssh -o StrictHostKeyChecking=no -X root@"+str(i)+" \"hadoop-daemon.sh stop namenode ; rm -rf /root/Desktop/jobtracker.txt\"")

###Shutting Down JobTracker
print("***** Shutting Down JobTracker")
f = open("/root/Desktop/Outputs/jobtracker.txt","r");

for i in f.readlines():
	
	i=i.strip()
		
	os.system("sshpass -p 'redhat' ssh -o StrictHostKeyChecking=no -X root@"+str(i)+" \"hadoop-daemon.sh stop jobtracker ; rm -rf /root/Desktop/jobtracker.txt ; rm -rf /root/Desktop/namenode.txt\"")
	

raw_input("\n***** CLUSTER SHUT DOWN SUCCESSFULLY")
