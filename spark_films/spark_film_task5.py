from pyspark.sql import SparkSession
from pyspark import SparkConf
from pyspark.sql import functions as f
from pyspark.sql import types as t
from pyspark.sql.window import Window

spark = SparkSession.builder\
    .master("local")\
    .appName("Task")\
    .config(conf=SparkConf())\
    .getOrCreate()

path_name = "/home/nikolay/Projects/pyspark_learn/name.basic.tsv"
df_name = spark.read.csv(path_name, sep="\t", header=True)

path_principals = "/home/nikolay/Projects/pyspark_learn/prinsipals.tsv"
df_principals = spark.read.csv(path_principals, sep="\t", header=True)

path = "/home/nikolay/Projects/pyspark_learn/basic.tsv"
df_basic = spark.read.csv(path, sep="\t", header=True)

path_ranking = "/home/nikolay/Projects/pyspark_learn/ranking.tsv"
ranking_df = spark.read.csv(path_ranking, sep='\t', header=True)

popular_films = df_basic.join(ranking_df, on="tconst", how="left")

popular_films.select("tconst", "primaryTitle", "numVotes", "averageRating", "startYear")\
                    .filter(f.col("titleType") == "movie")\
                    .orderBy("averageRating", ascending=False)

complex_films = popular_films.join(df_principals, on="tconst", how="left")
complex_films = complex_films.filter(f.col("titleType") == "movie")\
    .orderBy("averageRating", ascending=False)\
    .select("nconst", "tconst", "primaryTitle", "startYear", "averageRating", "numVotes", "category")

best_director = complex_films.join(df_name, on="nconst", how="left")

window = Window.partitionBy("primaryName").orderBy("primaryTitle")

best_director = best_director.filter((f.col("category") == "director") & (f.col("numVotes") > 10))\
    .orderBy("primaryName", "averageRating", ascending=False)\
    .select("primaryName", "primaryTitle", "startYear", "averageRating", "numVotes")

best_director.withColumn("row_number", f.row_number().over(window))\
    .filter(f.col("row_number") < 6)\
    .orderBy("primaryName", "averageRating", "row_number", ascending=False)\
    .select("primaryName", "primaryTitle", "startYear", "averageRating", "numVotes")\
    .show()

best_director.write.option("headers", True).csv("/home/nikolay/Projects/pyspark_learn/output_best_director")
