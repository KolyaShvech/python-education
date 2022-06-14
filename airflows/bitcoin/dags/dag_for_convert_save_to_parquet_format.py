
from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
from spark_jobs.action_with_bucket import create_bucket, clean_bucket

from spark_jobs.convert_and_save_to_parquet_format import transform_and_save_to_parquet


default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    'start_date': datetime(2022, 1, 1, 0, 0),
    'max_active_runs': 1,
    'retry_delay': timedelta(minutes=5),
    "is_paused_upon_creation": False
}

services = ['bitfinex', 'bitmex', 'poloniex']


with DAG("convert_and_save_to_parquet_format", schedule_interval="0 * * * *",
         default_args=default_args, catchup=False) as dag:
    parquet_operators = []
    bucket_create_operators = []
    bucket_clean_operators = []

    for exchange in services:
        operator = PythonOperator(
            task_id=f'create_{exchange}_parquet_bucket',
            python_callable=create_bucket,
            op_kwargs={'exchanger': exchange + "_parquet"}
        )
        bucket_create_operators.append(operator)

    for exchange in services:
        operator = PythonOperator(
            task_id=f'transform_and_save_{exchange}_to_parquet',
            python_callable=transform_and_save_to_parquet,
            op_kwargs={'exchanger': exchange}
        )
        parquet_operators.append(operator)

    for exchange in services:
        operator = PythonOperator(
            task_id=f'clean_{exchange}_bucket',
            python_callable=clean_bucket,
            op_kwargs={'bucket_name': exchange}
        )
        bucket_clean_operators.append(operator)

    for create, parquet, clean in zip(bucket_create_operators,
                                      parquet_operators,
                                      bucket_clean_operators):
        create >> parquet >> clean
