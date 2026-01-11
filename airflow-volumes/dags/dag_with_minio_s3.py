from airflow import DAG
from airflow.providers.amazon.aws.sensors.s3 import S3KeySensor
from datetime import datetime

defaultArgs = {
    "owner": "MCA",
    "retries": 5
}

with DAG(
    dag_id="S3_sensor_dagV1",
    default_args=defaultArgs,
    description="The first DAG we created in 2026 !",
    start_date=datetime(2026, 1, 6),
    schedule="*/30 * * * *",
    catchup=False
) as dag:
    task1 = S3KeySensor(
        task_id = "first_s3_key_sensor_task",
        bucket_name = "airflow",
        bucket_key = "s3-test/file-Entreprises-Auto-ecoles-Togo.csv",
        aws_conn_id = "airflow_minio"
    )