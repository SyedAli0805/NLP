import pandas as pd

data = {
"Name": ["Alice", "Bob", "Charlie"],
"Age": [24, None, 22],
"City": ["New York", "Los Angeles", None]
}
df = pd.DataFrame(data)


df_cleaned = df.dropna()
print("DataFrame after removing missing values:\n", df_cleaned)


df_filled = df.fillna({"Age": 25, "City": "Unknown"})
print("DataFrame after replacing missing values:\n", df_filled)