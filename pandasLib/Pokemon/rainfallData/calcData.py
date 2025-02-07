import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("pandasLib/Pokemon/rainfallData/Document1.csv")

print("---------York----------")

yorkAvarage = df["York"].mean()
yorkWettestMonth = df.loc[df["York"].idxmax(), "Month"]
yorkDryestMonth = df.loc[df["York"].idxmin(), "Month"]

print(f"Average: {yorkAvarage}ml")
print(f"Wettest: {yorkWettestMonth}")
print(f"Wettest: {yorkDryestMonth}")

print("\n---------London----------")

yorkAvarage = df["London"].mean()
yorkWettestMonth = df.loc[df["London"].idxmax(), "Month"]
yorkDryestMonth = df.loc[df["London"].idxmin(), "Month"]

print(f"Average: {yorkAvarage}ml")
print(f"Wettest: {yorkWettestMonth}")
print(f"Wettest: {yorkDryestMonth}")


print("\n---------Paris----------")

yorkAvarage = df["Paris"].mean()
yorkWettestMonth = df.loc[df["Paris"].idxmax(), "Month"]
yorkDryestMonth = df.loc[df["Paris"].idxmin(), "Month"]

print(f"Average: {yorkAvarage}ml")
print(f"Wettest: {yorkWettestMonth}")
print(f"Wettest: {yorkDryestMonth}")

print("\n---------Barcelona----------")

yorkAvarage = df["Barcelona"].mean()
yorkWettestMonth = df.loc[df["Barcelona"].idxmax(), "Month"]
yorkDryestMonth = df.loc[df["Barcelona"].idxmin(), "Month"]

print(f"Average: {yorkAvarage}ml")
print(f"Wettest: {yorkWettestMonth}")
print(f"Wettest: {yorkDryestMonth}")

# Plot data
df.plot(x="Month", y=["York", "London", "Paris", "Barcelona"], kind="bar")
plt.show()