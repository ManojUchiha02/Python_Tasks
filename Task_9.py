import pandas as pd
import plotly.express as px
excel_file = "Heatmap sheet.xlsx"
data = pd.read_excel(excel_file)
color_scale = [[0.0, 'lightgreen'],
               [0.2, 'palegreen'],
               [0.4, 'mediumseagreen'],
               [0.6, 'seagreen'],
               [0.8, 'darkseagreen'],
               [1.0, 'darkgreen'],
               ]
fig = px.treemap(data, path=['Area'], values='Existing Team Members Proficient with this area', color='Average Team Expertise C(1 -5)', color_continuous_scale=color_scale)
fig.update_layout(
    title="Variable-Sized Rectangle TreeMap",
    width=1600,
    height=800,
    autosize=True,)
fig.show()
