from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.models import Variable
from datetime import datetime


var_ = Variable.get("data")
# foo_json = Variable.get("foo_baz",
#                         deserialize_json=True)


def print_data():
    print("hola")


def print_var():
    print(var_)


with DAG(dag_id="Python_Operator",
         description="primer dag con python",
         schedule_interval="@once",
         start_date=datetime(2024, 4, 18)) as dag:

    t1 = PythonOperator(task_id="task_6",
                        python_callable=print_data)

    t2 = PythonOperator(task_id="task_7",
                        python_callable=print_var)

    t1 >> t2
