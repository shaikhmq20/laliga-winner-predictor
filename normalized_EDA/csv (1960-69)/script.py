# Importing necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Importing the dataset
la_liga = pd.read_csv('la_liga_dataset.csv')

# Selecting relevant columns
la_liga = la_liga[['Position', 'Team', 'Played', 'Won', 'Drawn', 'Lost', 'Goals For', 'Goals Against', 'Goal Difference', 'Points']]

# Previewing the dataset
print(la_liga.head())

# Checking the shape of the dataset
print(la_liga.shape)

# Checking the data types of the variables
print(la_liga.dtypes)

# Checking for missing values
print(la_liga.isnull().sum())

# Summary statistics of the variables
print(la_liga.describe())

# Visualizing the distribution of a variable
sns.histplot(la_liga['Points'], kde=True)
plt.show()

# Visualizing the relationship between two variables
sns.scatterplot(x='Goals For', y='Points', data=la_liga)
plt.show()

# Correlation matrix of the variables
sns.heatmap(la_liga.corr(), annot=True, cmap='coolwarm')
plt.show()
