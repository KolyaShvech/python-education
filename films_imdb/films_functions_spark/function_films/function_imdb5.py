from pyspark.sql import SparkSession
from pyspark import SparkConf
import pyspark.sql.types as t
import pyspark.sql.functions as f
from pyspark.sql.window import Window
from function_imdb4 import join_three_tables

spark = SparkSession.builder\
    .master("local")\
    .appName("Practise5")\
    .config(conf=SparkConf())\
    .getOrCreate()

path = "/basic.tsv"
df_spark = spark.read.csv(path, sep="\t", header=True)

ranking_path = "/ranking.tsv"
ranking_df = spark.read.csv(ranking_path, sep='\t', header=True)

path_principals = "/prinsipals.tsv"
principals_df = spark.read.csv(path_principals, sep="\t", header=True)

path = "/name.basic.tsv"
df_name = spark.read.csv(path, sep="\t", header=True)

#  use window function and partition by primaryName and orederby primeryName
window = Window.partitionBy("primaryName").orderBy("primaryTitle")

#  assign big_table func join_three_tables()
big_table = join_three_tables(df_spark, ranking_df, principals_df, on="tconst", how="left")


# create func which makes table best_director with films. Use needing filter and order by
def best_films_of_director():

    best_director = big_table.join(df_name, on="nconst", how="left")

    return best_director.filter(f.col("category") == "director")\
        .orderBy("primaryName", "averageRating", ascending=False)\
        .select("primaryName", "primaryTitle", "startYear", "averageRating", "numVotes")


#  func which getting dataframe with 5 best films of all directors
def get_best_films():

    best_5_films = best_films_of_director().withColumn("row_number", f.row_number().over(window))\
        .filter(f.col("row_number") < 6)\
        .orderBy("primaryName", "averageRating", "row_number", ascending=False)\
        .select("primaryName", "primaryTitle", "startYear", "averageRating", "numVotes")

    return best_5_films


#  create function write dataframe in csv file
def write_to_csv(df):
    return df.write.option("headers", True).csv("/home/nikolay/Projects/pyspark_learn/output_best_5_films_directors")


if __name__ == "__main__":
    get_best_films().show(truncate=False)
