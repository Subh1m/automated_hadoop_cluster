#! /usr/bin/python2

import os
import sys
import commands

###Check if JDK and Hadoop are installed or not. If not, install them first.
a = os.system("rpm -q hadoop")
b = os.system("rpm -q jdk")
	
if a != 0 or b != 0:
	os.system("yum install hadoop* jdk* -y")


print ("*****  Configuring NameNode")
sys.stdout.flush()

	### Directory Input
print ("\n*****  Enter the Directory to give HDFS:")
sys.stdout.flush()
directory=raw_input()
	
os.system("mkdir /"+directory)

	### Name Node Template for HDFS File Creation	
datahdfs="""<?xml version="1.0"?>
	<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

	<!-- Put site-specific property overrides in this file. -->

	<configuration>
	 <property>
	 <name>dfs.name.dir</name>
	 <value>/"""+directory+"""</value>
	 </property>
	</configuration>
	"""

f = open("/etc/hadoop/hdfs-site.xml","w+")
f.write(datahdfs)
f.close()

	### Read NN IP :
k = commands.getoutput("cat /root/Desktop/namenode.txt")

	### Core File Creation

core="""<?xml version="1.0"?>
	<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

	<!-- Put site-specific property overrides in this file. -->

	<configuration>
	<property>
	<name>fs.default.name</name>
	<value>hdfs://"""+k+""":9001</value>
	</property>
	</configuration>
	"""

f = open("/etc/hadoop/core-site.xml","w+")
f.write(core)
f.close()	

	### Starting NN
os.system("hadoop namenode -format -force")	
os.system("hadoop-daemon.sh start namenode")

	### Showing status
print("\n*****  Status  ******")
sys.stdout.flush()
stat = os.system("/usr/java/jdk1.7.0_51/bin/jps")

