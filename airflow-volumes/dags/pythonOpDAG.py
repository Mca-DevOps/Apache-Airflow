from typing import Callable
import airflow
from airflow.operators.python import PythonOperator
from datetime import datetime

# !!!! Next step: define a get_age() function which will deliver an age and just use the task_instance variable in the greet function in order to print fn, ln and age

# greet which pull informations from get_age and get_name functions to greet the user
greet:Callable[[airflow.models.taskinstance.TaskInstance],None] = lambda task_instance: print(f"Hello World ! My name is {task_instance.xcom_pull(task_ids='Get_name_task', key="first_name")} \
                                                                    {task_instance.xcom_pull(task_ids='Get_name_task', key="last_name")} and I am {task_instance.xcom_pull(task_ids='Get_age_task', key="age")} year(s) old .") \
                                                                    if type(task_instance.xcom_pull(task_ids='Get_name_task', key="first_name"))==str and \
                                                                        type(task_instance.xcom_pull(task_ids='Get_name_task', key="last_name"))==str and \
                                                                            type(task_instance.xcom_pull(task_ids='Get_age_task', key="age"))==int else print("Incorrect variables type")


# get_name function which push a first_name and a last_name in its XCom
def get_name(task_instance:airflow.models.taskinstance.TaskInstance) -> None: task_instance.xcom_push(key="first_name", value="Jerry"); \
                                                                                task_instance.xcom_push(key="last_name", value="Fridmann")


# get_age function which push an age in its XCom
get_age:Callable[[airflow.models.taskinstance.TaskInstance], None] = lambda task_instance: task_instance.xcom_push(key="age", value=24)


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
        task_id = "Get_age_task",
        python_callable = get_age
    )

    task2 = PythonOperator(
        task_id = "Get_name_task",
        python_callable = get_name
    )

    task3 = PythonOperator(
        task_id = "first_PythonOp_task",
        python_callable = greet
    )

    [task1, task2] >> task3