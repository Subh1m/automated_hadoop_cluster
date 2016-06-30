# automated_hadoop_cluster

Contains Python scripts that automate the management of a cluster created using Apache Hadoop v1.

### Introduction
> *How to create and manage a cluster on Apache Hadoop in minutes with minimal user intervention?
Here's your answer!*

The executable scripts perform the following functions :

- Automatically scans all PC's connected to the Network using `nmap`
    - Separates these IP's that are capable of login via `ssh`

- Logs into each IP via `sshpass` and gathers hardware information such as **RAM** , **No. of CPU Cores**, **Free Disk Space**
    - Respective IPs are sorted based on obtained information. 

- User may choose to create cluster with above configurations, or choose to manually decide Name/Data Nodes and Job/Task Trackers

- Automatically installs **JDK** and **Hadoop version 1** on each PC one by one, if not present and configures them to be Name/Data Nodes or Job/Task Trackers

### Functions

1. Map/Refresh Network
2. View Network
3. Automatic Cluster
4. Custom Cluster
5. View Cluster Report
6. View Data on HDFS
7. Push File to HDFS
8. Open Web UI for HDFS
9. Open Web UI for MapReduce
10.Shut Down Cluster 

### Files

- `hadoop.py` is the main script containing the Menu's that calls the other files.
- `1_prepareIPs.py` ... `7_auto_off.py` contain code to run in each case. They create a resources directory called `Outputs` in the `pwd` containing all data files.
- `namenode.py` etc contain the templates of the entries to be made into the `hdfs-site.xml` / `core-site.xml` / `mapred-site.xml` in each individual PC of the cluster.

### Enhancements 

Further development will include :

- Option to create a Secondary Name Node
- Add Map Reduce programs and Run Jobs on files in HDFS
- Entering / Exiting the cluster from *Safe mode*
- Highly Available Name Node
