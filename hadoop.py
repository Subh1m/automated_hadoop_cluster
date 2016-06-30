#! /usr/bin/python2

import os
import commands


while True : 
	
	os.system("clear; tput setaf 4")
	print """ 

		***###      ---- MENU ----      ###***
		|					
		|
		|	Press :         
		|	1  -> Map/Refresh Network
		|	2  -> View Network
		|	3  -> Automatic Cluster
		|	4  -> Custom Cluster
		|	5  -> View Cluster Report
		|	6  -> View Data on HDFS
		|	7  -> Push File to HDFS
		|	8  -> Open Web UI for HDFS
		|	9  -> Open Web UI for MapReduce
		|	10 -> Shut Down Cluster 
		|	x  -> Exit Program
		|
		|
		***###      ______________      ###***

	"""

	ch = raw_input("Enter Choice : ")

	if ch == '1' :

		os.system("clear; python 1_prepareIPs.py ; python 2_cores_RAM.py; python 3_hdd.py")

	elif ch == '2' :
	
		os.system("clear")
		print("***** All Available IPs are : \n")
		h=open('/root/Desktop/Outputs/preparedIPs.txt','r')
		h.seek(0)
		for i in h.readlines():
			i.split()	
			print i

		print("***** NameNode IP is : \n")
		h=open('/root/Desktop/Outputs/namenode.txt','r')
		h.seek(0)
		for i in h.readlines():
			i.split()	
			print i

		print("***** All DataNode IPs are : \n")
		h=open('/root/Desktop/Outputs/datanodes.txt','r')
		h.seek(0)
		for i in h.readlines():
			i.split()	
			print i

		print("***** JobTracker IP is : \n")
		h=open('/root/Desktop/Outputs/jobtracker.txt','r')
		h.seek(0)
		for i in h.readlines():
			i.split()	
			print i

		print("***** All TaskTracker IPs are : \n")
		h=open('/root/Desktop/Outputs/tasktrackers.txt','r')
		h.seek(0)
		for i in h.readlines():
			i.split()	
			print i
		raw_input()

	elif ch == '3' :
	
		os.system("clear; python 4_auto_namejob.py ; python 5_auto_data.py; python 6_auto_task.py")

	elif ch == '4' :
		
		while True :

			os.system("clear")
			print """ 

		***###      ---- CUSTOM CLUSTER MENU ----      ###***
		|
		|	NOTE: 
		|	If you manually wish to edit the cluster 
		|	files, press any of the below, edit the 
		|	files, save changes and press 44 to Create 
		|	Cluster with the new settings.
		|
		|	Press :         
		|	11 -> Edit NameNode
		|	22 -> Edit DataNodes
		|	33 -> Edit JobTracker
		|	44 -> Edit TaskTrackers
		|	55 -> Create Cluster
		|	x -> Exit to Main Menu
		|
		|
		***###      	________________       		   ###***

		"""
			cch = raw_input("Enter Choice : ")
	
			if cch == '11' :
		
				os.system("gedit /root/Desktop/Outputs/namenode.txt")
	
			elif cch == '22' :

				os.system("gedit /root/Desktop/Outputs/datanodes.txt")
	
			elif cch == '33' :
		
				os.system("gedit /root/Desktop/Outputs/jobtracker.txt")
	
			elif cch == '44' :

				os.system("gedit /root/Desktop/Outputs/tasktrackers.txt")

			elif cch == '55' :

				os.system("clear; python 4_auto_namejob.py ; python 5_auto_data.py; python 6_auto_task.py")
	
			else :
				break
	elif ch == '5' :
	
		os.system("clear; hadoop dfsadmin -report")
		raw_input()	
	
	elif ch == '6' :
	
		os.system("clear; hadoop fs -ls /")
		raw_input()

	elif ch == '7' :
		
		loc = raw_input("\nEnter the location of the file : ")
		a=os.system("clear; hadoop fs -put "+str(loc)+" /")
		if a == 0 :
			print("***** File Successfully uploaded to HDFS")	

	elif ch == '8' :

		k = commands.getoutput("cat namenode.txt")	
		os.system("clear; firefox "+k+":50070")

	elif ch == '9' :
	
		k = commands.getoutput("cat jobtracker.txt")	
		os.system("clear; firefox "+k+":50030")	

	elif ch == '10' :
	
		os.system("clear; python 7_auto_off.py")
		
		
	else :
		exit()
