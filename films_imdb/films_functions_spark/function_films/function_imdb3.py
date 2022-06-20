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
complex_df = join_dataframe(df1=df_spark, df2=ranking_df)

#  divide column with genres into separate words
split_genre = f.explode(f.split(f.col("genres"), ","))

#  use window function and partition by genres
window = Window.partitionBy("genres").orderBy(f.col("averageRating"))


#  best films sorted by genre and ranked by rating for the period from 2020 to today
def best_films_by_genres_2020th(df):

    df = (df.filter((f.col("titleType") == "movie") & (f.col("numVotes") > 100000) & (f.col("startYear") >= 2020))
        .withColumn("yearRange", f.lit("2020-today")))

    df = (df.withColumn("genres", split_genre)
        .withColumn("row_number", f.row_number().over(window))
        .filter((f.col("row_number") < 11)))

    return (df.orderBy("genres", "averageRating", "row_number", ascending=False)
        .select("tconst", "primaryTitle", "startYear", "genres", "averageRating", "numVotes", "yearRange"))


# best films sorted by genre and ranked by rating for the period from 2010 to 2020
def best_films_by_genres_2010th(df):

    df = (df.filter((f.col("titleType") == "movie") & (f.col("numVotes") > 100000)
                   & ((f.col("startYear") >= 2010) & (f.col("startYear") <= 2020)))
        .withColumn("yearRange", f.lit("2010-2020")))

    df = (df.withColumn("genres", split_genre)
        .withColumn("row_number", f.row_number().over(window))
        .filter((f.col("row_number") < 11)))

    return (df.orderBy("genres", "averageRating", "row_number", ascending=False)
        .select("tconst", "primaryTitle", "startYear", "genres", "averageRating", "numVotes", "yearRange"))


# best films sorted by genre and ranked by rating for the period from 2000 to 2010
def best_films_by_genres_2000th(df):

    df = (df.filter((f.col("titleType") == "movie") & (f.col("numVotes") > 100000)
                   & ((f.col("startYear") >= 2000) & (f.col("startYear") <= 2010)))
        .withColumn("yearRange", f.lit("2000-2010")))

    df = (df.withColumn("genres", split_genre)
        .withColumn("row_number", f.row_number().over(window))
        .filter((f.col("row_number") < 11)))

    return (df.orderBy("genres", "averageRating", "row_number", ascending=False)
        .select("tconst", "primaryTitle", "startYear", "genres", "averageRating", "numVotes", "yearRange"))


# best films sorted by genre and ranked by rating for the period from 1990 to 2000
def best_films_by_genres_1990th(df):

    df = (df.filter((f.col("titleType") == "movie") & (f.col("numVotes") > 100000)
                   & ((f.col("startYear") >= 1990) & (f.col("startYear") <= 1999)))
        .withColumn("yearRange", f.lit("1990-2000")))

    df = (df.withColumn("genres", split_genre)
        .withColumn("row_number", f.row_number().over(window))
        .filter((f.col("row_number") < 11)))

    return (df.orderBy("genres", "averageRating", "row_number", ascending=False)
        .select("tconst", "primaryTitle", "startYear", "genres", "averageRating", "numVotes", "yearRange"))


# best films sorted by genre and ranked by rating for the period from 1980 to 1990
def best_films_by_genres_1980th(df):

    df = (df.filter((f.col("titleType") == "movie") & (f.col("numVotes") > 100000)
                   & ((f.col("startYear") >= 1980) & (f.col("startYear") <= 1989)))
        .withColumn("yearRange", f.lit("1980-1990")))

    df = (df.withColumn("genres", split_genre)
        .withColumn("row_number", f.row_number().over(window))
        .filter((f.col("row_number") < 11)))

    return (df.orderBy("genres", "averageRating", "row_number", ascending=False)
        .select("tconst", "primaryTitle", "startYear", "genres", "averageRating", "numVotes", "yearRange"))


# best films sorted by genre and ranked by rating for the period from 1970 to 1980
def best_films_by_genres_1970th(df):

    df = (df.filter((f.col("titleType") == "movie") & (f.col("numVotes") > 100000)
                   & ((f.col("startYear") >= 1970) & (f.col("startYear") <= 1979)))
        .withColumn("yearRange", f.lit("1970-1980")))

    df = (df.withColumn("genres", split_genre)
        .withColumn("row_number", f.row_number().over(window))
        .filter((f.col("row_number") < 11)))

    return (df.orderBy("genres", "averageRating", "row_number", ascending=False)
        .select("tconst", "primaryTitle", "startYear", "genres", "averageRating", "numVotes", "yearRange"))


# best films sorted by genre and ranked by rating for the period from 1960 to 1970
def best_films_by_genres_1960th(df):

    df = (df.filter((f.col("titleType") == "movie") & (f.col("numVotes") > 100000)
                   & ((f.col("startYear") >= 1960) & (f.col("startYear") <= 1969)))
        .withColumn("yearRange", f.lit("1960-1970")))

    df = (df.withColumn("genres", split_genre)
        .withColumn("row_number", f.row_number().over(window))
        .filter((f.col("row_number") < 11)))

    return (df.orderBy("genres", "averageRating", "row_number", ascending=False)
        .select("tconst", "primaryTitle", "startYear", "genres", "averageRating", "numVotes", "yearRange"))


#  best films sorted by genre and ranked by rating for the period from 1950 to 1960
def best_films_by_genres_1950th(df):

    df = (df.filter((f.col("titleType") == "movie") & (f.col("numVotes") > 100000)
                   & ((f.col("startYear") >= 1950) & (f.col("startYear") <= 1959)))
        .withColumn("yearRange", f.lit("1950-1960")))

    df = (df.withColumn("genres", split_genre)
        .withColumn("row_number", f.row_number().over(window))
        .filter((f.col("row_number") < 11)))

    return (df.orderBy("genres", "averageRating", "row_number", ascending=False)
        .select("tconst", "primaryTitle", "startYear", "genres", "averageRating", "numVotes", "yearRange"))


#  create function write dataframe in csv file
def write_to_csv(df):
    return df.write.option("headers", True).csv("./output_films_genres_by_period")


if __name__ == "__main__":
    best_films_by_genres_2000th(complex_df).show(100, truncate=False)
