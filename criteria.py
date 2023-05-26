import plotly.express as px
import pandas as pd

df = pd.read_csv("data/2023-criteria.csv")

# Compute the percent share for each criteria
group = df.groupby(["Scenario", "Stage"])
totals = group["Count"].transform("sum")
df["Share%"] = (df["Count"] / totals) * 100

# Scale all odd rows to have negative shares
df.loc[df.index % 2 == 1, "Share%"] *= -1

# Generate a filter for the rows we want
group = df.groupby(["Scenario", "Stage"])
idx = group["Count"].transform(lambda x : x.max()) == df["Count"]

# Overwrite the Share%
df["Share%"] = group["Share%"].transform(lambda x: x.max() + x.min())

print(df)

# Plot
fig = px.bar(
    df[idx], 
    y="Scenario", 
    x="Share%", 
    color="Stage", 
    text="Criteria", 
    barmode='group',
    orientation="h",
    range_x=[-100,100],
    category_orders={"Stage": ["Beliefs", "Behaviors"]}
)
fig.update_yaxes(autorange="reversed")
fig.write_html('first_figure.html', auto_open=True)
