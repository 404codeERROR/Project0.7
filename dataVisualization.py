import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Sample data
data = {
    'Department': ['HR', 'Finance', 'Marketing', 'IT', 'Sales'],
    'Employees': [15, 25, 30, 20, 35]
}

df = pd.DataFrame(data)

# Bar plot
sns.barplot(x='Department', y='Employees', data=df)
plt.title("Employees in Each Department")
plt.show()

# Pie chart
plt.pie(df['Employees'], labels=df['Department'], autopct='%1.1f%%')
plt.title("Employee Distribution")
plt.show()