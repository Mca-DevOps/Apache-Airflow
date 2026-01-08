import airflow
from airflow.providers.common.sql.operators.sql import SQLExecuteQueryOperator
from datetime import datetime


defaultArgs = {
    "owner": "MCA",
    "retries": 5
}


with airflow.DAG(
    dag_id="PostgreSQL_Connection_DAG",
    default_args=defaultArgs,
    description="The PostgreSQL Connection DAG we created in 2026 !",
    start_date=datetime(2026, 1, 6),
    schedule="@once"
) as dag:
    create_pet_table = SQLExecuteQueryOperator(
        task_id="Create_pet_table",
        conn_id="airflow_postgres",
        sql="sql/create_pet_table.sql"
    )

    insert_data_into_pet_table = SQLExecuteQueryOperator(
        task_id="Insert_data_into_pet_table",
        conn_id="airflow_postgres",
        sql="sql/insert_into_pet_table.sql",
        params={"current_date": datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')}
    )

    fetch_data_from_pet_table = SQLExecuteQueryOperator(
        task_id="Fetch_data_from_pet_table",
        conn_id="airflow_postgres",
        sql="""SELECT * FROM pet;"""
    )

    delete_data_from_pet_table = SQLExecuteQueryOperator(
        task_id="Delete_data_from_pet_table",
        conn_id="airflow_postgres",
        sql="""DELETE FROM pet WHERE EXISTS (SELECT * FROM pet);"""
    )

    create_pet_table >> delete_data_from_pet_table >> insert_data_into_pet_table >> fetch_data_from_pet_table