from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG(
    dag_id="FirstDAG",
    description="The first DAG we created in 2026 !",
    start_date=datetime(2026, 1, 3),
    schedule="* * * * *"
) as dag:
    task1 = BashOperator(
        task_id = "first_bashOp_task",
        bash_command = "echo hello world !"
    )
    
    task1