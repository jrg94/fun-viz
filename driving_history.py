import matplotlib.pyplot as plt
import pandas as pd

# Load
df = pd.read_csv("data/2020-driving-history.csv")

# Clean
df["Start Time"] = pd.to_datetime(df["Start Time"])
df["Trip Time"] = pd.to_timedelta(df["Trip Time"])
df["Idle Time"] = pd.to_timedelta(df["Idle Time"])

# Manipulate
to_plot = df.resample("D", on="Start Time").agg(
    {
        "Total Distance (mi)": sum,
        #"Trip Time": sum,
        #"Idle Time": sum,
        "Top Speed (mph)": max
    }
)

print(to_plot)

# Plot
to_plot.plot.area(subplots=True)
plt.show()
