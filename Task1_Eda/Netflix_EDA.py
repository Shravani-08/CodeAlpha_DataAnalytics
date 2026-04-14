import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

# ===============================
# 1. LOAD DATASET
# ===============================
file_path = os.path.join("Task1_Eda", "netflix_titles_CLEANED.csv")
df = pd.read_csv(file_path)

# ===============================
# 2. BASIC DATA EXPLORATION
# ===============================
print("=" * 50)
print("NETFLIX DATASET - EXPLORATORY DATA ANALYSIS")
print("=" * 50)

print("\nFirst 5 rows:")
print(df.head())

print("\nDataset Shape:")
print(df.shape)

print("\nColumns:")
print(df.columns)

print("\nDataset Info:")
print(df.info())

print("\nMissing Values:")
print(df.isnull().sum())

# ===============================
# 3. BASIC INSIGHTS
# ===============================
print("\n" + "=" * 50)
print("BASIC INSIGHTS")
print("=" * 50)

print(f"\nTotal Netflix titles: {df.shape[0]}")
print(f"Total columns: {df.shape[1]}")
print(f"Latest release year: {df['release_year'].max()}")

# ===============================
# 4. EDA QUESTIONS
# ===============================
print("\n" + "=" * 50)
print("EDA QUESTIONS")
print("=" * 50)

# Movies vs TV Shows
print("\n1. Movies vs TV Shows:")
print(df['type'].value_counts())

# Top 10 countries
print("\n2. Top 10 Countries:")
print(df['countries'].value_counts().head(10))

# Most common ratings
print("\n3. Most Common Ratings:")
print(df['rating'].value_counts().head(10))

# Top 10 genres
print("\n4. Top 10 Genres:")
print(df['listed_in'].value_counts().head(10))

# Oldest and newest release
print("\n5. Oldest Release Year:")
print(df['release_year'].min())

print("\n6. Latest Release Year:")
print(df['release_year'].max())

# ===============================
# 5. FINAL CONCLUSION
# ===============================
print("\n" + "=" * 50)
print("CONCLUSION")
print("=" * 50)
print("""
- Netflix dataset contains a large collection of movies and TV shows.
- Movies are more common than TV shows.
- Most content comes from a few major countries.
- TV-MA and TV-14 are among the most frequent ratings.
- The dataset has some missing values in directors, cast, and countries.
- Recent years show more Netflix releases, indicating growth in content.
""")