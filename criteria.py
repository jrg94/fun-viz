import plotly.express as px
import pandas as pd

df = pd.read_csv("data/2023-criteria.csv")
print(df)

# Compute the percent share for each criteria
group = df.groupby(["Scenario", "Stage"])
totals = group["Count"].transform("sum")
df["Share%"] = (df["Count"] / totals) * 100

# Generate a filter for the rows we want
group = df.groupby(["Scenario", "Stage"])
idx = group["Share%"].transform(max) == df["Share%"]

# Overwrite the Share%
df["Share%"] = group["Share%"].transform(lambda x: x.max() - x.min())

# Plot
fig = px.bar(
    df[idx], 
    x="Scenario", 
    y="Share%", 
    color="Stage", 
    text="Criteria", 
    barmode='group'
)
fig.write_html('first_figure.html', auto_open=True)
