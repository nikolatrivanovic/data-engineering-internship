import pandas as pd
import matplotlib.pyplot as plt

file_path = 'avg.csv'

data = pd.read_csv(file_path)

data['date'] = pd.to_datetime(data['date'])

data = data.sort_values(by='date')

plt.figure(figsize=(20, 6))
plt.plot(data['date'], data['pollution_total_visitor'], marker='o', color='b', label='Pollution Total Visitor')
plt.title('Pollution Total Visitor Over Time')
plt.xlabel('Date')
plt.ylabel('Pollution Total Visitor')
plt.grid(True)
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
