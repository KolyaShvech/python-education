import pytest
from pyspark.sql import SparkSession, DataFrame
import films_imdb.films_functions_spark.function_films.function_imdb1


# Get one spark session for the whole test session
@pytest.fixture(scope="session")
def spark_session():
    return SparkSession.builder.getOrCreate()


def test_join_dataframe(spark_session):
    """
    Check func join_dataframe.
    """

    # Set up test column1
    df_column1 = ["tconst", "name", "last_name"]
    # Set up test data1
    df_data1 = [
        [1, "Semen", "Salo"],
        [2, "Anna", "Sunny"],
        [3, "Oleh", "Goroh"]]
    # Set up test column2
    df_column2 = ["tconst", "City"]
    # Set up test data2
    df_data2 = [
        [1, "Summy"],
        [2, "Kyev"],
        [3, "Kharkov"]]

    expected_column = ["tconst", "name", "last_name", "City"]

    expected_data = [[1, "Semen", "Salo", "Summy"],
                     [2, "Anna", "Sunny", "Kyev"],
                     [3, "Oleh", "Goroh", "Kharkov"]]
    # Create Dataframe
    df1: DataFrame = spark_session.createDataFrame(df_data1, df_column1)

    df2: DataFrame = spark_session.createDataFrame(df_data2, df_column2)

    expected_join: DataFrame = spark_session.createDataFrame(expected_data, expected_column)
    #  apply func join_dataframe
    joined_df = films_imdb.films_functions_spark.function_films.function_imdb1.join_dataframe(df1, df2)
    # Gather result rows
    rows = joined_df.collect()
    expected_rows = expected_join.collect()
    # Compare dataframes row by row
    assert rows == expected_rows


def test_best_films_all_time(spark_session):
    """
    Check func best films all time.
    """
    # Set up test column
    df_column = ["tconst", "titleType", "primaryTitle", "numVotes", "averageRating", "startYear"]
    # Set up test data
    df_data = [
        ["tt0000001", "short", "Carmencita", 1882, 5.7, 1894],
        ["tt0000009", "short", "Miss Jerry", 6803, 6.9, 1894],
        ["tt0068646", "movie", "The Godfather", 1785878, 9.2, 1972],
        ["tt0468569", "movie", "The Dark Knight", 2561375, 9.0, 2008],
        ["tt0816692", "movie", "Interstellar", 1733494, 8.6, 2014],
        ["tt0064116", "movie", "Once Upon a Time in the West", 323645, 8.5, 1968]
    ]

    expected_column = ["tconst", "primaryTitle", "numVotes", "averageRating", "startYear"]

    expected_data = [
        ["tt0068646", "The Godfather", 1785878, 9.2, 1972],
        ["tt0468569", "The Dark Knight", 2561375, 9.0, 2008],
        ["tt0816692", "Interstellar", 1733494, 8.6, 2014],
        ["tt0064116", "Once Upon a Time in the West", 323645, 8.5, 1968]
    ]
    # create Dataframe
    df: DataFrame = spark_session.createDataFrame(df_data, df_column)

    expected_df: DataFrame = spark_session.createDataFrame(expected_data, expected_column)
    # apply func best_films_all_time
    films = films_imdb.films_functions_spark.function_films.function_imdb1.best_films_all_time(df)
    # Gather result rows
    rows = films.collect()
    expected_rows = expected_df.collect()
    # Compare dataframes row by row
    assert rows == expected_rows


def test_best_films_for_last_10_years(spark_session):
    # Set up test column
    df_column = ["tconst", "titleType", "primaryTitle", "numVotes", "averageRating", "startYear"]
    # Set up test data
    df_data = [
        ["tt0000001", "short", "Carmencita", 1882, 5.7, 1894],
        ["tt0000009", "short", "Miss Jerry", 6803, 6.9, 1894],
        ["tt0068646", "movie", "The Godfather", 1785878, 9.2, 1972],
        ["tt0468569", "movie", "The Dark Knight", 2561375, 9.0, 2008],
        ["tt0816692", "movie", "Interstellar", 1733494, 8.6, 2014],
        ["tt0064116", "movie", "Once Upon a Time in the West", 323645, 8.5, 1968],
        ["tt4154796", "movie", "Avengers: Endgame", 1055700, 8.4, 2019]
    ]

    expected_column = ["tconst", "primaryTitle", "numVotes", "averageRating", "startYear"]

    expected_data = [
        ["tt0816692", "Interstellar", 1733494, 8.6, 2014],
        ["tt4154796", "Avengers: Endgame", 1055700, 8.4, 2019]]
    # Create Dataframe
    df: DataFrame = spark_session.createDataFrame(df_data, df_column)

    expected_df = spark_session.createDataFrame(expected_data, expected_column)
    # Apply func best_films_for_last_10_years
    films_from_2012 = films_imdb.films_functions_spark.function_films.function_imdb1.best_films_for_last_10_years(df)
    # Gather result rows
    row = films_from_2012.collect()
    expected_row = expected_df.collect()
    # Compare dataframes row by row
    assert row == expected_row


def test_best_films_in_60h_years(spark_session):
    # Set up test column
    df_column = ["tconst", "titleType", "primaryTitle", "numVotes", "averageRating", "startYear"]
    # Set up test data
    df_data = [
        ["tt0000001", "short", "Carmencita", 1882, 5.7, 1894],
        ["tt0000009", "short", "Miss Jerry", 6803, 6.9, 1894],
        ["tt0068646", "movie", "The Godfather", 1785878, 9.2, 1972],
        ["tt0468569", "movie", "The Dark Knight", 2561375, 9.0, 2008],
        ["tt0816692", "movie", "Interstellar", 1733494, 8.6, 2014],
        ["tt0064116", "movie", "Once Upon a Time in the West", 323645, 8.5, 1968],
        ["tt4154796", "movie", "Avengers: Endgame", 1055700, 8.4, 2019]
    ]

    expected_column = ["tconst", "primaryTitle", "numVotes", "averageRating", "startYear"]

    expected_data = [["tt0064116", "Once Upon a Time in the West", 323645, 8.5, 1968]]
    # Create Dataframe
    df: DataFrame = spark_session.createDataFrame(df_data, df_column)

    expected_df: DataFrame = spark_session.createDataFrame(expected_data, expected_column)
    # Apply func best_films_in_60h_years
    films_1960 = films_imdb.films_functions_spark.function_films.function_imdb1.best_films_in_60h_years(df)
    # Gather result rows
    row = films_1960.collect()
    expected_row = expected_df.collect()
    # Compare dataframes row by row
    assert row == expected_row





