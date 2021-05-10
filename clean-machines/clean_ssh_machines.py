import os

machine_names = ["m22","m32","m34","m37","m39"];

async def machine_delete_tmp(user: str):
    tmp_clean = "'rm -r /tmp/* -f >/dev/null 2>&1'"
    for m_name in machine_names:
        ssh_conn = f"ssh {user}@{m_name}"
        ssh_conn_clean = f"{ssh_conn} {tmp_clean}"
        os.system(ssh_conn_clean)
        
        print(f"Machine {m_name} cleaned!")
   
async def machine_delete_datanode(user: str):
    hadoop_directory = r" 'cd /var/user'"
    hadoop_hdfs = " 'rm -r hdfs/'"
    make_hdfs = " 'mkdir -p hdfs/datanode'"
    chmod_hdfs = " 'chmod 775 hdfs/datanode'"
    
    for m_name in machine_names:
        ssh_conn = f"ssh {user}@{m_name}"
        os.system(f"{ssh){hadoop_directory}")
        os.system(f"{ssh){hadoop_hdfs}")
        os.system(f"{ssh}{make_hdfs}")
        os.system(f"{ssh}{chmod_hdfs}")
                     
def run():
  await machine_delete_tmp(user="user")
  await machine_delete_datanode(user="user")
                  
      
