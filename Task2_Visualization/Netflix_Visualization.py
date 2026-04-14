import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Load dataset
file_path = os.path.join("Task2_Visualization", "netflix_titles_CLEANED.csv")
df = pd.read_csv(file_path)

# Style
sns.set(style="whitegrid")

# ===============================
# 1. Movies vs TV Shows
# ===============================
plt.figure(figsize=(8, 5))
sns.countplot(x='type', data=df)
plt.title("Movies vs TV Shows on Netflix")
plt.xlabel("Type")
plt.ylabel("Count")
plt.show()

# ===============================
# 2. Top 10 Ratings
# ===============================
plt.figure(figsize=(10, 5))
df['rating'].value_counts().head(10).plot(kind='bar')
plt.title("Top 10 Content Ratings")
plt.xlabel("Rating")
plt.ylabel("Count")
plt.show()

# ===============================
# 3. Release Year Trend
# ===============================
plt.figure(figsize=(12, 5))
df['release_year'].value_counts().sort_index().tail(20).plot(kind='line')
plt.title("Netflix Releases Over Last 20 Years")
plt.xlabel("Year")
plt.ylabel("Number of Releases")
plt.show()

# ===============================
# 4. Top 10 Countries
# ===============================
plt.figure(figsize=(12, 5))
df['countries'].value_counts().head(10).plot(kind='bar')
plt.title("Top 10 Countries Producing Netflix Content")
plt.xlabel("Country")
plt.ylabel("Count")
plt.show()

# ===============================
# 5. Top 10 Genres
# ===============================
plt.figure(figsize=(12, 5))
df['listed_in'].value_counts().head(10).plot(kind='bar')
plt.title("Top 10 Netflix Genres")
plt.xlabel("Genre")
plt.ylabel("Count")
plt.xticks(rotation=45)
plt.show()