from pyspark.sql import SparkSession
from pyspark import SparkConf
import pyspark.sql.functions as f
from pyspark.sql.window import Window
from function_imdb4 import join_three_tables, path_ranking, path_basic, path_principals, path_name_basic
from function_imdb1 import read_csv

spark = (SparkSession.builder
    .master("local")
    .appName("Practise1")
    .config(conf=SparkConf())
    .getOrCreate())


df_spark = read_csv(path_basic)

ranking_df = read_csv(path_ranking)

principals_df = read_csv(path_principals)

df_name = read_csv(path_name_basic)

#  use window function and partition by primaryName and orederby primeryName
window = Window.partitionBy("primaryName").orderBy("primaryTitle")

#  assign big_table func join_three_tables()
big_table = join_three_tables(df_spark, ranking_df, principals_df, on="tconst", how="left")


# create func which makes table best_director with films. Use needing filter and order by
def best_films_of_director():

    best_director = big_table.join(df_name, on="nconst", how="left")

    return (best_director.filter(f.col("category") == "director")
        .orderBy("primaryName", "averageRating", ascending=False)
        .select("primaryName", "primaryTitle", "startYear", "averageRating", "numVotes"))


#  func which getting dataframe with 5 best films of all directors
def get_best_films():

    best_5_films = (best_films_of_director().withColumn("row_number", f.row_number().over(window))
        .filter(f.col("row_number") < 6)
        .orderBy("primaryName", "averageRating", "row_number", ascending=False)
        .select("primaryName", "primaryTitle", "startYear", "averageRating", "numVotes"))

    return best_5_films


#  create function write dataframe in csv file
def write_to_csv(df):
    return df.write.option("headers", True).csv("./output_best_5_films_directors")


if __name__ == "__main__":
    get_best_films().show(truncate=False)
