from pyhive import hive
import pandas as pd

conn = hive.connect(
    host="spark-thrift-server-service",
    port=10001,
    username="hadoop",
    auth=None
    )
print(pd.read_sql(con=conn, sql="show databases"))
conn.close()
