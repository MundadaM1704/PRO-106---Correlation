import csv
import numpy as np
import plotly.express as px
import pandas as pd

df = pd.read_csv("./data/studentMarks_vs_daysPresent.csv")
fig = px.scatter(df, x="Marks In Percentage", y="Days Present",color="Roll No",
                    size_max=60)
fig.show()

def getDataSource(data_path):
    marks_in_percentage = []
    days_present = []
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            marks_in_percentage.append(float(row["Marks In Percentage"]))
            days_present.append(float(row["Days Present"]))

    return {"x" : marks_in_percentage, "y": days_present}

def findCorrelation(datasource):
    correlation = np.corrcoef(datasource["x"], datasource["y"])
    print("Correlation between Marks in percentage and Days present :-  \n--->",correlation[0,1])

def setup():
    data_path  = "./data/studentMarks_vs_daysPresent.csv"

    datasource = getDataSource(data_path)
    findCorrelation(datasource)

setup()