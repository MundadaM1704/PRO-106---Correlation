import csv
import numpy as np
import plotly.express as px
import pandas as pd

df = pd.read_csv("./data/cups of coffee_vs_hours of sleep.csv")
fig = px.scatter(df, x="Coffee in ml", y="Sleep in hours",color="week",
                    size_max=60)
fig.show()

def getDataSource(data_path):
    cups_of_coffee = []
    hours_of_sleep = []
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            cups_of_coffee.append(float(row["Coffee in ml"]))
            hours_of_sleep.append(float(row["Sleep in hours"]))

    return {"x" : cups_of_coffee, "y": hours_of_sleep}

def findCorrelation(datasource):
    correlation = np.corrcoef(datasource["x"], datasource["y"])
    print("Correlation between Coffee in ml and sleep in hours :-  \n--->",correlation[0,1])

def setup():
    data_path  = "./data/cups of coffee_vs_hours of sleep.csv"

    datasource = getDataSource(data_path)
    findCorrelation(datasource)

setup()
