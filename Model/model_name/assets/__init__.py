import os # For creating folders
import pandas as pd # For data manipulation
import matplotlib.pyplot as plt # For plotting
import seaborn as sns # For plotting
from sklearn.linear_model import LinearRegression # For regression
from dagster import asset, op, job, Out, AssetMaterialization # For dagster
from dotenv import load_dotenv # For loading environment variables
from ..DataBaseModule.database import DataBaseModule # For database connection

# This handles the path to load the .env file from the DataBaseModule folder
current_path = os.getcwd().split("/")[-1]
substring_start = __file__.rfind(current_path) + len(current_path) + 1
substring_end = __file__.find("/assets")
dotenv_path = __file__[substring_start:substring_end] + "/DataBaseModule/.env"

# Load the .env file
load_dotenv(dotenv_path=dotenv_path)

# This is the startup pipeline, which is run when the model is first loaded
@job
def startup_pipeline():
    db = DataBaseModule()
    db.connect()
    
result = startup_pipeline.execute_in_process()
