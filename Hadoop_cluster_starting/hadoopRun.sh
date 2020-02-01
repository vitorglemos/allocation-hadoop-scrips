## Running this script on master node
start-dfs.sh
start-yarn.sh
hadoop-daemon.sh start datanode
hdfs dfsadmin -safemode leave

