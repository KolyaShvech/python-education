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

#  best films for all times
best_films.select("tconst", "primaryTitle", "numVotes", "averageRating", "startYear")\
                    .filter((f.col("titleType") == "movie") & (f.col("numVotes") > 100000))\
                    .orderBy("averageRating", ascending=False).limit(100).show()

#  best films of the last 10 years.
best_films.select("tconst", "primaryTitle", "numVotes", "averageRating", "startYear")\
                    .filter((f.col("titleType") == "movie") & (f.col("numVotes") > 100000)
                            & (f.col("startYear") > 2012))\
                    .orderBy("averageRating", ascending=False).limit(100).show()

#  best films for period from 1960 - 1969 years
best_films.select("tconst", "primaryTitle", "numVotes", "averageRating", "startYear")\
                    .filter((f.col("titleType") == "movie") & (f.col("numVotes") > 100000)
                            & ((f.col("startYear") > 1960) & (f.col("startYear") <= 1969)))\
                    .orderBy("averageRating", ascending=False).limit(100).show()

best_films.write.option("headers", True).csv("/home/nikolay/Projects/pyspark_learn/output_films")
