import airflow
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator

dag = DAG(
    dag_id="example",
    start_date=airflow.utils.dates.days_ago(1),
    schedule_interval="* * * * *",
)

dummy_operator = DummyOperator(task_id="dummy_task", dag=dag)