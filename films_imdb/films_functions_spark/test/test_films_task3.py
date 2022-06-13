import pytest
from pyspark.sql import SparkSession, DataFrame
import films_imdb.films_functions_spark.function_films.function_imdb3


def test_best_films_by_genres_2020th(spark_session):

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
        ["tt0099348", "movie", "Dances with Wolves", 260435, 8.0, 1990, "Western"],
        ["tt0089927", "movie", "Rocky IV", 201574, 6.8, 1985, "Sport"],
        ["tt0077651", "movie", "Halloween", 266227, 7.7, 1978, "Thriller"],
        ["tt0053291", "movie", "Some Like It Hot", 262481, 8.2, 1959, "Music"]]

    expected_column = ["tconst", "primaryTitle", "startYear", "genres", "averageRating", "numVotes", "yearRange"]
    expected_data = ["tt0993840", "movie", "Army of the Dead", 167346, 5.7, 2021, "Horror", "2020-today"]

    df: DataFrame = spark_session.createDataFrame(df_data, df_column)
    expected_df: DataFrame = spark_session.createDataFrame(expected_data, expected_column)

    films = films_imdb.films_functions_spark.function_films.function_imdb3.best_films_by_genres_2020th(df)

    rows = films.collect()
    expected_rows = expected_df.collect()

    assert rows == expected_rows


def test_best_films_by_genres_2010th(spark_session):

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
        ["tt0099348", "movie", "Dances with Wolves", 260435, 8.0, 1990, "Western"],
        ["tt0089927", "movie", "Rocky IV", 201574, 6.8, 1985, "Sport"],
        ["tt0077651", "movie", "Halloween", 266227, 7.7, 1978, "Thriller"],
        ["tt0053291", "movie", "Some Like It Hot", 262481, 8.2, 1959, "Music"]]

    expected_column = ["tconst", "primaryTitle", "startYear", "genres", "averageRating", "numVotes", "yearRange"]
    expected_data = [["tt4555426", "movie", "Darkest Hour", 196485, 7.4, 2017, "War", "2010-2020"],
                      ["tt3076658", "movie", "Creed", 267664, 7.6, 2015, "Sport", "2010-2020"]]

    df: DataFrame = spark_session.createDataFrame(df_data, df_column)
    expected_df: DataFrame = spark_session.createDataFrame(expected_data, expected_column)

    best_2010_films = films_imdb.films_functions_spark.function_films.function_imdb3.best_films_by_genres_2010th(df)

    best_rows = best_2010_films.collect()
    expected_rows = expected_df.collect()

    assert best_rows == expected_rows


def test_best_films_by_genres_2000th(spark_session):
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
        ["tt0099348", "movie", "Dances with Wolves", 260435, 8.0, 1990, "Western"],
        ["tt0089927", "movie", "Rocky IV", 201574, 6.8, 1985, "Sport"],
        ["tt0077651", "movie", "Halloween", 266227, 7.7, 1978, "Thriller"],
        ["tt0053291", "movie", "Some Like It Hot", 262481, 8.2, 1959, "Music"],
        ["tt1046173", "movie", "G.I. Joe: The Rise of Cobra", 207690, 5.7, 2009, "Sci-Fi"]]

    expected_column = ["tconst", "primaryTitle", "startYear", "genres", "averageRating", "numVotes", "yearRange"]
    expected_data = ["tt1046173", "movie", "G.I. Joe: The Rise of Cobra", 207690, 5.7, 2009, "Sci-Fi", "2000-2010"]

    df: DataFrame = spark_session.createDataFrame(df_data, df_column)
    expected_df: DataFrame = spark_session.createDataFrame(expected_data, expected_column)

    best_2000_films = films_imdb.films_functions_spark.function_films.function_imdb3.best_films_by_genres_2000th(df)

    best_rows = best_2000_films.collect()
    expected_rows = expected_df.collect()

    assert best_rows == expected_rows


def test_best_films_by_genres_1990th(spark_session):

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
        ["tt0099348", "movie", "Dances with Wolves", 260435, 8.0, 1990, "Western"],
        ["tt0089927", "movie", "Rocky IV", 201574, 6.8, 1985, "Sport"],
        ["tt0077651", "movie", "Halloween", 266227, 7.7, 1978, "Thriller"],
        ["tt0053291", "movie", "Some Like It Hot", 262481, 8.2, 1959, "Music"],
        ["tt1046173", "movie", "G.I. Joe: The Rise of Cobra", 207690, 5.7, 2009, "Sci-Fi"]]

    expected_column = ["tconst", "primaryTitle", "startYear", "genres", "averageRating", "numVotes", "yearRange"]
    expected_data = ["tt0099348", "movie", "Dances with Wolves", 260435, 8.0, 1990, "Western", "1990-2000"]

    df: DataFrame = spark_session.createDataFrame(df_data, df_column)
    expected_df: DataFrame = spark_session.createDataFrame(expected_data, expected_column)

    best_1990_films = films_imdb.films_functions_spark.function_films.function_imdb3.best_films_by_genres_1990th(df)

    best_rows = best_1990_films.collect()
    expected_rows = expected_df.collect()

    assert best_rows == expected_rows


