from pyspark.sql import SparkSession
from pyspark import SparkConf
import pyspark.sql.types as t
import pyspark.sql.functions as f


spark = SparkSession.builder\
    .master("local")\
    .appName("Practise4")\
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


#  create function which joining three dataframe and use needing filters
def join_three_tables(df1, df2, df3, on=None, how=None):

    big_tables = df1.join(df2, on="tconst", how="left")\
        .join(df3, on="tconst", how="left")

    return big_tables.filter((f.col("titleType") == "movie") & (f.col("numVotes") > 10000))\
        .orderBy("averageRating", ascending=False)\
        .select("tconst", "nconst", "primaryTitle", "startYear", "genres", "averageRating", "numVotes", "category")


#  create function which join dataframe from "join_three_tables()" with dataframe df_name and use needing
#  filters with orederby
def make_tables_for_actors():
    best_actors = join_three_tables(df1=df_spark, df2=ranking_df, df3=principals_df).join(df_name, on="nconst", how="left")

    return best_actors.filter((f.col("category") == "actor") | (f.col("category") == "actress")
                              & (f.col("averageRating") > 7))\
        .orderBy("averageRating", ascending=False)\
        .select("nconst", "tconst", "primaryTitle", "genres", "averageRating", "numVotes", "category", "primaryName")


#  create func which show best actors
def get_top_actors():

    list_best_actors = make_tables_for_actors().groupby("primaryName").count()\
        .filter(f.col("count") > 1)\
        .orderBy("count", ascending=False)\
        .select("primaryName")

    return list_best_actors


#  create function write dataframe in csv file
def write_to_csv(df):
    return df.write.option("headers", True).csv("/home/nikolay/Projects/pyspark_learn/output_best_actors")


if __name__ == "__main__":
    get_top_actors().show(truncate=False)
