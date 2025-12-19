import pandas as pd
import matplotlib.pyplot as plt

# Read CSV file
df = pd.read_csv('daily_vaccinations_20201214_20210615.csv')

# Convert date column to datetime (assuming you have a date column)
# Replace 'date' with your actual date column name
# df['Date'] = pd.to_datetime(df['Date'])  # Add this line

# Create the plot
plt.figure(figsize=(12, 6))
plt.plot(df['Date'], df['Administered_Daily'])  # Plot against actual dates
plt.title('Daily Vaccinations Over Time')
plt.xlabel('Date')
plt.ylabel('Daily Vaccinations Administered')
plt.xticks(rotation=45)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()