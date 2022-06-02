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
best_films = best_films.withColumn("yearRange", f.lit("2020-today"))

#  best films sorted by genre and ranked by rating for the period from 2020 to today
# best_films = best_films.filter((f.col("titleType") == "movie") & (f.col("numVotes") > 100000)
#                                & ((f.col("startYear") >= 2020)))
#
# best_films = best_films.withColumn("genres", split_genre) \
#     .withColumn("row_number", f.row_number().over(window))\
#     .filter((f.col("row_number") < 11))
#
# best_films.orderBy("genres", "averageRating", "row_number", ascending=False)\
#     .select("tconst", "primaryTitle", "startYear", "genres", "averageRating", "yearRange")\
#     .show()

#  best films sorted by genre and ranked by rating for the period from 2010 to 2019
# best_films = best_films.withColumn("yearRange", f.lit("2010-2020"))
#
# best_films = best_films.filter((f.col("titleType") == "movie") & (f.col("numVotes") > 100000)
#                                & ((f.col("startYear") > 2010) & (f.col("startYear") <= 2019)))
#
# best_films = best_films.withColumn("genres", split_genre) \
#     .withColumn("row_number", f.row_number().over(window))\
#     .filter((f.col("row_number") < 11))
#
# best_films.orderBy("genres", "averageRating", "row_number", ascending=False)\
#     .select("tconst", "primaryTitle", "startYear", "genres", "averageRating", "numVotes", "yearRange")\
#     .show()

#  best films sorted by genre and ranked by rating for the period from 2000 to 2009
# best_films = best_films.withColumn("yearRange", f.lit("2000-2010"))
#
# best_films = best_films.filter((f.col("titleType") == "movie") & (f.col("numVotes") > 100000)
#                                & ((f.col("startYear") > 2000) & (f.col("startYear") <= 2009)))
#
# best_films = best_films.withColumn("genres", split_genre) \
#     .withColumn("row_number", f.row_number().over(window))\
#     .filter((f.col("row_number") < 11))
#
#
# best_films.orderBy("genres", "averageRating", "row_number", ascending=False)\
#     .select("tconst", "primaryTitle", "startYear", "genres", "averageRating", "numVotes", "yearRange")\
#     .show()

#  best films sorted by genre and ranked by rating for the period from 1990 to 1999
# best_films = best_films.withColumn("yearRange", f.lit("1990-2000"))
#
# best_films = best_films.filter((f.col("titleType") == "movie") & (f.col("numVotes") > 100000)
#                                & ((f.col("startYear") > 1990) & (f.col("startYear") <= 1999)))
#
# best_films = best_films.withColumn("genres", split_genre) \
#     .withColumn("row_number", f.row_number().over(window))\
#     .filter((f.col("row_number") < 11))
#
# best_films.orderBy("genres", "averageRating", "row_number", ascending=False)\
#     .select("tconst", "primaryTitle", "startYear", "genres", "averageRating", "numVotes", "yearRange")\
#     .show()

#  best films sorted by genre and ranked by rating for the period from 1980 to 1989
# best_films = best_films.withColumn("yearRange", f.lit("1980-1990"))
#
# best_films = best_films.filter((f.col("titleType") == "movie") & (f.col("numVotes") > 100000)
#                                & ((f.col("startYear") > 1980) & (f.col("startYear") <= 1989)))
#
# best_films = best_films.withColumn("genres", split_genre) \
#     .withColumn("row_number", f.row_number().over(window))\
#     .filter((f.col("row_number") < 11))
#
# best_films.orderBy("genres", "averageRating", "row_number", ascending=False)\
#     .select("tconst", "primaryTitle", "startYear", "genres", "averageRating", "numVotes", "yearRange")\
#     .show()

#  best films sorted by genre and ranked by rating for the period from 1970 to 1979
# best_films = best_films.withColumn("yearRange", f.lit("1970-1980"))
#
# best_films = best_films.filter((f.col("titleType") == "movie") & (f.col("numVotes") > 100000)
#                                & ((f.col("startYear") > 1970) & (f.col("startYear") <= 1979)))
#
# best_films = best_films.withColumn("genres", split_genre) \
#     .withColumn("row_number", f.row_number().over(window))\
#     .filter((f.col("row_number") < 11))
#
# best_films.orderBy("genres", "averageRating", "row_number", ascending=False)\
#     .select("tconst", "primaryTitle", "startYear", "genres", "averageRating", "numVotes", "yearRange")\
#     .show()

# best films sorted by genre and ranked by rating for the period from 1960 to 1969
# best_films = best_films.withColumn("yearRange", f.lit("1960-1970"))
#
# best_films = best_films.filter((f.col("titleType") == "movie") & (f.col("numVotes") > 100000)
#                                & ((f.col("startYear") > 1960) & (f.col("startYear") <= 1969)))
#
# best_films = best_films.withColumn("genres", split_genre) \
#     .withColumn("row_number", f.row_number().over(window))\
#     .filter((f.col("row_number") < 11))
#
# best_films.orderBy("genres", "averageRating", "row_number", ascending=False)\
#     .select("tconst", "primaryTitle", "startYear", "genres", "averageRating", "numVotes", "yearRange")\
#     .show()

#  best films sorted by genre and ranked by rating for the period from 1950 to 1959
best_films = best_films.withColumn("yearRange", f.lit("1950-1960"))

best_films = best_films.filter((f.col("titleType") == "movie") & (f.col("numVotes") > 100000)
                               & ((f.col("startYear") > 1950) & (f.col("startYear") <= 1959)))

best_films = best_films.withColumn("genres", split_genre) \
    .withColumn("row_number", f.row_number().over(window))\
    .filter((f.col("row_number") < 11))

best_films.orderBy("genres", "averageRating", "row_number", ascending=False)\
    .select("tconst", "primaryTitle", "startYear", "genres", "averageRating", "numVotes", "yearRange")\
    .show()


best_films.write.option("headers", True).csv("/home/nikolay/Projects/pyspark_learn/output_genres_decades")
