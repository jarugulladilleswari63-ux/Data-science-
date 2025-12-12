import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv(r"C:\Users\dilleshwari\OneDrive\Desktop\weatherHistory.csv")

# Convert date column correctly (handles timezone)
df['Formatted Date'] = pd.to_datetime(df['Formatted Date'], utc=True, errors='coerce')

# Drop rows where date is missing
df = df.dropna(subset=['Formatted Date'])

# Extract year & month
df['Year'] = df['Formatted Date'].dt.year
df['Month'] = df['Formatted Date'].dt.month_name()

# -----------------------------
# Temperature Trend Line
# -----------------------------
plt.figure(figsize=(12,5))
plt.plot(df['Formatted Date'], df['Temperature (C)'])
plt.title("Daily Temperature Trend")
plt.xlabel("Date")
plt.ylabel("Temperature (C)")
plt.grid()
plt.show()

# -----------------------------
# Monthly Average Temperature
# -----------------------------
monthly_temp = df.groupby('Month')['Temperature (C)'].mean().reindex([
    'January','February','March','April','May','June',
    'July','August','September','October','November','December'
])

plt.figure(figsize=(10,5))
monthly_temp.plot(kind='line', marker='o')
plt.title("Average Monthly Temperature")
plt.ylabel("Temperature (C)")
plt.grid()
plt.show()

# -----------------------------
# Weather Summary Frequency
# -----------------------------
plt.figure(figsize=(10,5))
df['Summary'].value_counts().head(10).plot(kind='bar')
plt.title("Most Common Weather Conditions")
plt.xlabel("Condition")
plt.ylabel("Count")
plt.show()

# -----------------------------
# Correlation Heatmap
# -----------------------------
plt.figure(figsize=(8,5))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()
