import os
import glob
import geopandas as gpd
import pandas as pd
import boto3
import os

# from .service.config import settings

# from .src import get_bucket_files
import re

BUCKET = os.environ.get("BUCKET")
ACCES_KEY = os.environ.get("ACCES_KEY")
SECRET_KEY = os.environ.get("SECRET_KEY")
BASE_PATH_SC = os.environ.get("BASE_PATH_SC")


def get_bucket_files(bckt, ACCESS_KEY, SECRET_KEY, base_path):
    session = boto3.Session(
        aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY
    )

    s3 = session.resource("s3")
    your_bucket = s3.Bucket(bckt)

    s3_files = []
    for my_bucket_object in your_bucket.objects.filter(Prefix=base_path):
        s3_files.append(my_bucket_object.key)
    return s3_files
