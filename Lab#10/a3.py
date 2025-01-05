import pandas as pd
import matplotlib.pyplot as plt

data = {
"Duration": [30, 45, 60, 90],
"Calories": [100, 200, 300, 400]
}
df = pd.DataFrame(data)

df.plot(kind='scatter', x='Duration', y='Calories', title="Duration vs Calories")
plt.show()