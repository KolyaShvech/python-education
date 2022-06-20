from pyspark.sql import SparkSession
from pyspark import SparkConf
from pyspark.sql import functions as f
from pyspark.sql import types as t
from spark_train import best_films

spark = SparkSession.builder\
    .master("local")\
    .appName("Task")\
    .config(conf=SparkConf())\
    .getOrCreate()

#  create dataframe with names actors
path = "/home/nikolay/Projects/pyspark_learn/name.basic.tsv"
df_name = spark.read.csv(path, sep="\t", header=True)

#  create dataframe principal where all info about film, actors and other.
path_principals = "/home/nikolay/Projects/pyspark_learn/prinsipals.tsv"
df_principals = spark.read.csv(path_principals, sep="\t", header=True)

#  join dataframe best_films, this dataframe from last tasks, with principal dataframe.
complit = best_films.join(df_principals, on="tconst", how="left")

#  doing filter for stay only movie and votes for film more than 100000.
complit = complit.filter((f.col("titleType") == "movie") & (f.col("numVotes") > 100000))\
    .orderBy("averageRating", ascending=False)\
    .select("tconst", "nconst", "primaryTitle", "genres", "averageRating", "numVotes", "category")\

#  join complit dataframe with dataframe name.
best_actors = complit.join(df_name, on="nconst", how="left")

#  doing filter to keep the actors and actress, sorting by averageRating desc.
best_actors = best_actors.filter((f.col("category") == "actress") | (f.col("category") == "actor"))\
    .orderBy("averageRating", ascending=False)\
    .select("nconst", "tconst", "primaryTitle", "genres", "averageRating", "numVotes", "category", "primaryName")

#  making filter to leave films where averageRating more than 7
best_actors = best_actors.filter(f.col("averageRating") > 7).orderBy("averageRating", ascending=False)

#  grouping by actors and if count more than 1 sorting by count desc
best_actors.groupby("primaryName").count()\
    .filter(f.col("count") > 1)\
    .orderBy("count", ascending=False)\
    .select("primaryName")\
    .show()

best_actors.write.option("headers", True).csv("/home/nikolay/Projects/pyspark_learn/output_best_actors")
