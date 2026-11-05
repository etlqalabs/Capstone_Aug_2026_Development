import  pandas as pd
from sqlalchemy import create_engine,text
import cx_Oracle
import logging
from common_utilities.utilities import read_from_file
from project_config.etlconfig import *

logging.basicConfig(
    filename='application_log/etlprocess.log',
    filemode='w',
    format='%(asctime)s-%(levelname)s-%(message)s',
    level=logging.INFO)
logger = logging.getLogger(__name__)



oracle_conn = create_engine(f"oracle+cx_oracle://{ORACLE_USER}:{ORACLE_PASSWORD}@{ORACLE_HOST}:{ORACLE_PORT}/{ORACLE_SERVICE}")

mysql_conn = create_engine(f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DATBASE}")

class DataLoading:
    def load_fact_sales_table(self):
        logger.info("Data loading in fact_sales tables has started... ")
        query = text("""insert into fact_sales(sales_id,product_id,store_id,quantity,total_sales,sale_date)
                        select sales_id,product_id,store_id,quantity,sales_amount,sale_date from sales_with_details""")
        with mysql_conn.connect() as conn:
            logger.info(query)
            conn.execute(query)
            conn.commit()
        logger.info("Data loading in fact_sales tables has completed... ")


    def load_fact_inventory_table(self):
        pass

    def load_monthly_sales_summary_table(self):
        pass

    def load_inventory_levl_by_stores_table(self):
        pass


if __name__ == "__main__":
    dl = DataLoading()
    dl.load_fact_sales_table()


