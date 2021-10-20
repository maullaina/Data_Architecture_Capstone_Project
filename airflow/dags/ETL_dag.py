from datetime import datetime, timedelta
import os
from airflow import DAG
from airflow.operators.postgres_operator import PostgresOperator
from airflow.operators.dummy_operator import DummyOperator
from airflow.contrib.hooks.aws_hook import AwsHook
from airflow.operators import (StageToRedshiftOperator, HasRowsOperator, LoadDimensionOperator, LoadFactOperator, DataQualityOperator)
from helpers import SqlQueries

default_args = {
    'owner': 'udacity',
    'depends_on_past': False,
    'start_date': datetime(2019, 1, 12),
    'email': ['maullaina@gmail.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 3, 
    'retry_delay': timedelta(minutes=5)
}

dag = DAG('udac_example_dag',
          default_args=default_args,
          description='Load and transform data in Redshift with Airflow',
          schedule_interval='@yearly'
        )

start_operator = DummyOperator(task_id='Begin_execution',  dag=dag)

stage_immigration_to_redshift = StageToRedshiftOperator(
    task_id='Stage_immigration',
    dag=dag,
    table="staging_immigration",
    redshift_conn_id="redshift",
    aws_credentials_id="aws_credentials",
    s3_bucket="s3capstone",
    s3_key="immigration_prova.csv" #"immigration_data_sample.csv"
)

stage_demographics_to_redshift = StageToRedshiftOperator(
    task_id='Stage_demographics',
    dag=dag,
    table="staging_demographics",
    redshift_conn_id="redshift",
    aws_credentials_id="aws_credentials",
    s3_bucket="s3capstone",
    s3_key= "demographics_prova.csv" #"NEWus-cities-demographics.csv"
)

stage_airports_to_redshift = StageToRedshiftOperator(
    task_id='Stage_airports',
    dag=dag,
    table="staging_airports",
    redshift_conn_id="redshift",
    aws_credentials_id="aws_credentials",
    s3_bucket="s3capstone",
    s3_key= "airport-codes_csv.csv"
)

check_immigration = HasRowsOperator(
    task_id='check_immigration_data',
    dag=dag,
    redshift_conn_id="redshift",
    table="staging_immigration"
)

check_demographics = HasRowsOperator(
    task_id='check_demographics_data',
    dag=dag,
    redshift_conn_id="redshift",
    table="staging_demographics"
)

check_airports = HasRowsOperator(
    task_id='check_airports_data',
    dag=dag,
    redshift_conn_id="redshift",
    table="staging_airports"
)

load_entries_table = LoadFactOperator(
    task_id='Load_entries_fact_table',
    dag=dag,
    table = 'entries',
    redshift_conn_id = "redshift",
    load_sql_stmt = SqlQueries.entries_table_insert
    
)

load_newcomers_dimension_table = LoadDimensionOperator(
    task_id='Load_newcomers_dim_table',
    dag=dag,
    table = 'newcomers',
    redshift_conn_id = "redshift",
    append_data = True,
    load_sql_stmt = SqlQueries.newcomers_table_insert
)

load_visa_dimension_table = LoadDimensionOperator(
    task_id='Load_visa_dim_table',
    dag=dag,
    table = 'visa',
    redshift_conn_id = "redshift",
    append_data = True,
    load_sql_stmt = SqlQueries.visa_table_insert
)

load_flights_dimension_table = LoadDimensionOperator(
    task_id='Load_flights_dim_table',
    dag=dag,
    table = 'flights',
    redshift_conn_id = "redshift",
    append_data = True,
    load_sql_stmt = SqlQueries.flights_table_insert
)

load_cities_dimension_table = LoadDimensionOperator(
    task_id='Load_cities_dim_table',
    dag=dag,
    table = 'cities',
    redshift_conn_id = "redshift",
    append_data = True,
    load_sql_stmt = SqlQueries.cities_table_insert 
)

load_airports_dimension_table = LoadDimensionOperator(
    task_id='Load_airports_dim_table',
    dag=dag,
    table = 'airports',
    redshift_conn_id = "redshift",
    append_data = True,
    load_sql_stmt = SqlQueries.airports_table_insert
)

run_quality_checks = DataQualityOperator(
    task_id='Run_data_quality_checks',
    dag=dag,
    dq_checks_null=[
        { 'check_sql': 'SELECT COUNT(*) FROM visa WHERE admnum IS NULL', 'expected_result': 0 },
        { 'check_sql': 'SELECT COUNT(*) FROM flights WHERE fltno IS NULL', 'expected_result': 0 },
        { 'check_sql': 'SELECT COUNT(*) FROM newcomers WHERE cicid IS NULL', 'expected_result': 0 },
        { 'check_sql': 'SELECT COUNT(*) FROM cities WHERE city IS NULL', 'expected_result': 0 },
        { 'check_sql': 'SELECT COUNT(*) FROM airports WHERE ident IS NULL', 'expected_result': 0 }
    ],
    redshift_conn_id ="redshift"
)

end_operator = DummyOperator(task_id='Stop_execution',  dag=dag)


start_operator >> stage_immigration_to_redshift
start_operator >> stage_demographics_to_redshift
start_operator >> stage_airports_to_redshift

stage_immigration_to_redshift >> check_immigration
stage_demographics_to_redshift >> check_demographics
stage_airports_to_redshift >> check_airports

check_immigration >> load_entries_table
check_demographics >> load_entries_table
check_airports >> load_entries_table

load_entries_table >> load_newcomers_dimension_table
load_entries_table >> load_visa_dimension_table
load_entries_table >> load_flights_dimension_table
load_entries_table >> load_cities_dimension_table
load_entries_table >> load_airports_dimension_table

load_newcomers_dimension_table >> run_quality_checks
load_visa_dimension_table >> run_quality_checks
load_flights_dimension_table >> run_quality_checks
load_cities_dimension_table >> run_quality_checks
load_airports_dimension_table >> run_quality_checks

run_quality_checks >> end_operator
