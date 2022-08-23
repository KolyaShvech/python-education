from pyspark.sql import SparkSession
from pyspark import SparkConf
import pyspark.sql.functions as f
from pyspark.sql.window import Window
from function_imdb1 import join_dataframe, read_csv, path_basic, path_ranking


spark = (SparkSession.builder
    .master("local")
    .appName("Practise1")
    .config(conf=SparkConf())
    .getOrCreate())


df_spark = read_csv(path_basic)

ranking_df = read_csv(path_ranking)

# join df_spark and ranking_df in one dataframe
complex_df = join_dataframe(df_spark, ranking_df)

#  divide column with genres into separate words
split_genre = f.explode(f.split(f.col("genres"), ","))

#  use window function and partition by genres
window = Window.partitionBy("genres").orderBy(f.col("averageRating"))


#  the best films sorted by genre and ranked by rating of all time
def genres_best_films(df):

    df = df.filter((f.col("titleType") == "movie") & (f.col("numVotes") > 100000))

    df = (df.withColumn("genres", split_genre)
        .withColumn("row_number", f.row_number().over(window))
        .filter((f.col("row_number") < 11)))

    return (df.orderBy("genres", "averageRating", "row_number", ascending=False)
        .select("tconst", "primaryTitle", "startYear", "genres", "averageRating", "numVotes"))


#  the best films divided by genre and ranked by rating of the last 10 years
def last_10_years(df):

    df = df.filter((f.col("titleType") == "movie") & (f.col("numVotes") > 100000)
                   & (f.col("startYear") >= 2012))

    df = (df.withColumn("genres", split_genre)
        .withColumn("row_number", f.row_number().over(window))
        .filter((f.col("row_number") < 11)))

    return (df.orderBy("genres", "averageRating", "row_number", ascending=False)
        .select("tconst", "primaryTitle", "startYear", "genres", "averageRating", "numVotes"))


#  best films sorted by genre and ranked by rating for the period from 1960 to 1969
def genres_best_films_in_1960th(df):

    df = df.filter((f.col("titleType") == "movie") & (f.col("numVotes") > 100000)
                   & (f.col("startYear") >= 1960) & (f.col("startYear") <= 1969))

    df = (df.withColumn("genres", split_genre)
        .withColumn("row_number", f.row_number().over(window))
        .filter((f.col("row_number") < 11)))

    return (df.orderBy("genres", "averageRating", "row_number", ascending=False)
        .select("tconst", "primaryTitle", "startYear", "genres", "averageRating", "numVotes"))


#  create function write dataframe in csv file
def write_to_csv(df):
    return df.write.option("headers", True).csv("/output_films_genres")


if __name__ == "__main__":
    genres_best_films_in_1960th(complex_df).show()
