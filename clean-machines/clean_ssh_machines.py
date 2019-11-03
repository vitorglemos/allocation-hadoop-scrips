import os

machines = ["22","32","34","37","39"];

def machines_tmp_delete():
    for i in range(0,len(machines)):
        ssh = "ssh vlemos@" + machines[i];
        delete = " 'rm -r /tmp/* -f >/dev/null 2>&1'";
        command = ssh + delete;
        out = os.system(command);
        print(" Machine uff" + machines[i] + " /tmp deleted ! Success !")
        
def machines_datanode_format():
    for i in range(0,len(machines)):
        ssh = "ssh vlemos@uff" + machines[i];
        directory = r" 'cd /var/usuarios/vitor/hadop'";
        delete = " 'rm -r hdfs/'";
        make = " 'mkdir -p hdfs/datanode'";
        chmod = " 'chmod 775 hdfs/datanode'";
        os.system(ssh + directory);
        os.system(ssh + delete);
        os.system(ssh + make);
        os.system(ssh + chmod);
        print(" Machine uff" + machines[i] + " HDFS Datanode formated ! Success !")
      

machines_tmp_delete();
machines_datanode_format();
