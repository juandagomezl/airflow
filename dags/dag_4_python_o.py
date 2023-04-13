from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime


def print_data():
    print("hola")


with DAG(dag_id="Python_Operator",
         description="primer dag con python",
         schedule_interval="@once",
         start_date=datetime(2024, 4, 18)) as dag:

    t1 = PythonOperator(task_id="task_6",
                        python_callable=print_data)

    t1
