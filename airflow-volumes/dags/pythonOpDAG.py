from typing import Callable
import airflow
from airflow.operators.python import PythonOperator
from datetime import datetime

# !!!! Next step: define a get_age() function which will deliver an age and just use the task_instance variable in the greet function in order to print fn, ln and age


greet:Callable[[str, int],None] = lambda age, task_instance: print(f"Hello World ! My name is {task_instance.xcom_pull(task_ids='Get_name_task', key="first_name")} \
                                                                    {task_instance.xcom_pull(task_ids='Get_name_task', key="last_name")} and I am {age} year(s) old .") \
                                                                    if type(task_instance.xcom_pull(task_ids='Get_name_task', key="first_name"))==str and \
                                                                        type(task_instance.xcom_pull(task_ids='Get_name_task', key="last_name"))==str and \
                                                                            type(age)==int else None

def get_name(task_instance:airflow.models.taskinstance.TaskInstance) -> None: task_instance.xcom_push(key="first_name", value="Jerry"); \
                                                                                task_instance.xcom_push(key="last_name", value="Fridmann")
defaultArgs = {
    "owner": "MCA",
    "retries": 5
}

with airflow.DAG(
    dag_id="PythonOp_DAG",
    default_args=defaultArgs,
    description="The python operator DAG we created in 2026 !",
    start_date=datetime(2026, 1, 6),
    schedule="*/30 * * * *"
) as dag:
    task1 = PythonOperator(
        task_id = "first_PythonOp_task",
        python_callable = greet,
        op_kwargs={"age": 54}
    )

    task2 = PythonOperator(
        task_id = "Get_name_task",
        python_callable = get_name
    )

    task2 >> task1

    # task2 = PythonOperator(
    #     task_id = "second_bashOp_task",
    #     bash_command = "echo i am task 2 !"
    # )

    # task3 = PythonOperator(
    #     task_id = "third_bashOp_task",
    #     bash_command = "echo i am task 3 !"
    # )
    
    # task1 >> [task2, task3]