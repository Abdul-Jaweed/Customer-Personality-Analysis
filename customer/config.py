import pymongo
import numpy as np
import pandas as pd
import json
import os
import sys
from dataclasses import dataclass


@dataclass
class EnvironmentVariables:
    mongo_db_url = os.getenv("MONGO_DB_URL")



env_var = EnvironmentVariables()
mongo_client = pymongo.MongoClient(env_var, mongo_db_url)
TARGET_COLUMN = "Response"
print(env_var.mongo_db_url)()






# Cloud like AWS 
# key acesses and Secret keys
    