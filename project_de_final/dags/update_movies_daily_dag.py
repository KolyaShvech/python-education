"""DAG for update movies"""
from datetime import timedelta
from os import environ

from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.utils.dates import datetime

from jobs.update_movies_daily_job import update_movies_daily


start_datetime = datetime(2021, 6, 21, 0, 0, 0, 0)

default_args = {
    "owner": "airflow",
    'max_active_runs': 1,
    "depends_on_past": False,
    'start_date': start_datetime,
    'retry_delay': timedelta(minutes=5)
}


with DAG("update_movies_s3_dag", default_args=default_args,
         schedule_interval="0 3 * * *", catchup=False) as dag:

    bucket_name = environ.get("MINIO_RAW_DATA_BUCKET_NAME")

    save_operator = PythonOperator(
        task_id='update_movies_daily',
        python_callable=update_movies_daily,
        provide_context=True
    )