import snowflake.connector
from dotenv import load_dotenv
import os

load_dotenv()

db_instance = snowflake.connector.connect(
    user = 'Stoyan0550',
    password =  os.getenv('SNOWFLAKE_PASSWORD'),
    account = 'FXYVGUR-XK87941',
    warehouse = 'COMPUTE_WH',
    database = 'amusement_park',
    schema = 'public'
)

query = db_instance.cursor()

def db_query(query_str, params=None):
    query.execute(query_str,params) if params else query.execute(query_str)
    return query.fetchall()

def db_insert(query_str):
    query.execute(query_str)
    db_instance.commit()

def db_get_highest_id(query_str):
    query.execute(query_str)
    return query.fetchall()
