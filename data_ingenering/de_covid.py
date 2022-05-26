""" Module which implement trasportiration data to the database. Changed headers."""
import os
import boto3
import pandas as pd
import sqlalchemy


BUCKET_NAME = "test_data"
HEADERS = ['Date of notification', 'Country of reference', 'Code of the Region',
                'Name of the Region', 'Code of the Province', 'Name of the Provine',
                'Province abbreviation', 'Latitude', 'Longitude',
                'Total amount of positive cases', 'Notes in italian language', 'Code nut 1',
           'Code nut 2', 'Code nut 3']


def read_csv_file():
    """
    Create function read csv file from minio and replace column in table.
    """
    s3 = boto3.resource("s3",
            endpoint_url=os.environ.get('MINIO_HOST'),
            aws_access_key_id=os.environ.get("MINIO_ROOT_USER"),
            aws_secret_access_key=os.environ.get('MINIO_ROOT_PASSWORD'))

    test_bucket = s3.Bucket('test_data')
    for bucket in test_bucket.objects.all():  # iteration for tables.
        df = pd.read_csv(bucket.get()['Body'], names=HEADERS, header=0)
        yield df


def write_db():
    """
    Create function write to csv file. Use sqlalchemy.
    """
    post_ges = os.environ.get("POSTGRES_USER")
    password = os.environ.get("POSTGRES_PASSWORD")
    engine = sqlalchemy.create_engine(f'postgresql://{post_ges}:{password}@localhost/postgres')
    print(engine)
    for file in read_csv_file():
        file.to_sql('Covid italy', con=engine, if_exists='append')


if __name__ == "__main__":
    write_db()
