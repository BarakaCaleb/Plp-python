# Task 1: Load and Explore the Dataset
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

# Load dataset
try:
    iris = load_iris(as_frame=True)
    df = iris.frame   # pandas DataFrame
    df['species'] = df['target'].map(dict(enumerate(iris.target_names)))  # map species names
    print("Dataset loaded successfully")
except FileNotFoundError:
    print("File not found. Please check dataset path.")
except Exception as e:
    print("⚠️ Error loading dataset:", e)

# Display first few rows
print("\nFirst 5 rows of dataset:")
print(df.head())

# Dataset structure
print("\nDataset Info:")
print(df.info())

# Check missing values
print("\nMissing values per column:")
print(df.isnull().sum())

# (Iris dataset has no missing values, but if needed)
df = df.dropna()

# Task 2: Basic Data Analysis
print("\nDescriptive statistics:")
print(df.describe())

# Group by species and compute mean
grouped = df.groupby("species").mean()
print("\nAverage values per species:")
print(grouped)

# Observations (example)
print("\nObservations:")
print("- Setosa flowers generally have smaller petals.")
print("- Virginica species has the largest petal length and width.")
print("- Sepal length tends to increase from Setosa → Versicolor → Virginica.")

# Task 3: Data Visualization
plt.figure(figsize=(12, 8))

# 1. Line chart (simulate trend: sepal length across samples)
plt.subplot(2, 2, 1)
plt.plot(df.index, df['sepal length (cm)'], label="Sepal Length")
plt.title("Line Chart: Sepal Length Across Samples")
plt.xlabel("Sample Index")
plt.ylabel("Sepal Length (cm)")
plt.legend()

# 2. Bar chart (mean petal length per species)
plt.subplot(2, 2, 2)
grouped['petal length (cm)'].plot(kind='bar', color=['skyblue', 'orange', 'green'])
plt.title("Bar Chart: Avg Petal Length by Species")
plt.ylabel("Petal Length (cm)")

# 3. Histogram (distribution of sepal width)
plt.subplot(2, 2, 3)
plt.hist(df['sepal width (cm)'], bins=15, color="purple", alpha=0.7)
plt.title("Histogram: Sepal Width Distribution")
plt.xlabel("Sepal Width (cm)")
plt.ylabel("Frequency")

# 4. Scatter plot (sepal length vs petal length)
plt.subplot(2, 2, 4)
sns.scatterplot(data=df, x="sepal length (cm)", y="petal length (cm)", hue="species")
plt.title("Scatter Plot: Sepal Length vs Petal Length")

plt.tight_layout()
plt.show()
