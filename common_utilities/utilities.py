import  pandas as pd
from sqlalchemy import create_engine
import cx_Oracle
from project_config.etlconfig import *

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

    df.to_sql("stag_product", mysql_conn, index=False)
