import plotly.figure_factory as ff 
import plotly.graph_objects as po 
import csv
import pandas as pd 
import statistics

df = pd.read_csv("meduim_data.csv")
data = df["Math_score"].tolist()