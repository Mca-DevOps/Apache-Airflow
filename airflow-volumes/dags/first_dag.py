from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

defaultArgs = {
    "owner": "MCA",
    "retries": 5
}

with DAG(
    dag_id="FirstDAG",
    default_args=defaultArgs,
    description="The first DAG we created in 2026 !",
    start_date=datetime(2026, 1, 6),
    schedule="*/30 * * * *"
) as dag:
    task1 = BashOperator(
        task_id = "first_bashOp_task",
        bash_command = "echo i am task 1 !"
    )

    task2 = BashOperator(
        task_id = "second_bashOp_task",
        bash_command = "echo i am task 2 !"
    )

    task3 = BashOperator(
        task_id = "third_bashOp_task",
        bash_command = "echo i am task 3 !"
    )
    
    task1 >> [task2, task3]