def test_best_films_by_genres_1980th(spark_session):
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
        ["tt0099348", "movie", "Dances with Wolves", 260435, 8.0, 1990, "Western"],
        ["tt0089927", "movie", "Rocky IV", 201574, 6.8, 1985, "Sport"],
        ["tt0077651", "movie", "Halloween", 266227, 7.7, 1978, "Thriller"],
        ["tt0053291", "movie", "Some Like It Hot", 262481, 8.2, 1959, "Music"],
        ["tt1046173", "movie", "G.I. Joe: The Rise of Cobra", 207690, 5.7, 2009, "Sci-Fi"]]

    expected_column = ["tconst", "primaryTitle", "startYear", "genres", "averageRating", "numVotes", "yearRange"]
    expected_data = ["tt0089927", "movie", "Rocky IV", 201574, 6.8, 1985, "Sport", "1980-1990"]

    df: DataFrame = spark_session.createDataFrame(df_data, df_column)
    expected_df: DataFrame = spark_session.createDataFrame(expected_data, expected_column)

    best_1980_films = films_imdb.films_functions_spark.function_films.function_imdb3.best_films_by_genres_1980th(df)

    best_rows = best_1980_films.collect()
    expected_rows = expected_df.collect()

    assert best_rows == expected_rows


def test_best_films_by_genres_1970th(spark_session):
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
        ["tt0099348", "movie", "Dances with Wolves", 260435, 8.0, 1990, "Western"],
        ["tt0089927", "movie", "Rocky IV", 201574, 6.8, 1985, "Sport"],
        ["tt0077651", "movie", "Halloween", 266227, 7.7, 1978, "Thriller"],
        ["tt0053291", "movie", "Some Like It Hot", 262481, 8.2, 1959, "Music"],
        ["tt1046173", "movie", "G.I. Joe: The Rise of Cobra", 207690, 5.7, 2009, "Sci-Fi"]]

    expected_column = ["tconst", "primaryTitle", "startYear", "genres", "averageRating", "numVotes", "yearRange"]
    expected_data = ["tt0077651", "movie", "Halloween", 266227, 7.7, 1978, "Thriller", "1970-1980"]

    df: DataFrame = spark_session.createDataFrame(df_data, df_column)
    expected_df: DataFrame = spark_session.createDataFrame(expected_data, expected_column)

    best_1970_films = films_imdb.films_functions_spark.function_films.function_imdb3.best_films_by_genres_1970th(df)

    best_rows = best_1970_films.collect()
    expected_rows = expected_df.collect()

    assert best_rows == expected_rows


def test_best_films_by_genres_1960th(spark_session):

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
        ["tt0099348", "movie", "Dances with Wolves", 260435, 8.0, 1990, "Western"],
        ["tt0089927", "movie", "Rocky IV", 201574, 6.8, 1985, "Sport"],
        ["tt0077651", "movie", "Halloween", 266227, 7.7, 1978, "Thriller"],
        ["tt0053291", "movie", "Some Like It Hot", 262481, 8.2, 1959, "Music"],
        ["tt1046173", "movie", "G.I. Joe: The Rise of Cobra", 207690, 5.7, 2009, "Sci-Fi"]]

    expected_column = ["tconst", "primaryTitle", "startYear", "genres", "averageRating", "numVotes", "yearRange"]
    expected_data = ["tt0064116", "movie", "Once Upon a Time in the West", 323645, 8.5, 1968, "Western", "1960-1970"]

    df: DataFrame = spark_session.createDataFrame(df_data, df_column)
    expected_df: DataFrame = spark_session.createDataFrame(expected_data, expected_column)

    best_1960_films = films_imdb.films_functions_spark.function_films.function_imdb3.best_films_by_genres_1960th(df)

    best_rows = best_1960_films.collect()
    expected_rows = expected_df.collect()

    assert best_rows == expected_rows


def test_best_films_by_genres_1950th(spark_session):

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
        ["tt0099348", "movie", "Dances with Wolves", 260435, 8.0, 1990, "Western"],
        ["tt0089927", "movie", "Rocky IV", 201574, 6.8, 1985, "Sport"],
        ["tt0077651", "movie", "Halloween", 266227, 7.7, 1978, "Thriller"],
        ["tt0053291", "movie", "Some Like It Hot", 262481, 8.2, 1959, "Music"],
        ["tt1046173", "movie", "G.I. Joe: The Rise of Cobra", 207690, 5.7, 2009, "Sci-Fi"]]

    expected_column = ["tconst", "primaryTitle", "startYear", "genres", "averageRating", "numVotes", "yearRange"]
    expected_data = ["tt0053291", "movie", "Some Like It Hot", 262481, 8.2, 1959, "Music", "1950-1960"]

    df: DataFrame = spark_session.createDataFrame(df_data, df_column)
    expected_df: DataFrame = spark_session.createDataFrame(expected_data, expected_column)

    best_1950_films = films_imdb.films_functions_spark.function_films.function_imdb3.best_films_by_genres_1950th(df)

    best_rows = best_1950_films.collect()
    expected_rows = expected_df.collect()

    assert best_rows == expected_rows
    