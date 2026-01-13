from airflow import DAG
from datetime import datetime
from airflow.operators.python import PythonOperator
from airflow.providers.postgres.hooks.postgres import PostgresHook
from airflow.providers.amazon.aws.hooks.s3 import S3Hook
from psycopg2.extensions import connection
import csv, logging, os, tempfile


def postgres_to_s3(ds_nodash) -> None:
    # 1/ Query data from postgres and retrieve them in a .txt file locally
    pg_hook:PostgresHook = PostgresHook(postgres_conn_id="airflow_postgres")
    conn:connection = pg_hook.get_conn()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM public.orders WHERE date <'20220430' ORDER BY DATE ASC;")

    with tempfile.NamedTemporaryFile(mode='w', suffix=f"{ds_nodash}") as text_file:
    # with open(f"dags/get_orders_{ds_nodash}.txt", "w") as text_file:
        writer = csv.writer(text_file)
        writer.writerow([column[0] for column in cursor.description])
        writer.writerows(cursor)
        text_file.flush()
        cursor.close()
        conn.close()
        logging.info(f"File '{text_file.name}' successfully written !")

        # 2/ dump the file into minIO bucket
        s3_hook:S3Hook = S3Hook(aws_conn_id="airflow_minio")
        if s3_hook.check_for_bucket("airflow"):
            s3_hook.load_file(
                filename=text_file.name,
                key=f"s3-test/{ds_nodash}.txt",
                bucket_name="airflow",
                replace=True
            )
            logging.info(f"File '{text_file.name}' successfully uploaded to MinIO S3 bucket 'airflow' !")
        else:
            logging.error("The bucket 'airflow' does not exist in MinIO !")



defaultArgs = {
    "owner": "MCA",
    "retries": 5
}

with DAG(
    dag_id="DAG_PostgresHooks_v02",
    default_args=defaultArgs,
    description="Introduction to Airflow Hooks !",
    start_date=datetime(2022, 4, 30),
    schedule="@once",
    catchup=False
) as dag:
    task = PythonOperator(
        task_id="data_from_postgres_to_.txt_file",
        python_callable=postgres_to_s3
    )