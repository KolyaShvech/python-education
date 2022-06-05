import pytest
from pyspark.sql import SparkSession, DataFrame
import films_imdb.films_functions_spark.function_films.function_imdb2


# Get one spark session for the whole test session
@pytest.fixture(scope="session")
def spark():
    return SparkSession.builder.getOrCreate()


def test_genres_best_films(spark_session):

    # Set up test column
    df_column = ["tconst", "titleType", "primaryTitle", "numVotes", "averageRating", "startYear", "genres"]
    # Set up test data
    df_data = [
        ["tt0000001", "short", "Carmencita", 1882, 5.7, 1894, "Documentary,Short"],
        ["tt0000009", "short", "Miss Jerry", 6803, 6.9, 1894, "Animation,Short"],
        ["tt4555426", "movie", "Darkest Hour", 196485, 7.4, 2017, "War"],
        ["tt0993840", "movie", "Army of the Dead", 167346, 5.7, 2021, "Horror"],
        ["tt3076658", "movie", "Creed", 267664, 7.6, 2015, "Sport"],
        ["tt0064116", "movie", "Once Upon a Time in the West", 323645, 8.5, 1968, "Western"],
        ["tt0099348", "movie", "Dances with Wolves", 260435, 8.0, 1990, "Western"]
    ]

    expected_column = ["tconst", "primaryTitle", "startYear", "genres", "averageRating", "numVotes"]

    expected_data = [
        ["tt0064116", "Once Upon a Time in the West", 1968, "Western", 8.5, 323645],
        ["tt0099348", "Dances with Wolves", 1990, "Western", 8.0, 260435],
        ["tt4555426", "Darkest Hour", 2017, "War", 7.4, 196485],
        ["tt3076658", "Creed", 2015, "Sport", 7.6, 267664],
        ["tt0993840", "Army of the Dead", 2021, "Horror", 5.7, 167346]
    ]

    df: DataFrame = spark_session.createDataFrame(df_data, df_column)

    expected_df: DataFrame = spark.createDataFrame(expected_data, expected_column)

    genres = films_imdb.films_functions_spark.function_films.function_imdb2.genres_best_films(df)

    rows = genres.collect()
    expected_rows = expected_df.collect()

    assert rows == expected_rows


def test_last_10_years(spark_session):

    # Set up test column
    df_column = ["tconst", "titleType", "primaryTitle", "numVotes", "averageRating", "startYear", "genres"]
    # Set up test data
    df_data = [
        ["tt0000001", "short", "Carmencita", 1882, 5.7, 1894, "Documentary,Short"],
        ["tt0000009", "short", "Miss Jerry", 6803, 6.9, 1894, "Animation,Short"],
        ["tt4555426", "movie", "Darkest Hour", 196485, 7.4, 2017, "War"],
        ["tt0993840", "movie", "Army of the Dead", 167346, 5.7, 2021, "Horror"],
        ["tt3076658", "movie", "Creed", 267664, 7.6, 2015, "Sport"],
        ["tt0064116", "movie", "Once Upon a Time in the West", 323645, 8.5, 1968, "Western"],
        ["tt0099348", "movie", "Dances with Wolves", 260435, 8.0, 1990, "Western"]
    ]

    expected_column = ["tconst", "primaryTitle", "startYear", "genres", "averageRating", "numVotes"]

    expected_data = [
        ["tt4555426", "movie", "Darkest Hour", 2017, 7.4, 196485, "War"],
        ["tt3076658", "movie", "Creed", 2015, 7.6, 267664, "Sport"],
        ["tt0993840", "movie", "Army of the Dead", 2021, 5.7, 167346, "Horror"]
    ]

    df: DataFrame = spark_session.createDataFrame(df_data, df_column)

    expected_df: DataFrame = spark.createDataFrame(expected_data, expected_column)

    last_10_years = films_imdb.films_functions_spark.function_films.function_imdb2.last_10_years(df)

    last_rows = last_10_years.collect()
    expected_rows = expected_df.collect()

    assert last_rows == expected_rows

def test_best_genres_1960(spark):

    # Set up test column
    df_column = ["tconst", "titleType", "primaryTitle", "numVotes", "averageRating", "startYear", "genres"]
    # Set up test data
    df_data = [
        ["tt0000001", "short", "Carmencita", 1882, 5.7, 1894, "Documentary,Short"],
        ["tt0000009", "short", "Miss Jerry", 6803, 6.9, 1894, "Animation,Short"],
        ["tt4555426", "movie", "Darkest Hour", 196485, 7.4, 2017, "War"],
        ["tt0993840", "movie", "Army of the Dead", 167346, 5.7, 2021, "Horror"],
        ["tt3076658", "movie", "Creed", 267664, 7.6, 2015, "Sport"],
        ["tt0064116", "movie", "Once Upon a Time in the West", 323645, 8.5, 1968, "Western"],
        ["tt0099348", "movie", "Dances with Wolves", 260435, 8.0, 1990, "Western"]
    ]

    expected_column = ["tconst", "primaryTitle", "startYear", "genres", "averageRating", "numVotes"]

    expected_data = [["tt0064116", "movie", "Once Upon a Time in the West", 323645, 8.5, 1968, "Western"]]

    df: DataFrame = spark.createDataFrame(df_data, df_column)
    expected_df: DataFrame = spark.createDataFrame(expected_data, expected_column)

    best_genres_1960 = films_imdb.films_functions_spark.function_films.function_imdb2.genres_best_films_in_1960th(df)

    rows_1960 = best_genres_1960.collect()
    expected_rows = expected_df.collect()

    assert rows_1960 == expected_rows


