from airflow import DAG
from datetime import datetime
from airflow.operators.python import PythonOperator
from airflow.providers.postgres.hooks.postgres import PostgresHook
from psycopg2.extensions import connection
import csv, logging, os


# 1/ Query data from postgres and retrieve them in a .txt file locally
# 2/ dump the file into minIO bucket

def postgres_to_s3() -> None:
    hook:PostgresHook = PostgresHook(postgres_conn_id="airflow_postgres")
    conn:connection = hook.get_conn()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM public.orders WHERE date <= '20220501'")
    with open("dags/get_orders.txt", "w") as text_file:
        logging.info(f"Abs path: {os.path.abspath("get_orders.txt")}")
        writer = csv.writer(text_file)
        writer.writerow([column[0] for column in cursor.description])
        writer.writerows(cursor)
    cursor.close()
    conn.close()
    logging.info(f"File 'get_orders.txt' successfully written !")




defaultArgs = {
    "owner": "MCA",
    "retries": 5
}

with DAG(
    dag_id="DAG_PostgresHooks",
    default_args=defaultArgs,
    description="Introduction to Airflow Hooks !",
    start_date=datetime(2026, 1, 12),
    schedule="@once",
    catchup=False
) as dag:
    task = PythonOperator(
        task_id="data_from_postgres_to_.txt_file",
        python_callable=postgres_to_s3
    )