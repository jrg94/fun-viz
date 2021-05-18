import matplotlib.pyplot as plt
import pandas as pd

# Load
df = pd.read_csv("data/2020-driving-history.csv")

# Clean
df["Start Time"] = pd.to_datetime(df["Start Time"])
df["Trip Time"] = pd.to_timedelta(df["Trip Time"])
df["Idle Time"] = pd.to_timedelta(df["Idle Time"])

# Manipulate
daily_resample = df.resample("D", on="Start Time").agg(
    {
        "Total Distance (mi)": sum,
        "Top Speed (mph)": max,
        "Trip Time": sum,
        "Idle Time": sum,
        "Average Speed (mph)": pd.DataFrame.mean,
        "Average mpg": pd.DataFrame.mean,
        "Fuel Used (gal)": sum
    }
)

daily_resample["Trip Time"] = daily_resample["Trip Time"].dt.total_seconds()
daily_resample["Idle Time"] = daily_resample["Idle Time"].dt.total_seconds()

# Plot
daily_resample.plot.area(subplots=True)

plt.tight_layout()
plt.show()
