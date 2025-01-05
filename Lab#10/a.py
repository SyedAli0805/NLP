import pandas as pd

data = {
"Name": ["Alice", "Bob", "Charlie"],
"Age": [24, 27, 22],
"City": ["New York", "Los Angeles", "Chicago"]
}
df = pd.DataFrame(data)

print("DataFrame:\n", df)

print("First Row:\n", df.loc[0])
print("Names Column:\n", df["Name"])