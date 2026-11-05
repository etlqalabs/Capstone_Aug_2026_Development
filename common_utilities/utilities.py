import  pandas as pd
from sqlalchemy import create_engine
import cx_Oracle
import logging
from project_config.etlconfig import *
import paramiko

logging.basicConfig(
    filename='application_log/etlprocess.log',
    filemode='w',
    format='%(asctime)s-%(levelname)s-%(message)s',
    level=logging.INFO)
logger = logging.getLogger(__name__)


def read_from_file(file_path,file_type):
    if file_type == "csv":
        df = pd.read_csv(file_path)
    elif file_type == "json":
        df = pd.read_json(file_path)
    elif file_type == "xml":
        df = pd.read_xml(file_path,xpath=".//item")
    else:
        raise ValueError(f"insuppotted file Type passed {file_type}")
    return df

def download_file_from_linux_server():
    logger.info("File download from linux server has started....")
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy)
    ssh_client.connect(LINUX_HOSTNAME,username=LINUX_USERNAME,password=LINUX_PASSWORD)
    sftp = ssh_client.open_sftp()
    sftp.get(REMOTE_FILE_PATH,LOCAL_FILE_PATH)
    sftp.close()
    logger.info("File download from linux server has completed....")


