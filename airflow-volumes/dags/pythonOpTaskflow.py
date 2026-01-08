from airflow.decorators import dag, task
from datetime import datetime

defaultArgs = {
    "owner": "MCA",
    "retries": 5
}

@dag(
    dag_id="PythonOp_DAG_Taskflow",
    default_args=defaultArgs,
    description="The python operator DAG we created with Taskflow !",
    start_date=datetime(2026, 1, 7),
    schedule="*/30 * * * *",
    catchup=False
)
def pythonOp_dag_taskflow():

    @task(multiple_outputs=True)
    def get_name() -> dict[str, str]: 
        return {"first_name": "Jerry", 
         "last_name":"Fridmann"}

    @task()
    def get_age() -> int:
        return 24


    @task()
    def greet(name:dict[str, str], age:int) -> None:
        print(f"Hello World ! My name is {name["first_name"]} {name["last_name"]} and I am {age} year(s) old .") if type(age)==int and type(name["first_name"])==str \
                and type(name["last_name"])==str else print("Incorrect variables type")
        
    name = get_name(); age = get_age()
    greet(name, age)
        

pythonOp_dag_taskflow()