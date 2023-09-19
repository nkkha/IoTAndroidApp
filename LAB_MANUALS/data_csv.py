import pandas as pd
import matplotlib.pyplot as plt

file_path = "temp-20230919-1248.csv"
df = pd.read_csv(file_path)

df = df[['created_at', 'value']]

df['created_at'] = pd.to_datetime(df['created_at'])

plt.figure(figsize=(12, 6))
plt.plot(df['created_at'], df['value'], linestyle='-', color='b')
plt.title('Temperature Data Over Time')
plt.xlabel('Timestamp')
plt.ylabel('Temperature (°C)')
plt.grid(True)

plt.show()