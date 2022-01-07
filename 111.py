import plotly.figure_factory as ff
import plotly_graph objects as go
import statistics
import random
import pandas as pd
import csv
df=pd.read_csv("studentsmark.csv")
data=df["marks_score"].tolist()
fig=ff.create_distplot([data],["math scores"],show_hist=false)
fig.show()
mean=statistics.mean(data)
standarddeviation=statistics.stdev(data)