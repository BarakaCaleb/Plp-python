# Task 1: Load and Explore the Dataset
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

# Load dataset (with error handling if using CSV)
try:
    # Example with Iris dataset
    iris = load_iris(as_frame=True)
    df = iris.frame
    df['species'] = df['target'].map(dict(zip(range(3), iris.target_names)))
except FileNotFoundError:
    print("Dataset not found. Please check the file path.")
except Exception as e:
    print("Error loading dataset:", e)

# Display first few rows
print("First 5 rows of the dataset:")
print(df.head())

# Explore structure
print("\nDataset Info:")
print(df.info())

# Check for missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Clean data (Iris has no missing, but example shown)
df = df.dropna()

# Task 2: Basic Data Analysis
print("\nStatistical Summary:")
print(df.describe())

# Grouping example: Average petal length per species
grouped = df.groupby("species")["petal length (cm)"].mean()
print("\nAverage petal length per species:")
print(grouped)

# Interesting pattern
print("\nObservation: Virginica tends to have the longest petals on average.")

# Task 3: Data Visualization
plt.style.use("seaborn-v0_8")

# 1. Line chart (fake trend: cumulative petal length over index just for demo)
df["petal length (cm)"].cumsum().plot(kind="line", title="Cumulative Petal Length")
plt.xlabel("Index")
plt.ylabel("Cumulative Petal Length")
plt.show()

# 2. Bar chart (average petal length per species)
grouped.plot(kind="bar", title="Average Petal Length by Species", color=["skyblue", "orange", "green"])
plt.xlabel("Species")
plt.ylabel("Average Petal Length (cm)")
plt.show()

# 3. Histogram (distribution of sepal length)
df["sepal length (cm)"].plot(kind="hist", bins=20, title="Distribution of Sepal Length")
plt.xlabel("Sepal Length (cm)")
plt.show()

# 4. Scatter plot (sepal length vs petal length)
plt.figure(figsize=(6,4))
sns.scatterplot(data=df, x="sepal length (cm)", y="petal length (cm)", hue="species", palette="deep")
plt.title("Sepal Length vs Petal Length by Species")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Petal Length (cm)")
plt.legend(title="Species")
plt.show()
