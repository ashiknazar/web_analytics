from airflow import DAG
from airflow.providers.apache.hive.operators.hive import HiveOperator
from datetime import datetime

with DAG(
    dag_id="daily_hive_analytics",
    start_date=datetime(2026, 1, 1),
    schedule_interval="@daily",
    catchup=False
) as dag:

    run_hive = HiveOperator(
        task_id="compute_page_visits",
        hql="hive/analytics.hql"
    )
