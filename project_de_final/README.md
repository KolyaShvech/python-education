# Final Project of Data Engineering

Create a data pipeline with Airflow and Spark jobs.

## In this project used some tools like with
#### 1. Docker-compose - build some containers 
![](scrins/ClipartKey_2268591.png)
#### 2. Airflow - create pipeline for DAGs
![](https://upload.wikimedia.org/wikipedia/commons/d/de/AirflowLogo.png)
#### 3. S3(Amazon) - keep some information about raw movies in storage
![](scrins/NicePng_amazon-arrow-png_1682898.png)
#### 4. PostgreSql - used for storing transform dataframe
![](scrins/NicePng_mysql-logo-transparent-png_2693721.png)
#### 5. Pyspark - used with framework to transform data
![](https://upload.wikimedia.org/wikipedia/commons/f/f3/Apache_Spark_logo.svg)
#### 6. Metabase - tool for intelligence business source, but SORRY I can't use this great service : (
![](scrins/metabase_logo_icon_168103.png)



*Starting project with building some containers in* `docker-compose.yml`

When `docker-compose.yml` ready and make `envirement (.env)`, starting file with command

```
sudo docker-compose up
```

##### First DAG save_movies_s3
take raw data about films 
![](scrins/first_dag_raw_movies.png)
##### Second DAG update_movies_daily
load movies which release in this day
![](scrins/second_dag_update_movies_daily.png)

##### Third DAG load_data_to_postgres
loading info about movies in postgres
![](scrins/third_dag_load_movies_to_postgres.png)
![](scrins/trird_dag_table.png)

##### Four DAG derive_imdb_data
joining imdb data with tmdb data
![](scrins/fourth_dag_derive_tmdb_imdb_datas.png)

#### Task with Metabase didn't, I managed to connect ; (
