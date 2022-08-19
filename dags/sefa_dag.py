"""This dag only runs some simple tasks to test Airflow's task execution."""
import datetime

from airflow.models.dag import DAG
from airflow.operators.python_operator import PythonOperator

import pandas as pd
import telethon

# create a function to get pandas version
def get_pandas_version():
    return pd.__version__


def get_telegram_version():
    return telethon.__version__


DAG_NAME = "sefa_dag"

# run telegram version check in a dag
with DAG(DAG_NAME, schedule_interval="*/30 * * * *") as dag:
    get_pandas_version_task = PythonOperator(
        task_id="get_pandas_version",
        python_callable=get_pandas_version,
        dag=dag,
        start_date=datetime.datetime(2022, 8, 20),
    )
    get_telegram_version_task = PythonOperator(
        task_id="get_telegram_version",
        python_callable=get_telegram_version,
        dag=dag,
        start_date=datetime.datetime(2022, 8, 20),
    )
get_pandas_version_task >> get_telegram_version_task
