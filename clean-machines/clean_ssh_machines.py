import os

machines = ["22","32","34","37","39"]; ## array with all machines on cluster

def machines_tmp_delete():
    for i in range(0,len(machines)):
        ssh = "ssh my_user_ssh@" + machines[i]; # your ssh user
        delete = " 'rm -r /tmp/* -f >/dev/null 2>&1'"; # temp files
        command = ssh + delete;
        out = os.system(command);
        print(" Machine uff" + machines[i] + " /tmp deleted ! Success !")
        
def machines_datanode_format():
    for i in range(0,len(machines)):
        ssh = "ssh my_user_ssh@" + machines[i];
        directory = r" 'cd /var/user'"; # your directory
        delete = " 'rm -r hdfs/'";
        make = " 'mkdir -p hdfs/datanode'"; # clean datanodes
        chmod = " 'chmod 775 hdfs/datanode'";
        os.system(ssh + directory);
        os.system(ssh + delete);
        os.system(ssh + make);
        os.system(ssh + chmod);
        print(" Machine uff" + machines[i] + " HDFS Datanode formated ! Success !")
      

machines_tmp_delete(); #this code clean /temp
machines_datanode_format(); #this code format datanode directory 
