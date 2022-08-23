from pyspark.sql import SparkSession
from pyspark import SparkConf
import pyspark.sql.functions as f


spark = (SparkSession.builder
    .master("local")
    .appName("Practise1")
    .config(conf=SparkConf())
    .getOrCreate())


def read_csv(path):
    dataframe = spark.read.csv(path, sep="\t", header=True)
    return dataframe


path_basic = "./basic.tsv"
df_spark = read_csv(path_basic)

path_ranking = "./ranking.tsv"
ranking_df = read_csv(path_ranking)


# create function join two dataframe
def join_dataframe(df1, df2, on=None, how=None):
    return df1.join(df2, on="tconst", how="left")


#  best films for all times
def best_films_all_time(df):

    best_films_all_times = (df
                    .select("tconst", "primaryTitle", "numVotes", "averageRating", "startYear")
                    .filter((f.col("titleType") == "movie") & (f.col("numVotes") > 100000))
                    .orderBy("averageRating", ascending=False).limit(100))

    return best_films_all_times


#  best films of the last 10 years.
def best_films_for_last_10_years(df):

    best_10_years = best_films_all_time(df).filter(f.col("startYear") >= 2012)

    return best_10_years


#  best films for period from 1960 - 1969 years
def best_films_in_60h_years(df):

    best_films_60h_years = (best_films_all_time(df)
        .filter((f.col("startYear") >= 1960) & (f.col("startYear") <= 1969)))

    return best_films_60h_years


# create function write to csv file dataframe
def write_to_csv(df):
    return df.write.option("headers", True).csv("./output_films")


if __name__ == "__main__":
    join_dataframe(df_spark, ranking_df).show(100, truncate=False)
