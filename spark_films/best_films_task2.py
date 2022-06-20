from pyspark.sql import SparkSession
from pyspark import SparkConf
import pyspark.sql.types as t
import pyspark.sql.functions as f
from pyspark.sql.window import Window


spark = SparkSession.builder\
    .master("local")\
    .appName("Practise")\
    .config(conf=SparkConf())\
    .getOrCreate()


path = "/home/nikolay/Projects/pyspark_learn/basic.tsv"
df_spark = spark.read.csv(path, sep="\t", header=True)


codes_path = "/home/nikolay/Projects/pyspark_learn/ranking.tsv"
ranking_df = spark.read.csv(codes_path, sep='\t', header=True)

code_scheme = t.StructType([
    t.StructField("id", t.StringType(), True),
    t.StructField("ranking", t.DoubleType(), True),
    t.StructField("numVotes", t.IntegerType(), True)
])

best_films = df_spark.join(ranking_df, on="tconst", how="left")

#  divide column with genres into separate words
split_genre = f.explode(f.split(f.col("genres"), ","))
window = Window.partitionBy("genres").orderBy(f.col("averageRating"))

#  the best films sorted by genre and ranked by rating of all time
best_films = best_films.filter((f.col("titleType") == "movie") & (f.col("numVotes") > 100000))

best_films = best_films.withColumn("genres", split_genre) \
    .withColumn("row_number", f.row_number().over(window))\
    .filter((f.col("row_number") < 11))

best_films.orderBy("genres", "averageRating", "row_number", ascending=False)\
    .select("tconst", "primaryTitle", "startYear", "genres", "averageRating", "numVotes")\
    .show()

#  the best films divided by genre and ranked by rating of the last 10 years
best_films = best_films.filter((f.col("titleType") == "movie") & (f.col("numVotes") > 100000)
                               & (f.col("startYear") > 2012))

best_films = best_films.withColumn("genres", split_genre) \
    .withColumn("row_number", f.row_number().over(window))\
    .filter((f.col("row_number") < 11))

best_films.orderBy("genres", "averageRating", "row_number", ascending=False)\
    .select("tconst", "primaryTitle", "startYear", "genres", "averageRating", "numVotes")\
    .show()

#  best films sorted by genre and ranked by rating for the period from 1960 to 1969
best_films = best_films.filter((f.col("titleType") == "movie") & (f.col("numVotes") > 100000)
                               & ((f.col("startYear") > 1960) & (f.col("startYear") <= 1969)))

best_films = best_films.withColumn("genres", split_genre) \
    .withColumn("row_number", f.row_number().over(window))\
    .filter((f.col("row_number") < 11))

best_films.orderBy("genres", "averageRating", "row_number", ascending=False)\
    .select("tconst", "primaryTitle", "startYear", "genres", "averageRating", "numVotes")\
    .show()

best_films.write.option("headers", True).csv("/home/nikolay/Projects/pyspark_learn/output_films_genres")