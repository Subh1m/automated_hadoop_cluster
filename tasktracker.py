#! /usr/bin/python2

import os
import sys
import commands

###Check if JDK and Hadoop are installed or not. If not, install them first.
a = os.system("rpm -q hadoop")
b = os.system("rpm -q jdk")
	
if a != 0 or b != 0:
	os.system("yum install hadoop* jdk* -y")


print ("*****  Configuring TaskTracker")
sys.stdout.flush()

	### Read JT IP :

k = commands.getoutput("cat /root/Desktop/jobtracker.txt")

	### Mapred File Creation

core="""<?xml version="1.0"?>
	<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

	<!-- Put site-specific property overrides in this file. -->

	<configuration>
	<property>
	<name>mapred.job.tracker</name>
	<value>hdfs://"""+k+""":9002</value>
	</property>
	</configuration>
	"""

f = open("/etc/hadoop/mapred-site.xml","w+")
f.write(core)
f.close()	

	### Starting TT
os.system("hadoop-daemon.sh start tasktracker")

	### Showing status
print("\n*****  Status  ******")
sys.stdout.flush()
stat = os.system("/usr/java/jdk1.7.0_51/bin/jps")
