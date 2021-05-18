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

pd.set_option('display.max_columns', None)
print(daily_resample.head())

# Plot
plt.show()
