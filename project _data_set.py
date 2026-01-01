import pandas as pd
import numpy as np
import matplotlib.pylab as plt
import seaborn as sns

# Load the Airbnb dataset from a CSV file located at E:\datasets.csv
# The 'encoding_errors' parameter is set to 'ignore' to handle any encoding issues gracefully
data = pd.read_csv(r"E:\datasets.csv", encoding_errors='ignore')

# Display the column names of the dataset to understand the available features
print(data.columns)

# Display the first 5 rows of the dataset for an initial overview
print(data.head())

# Display the last 5 rows of the dataset
print(data.tail())

# Provide a concise summary of the dataset, including data types and non-null counts
print(data.info())

# Generate descriptive statistics for numerical columns, such as mean, std, min, max, etc.
print(data.describe())

# Display the data types of each column
print(data.dtypes)

# Show the dimensions of the dataset (number of rows and columns)
print(data.shape)

# Count the number of missing values in each column
print(data.isnull().sum())

# Remove rows with any missing values from the dataset in place
# This modifies the original DataFrame by dropping rows that contain NaN values
data.dropna(inplace=True)

# Verify that there are no more missing values after dropping
print(data.isnull().sum())

# Count the number of duplicate rows in the dataset
print(data.duplicated().sum())

# Remove duplicate rows from the dataset in place
# The commented line below would show which rows are duplicates if needed
# data[data.duplicated()]
data.drop_duplicates(inplace=True)

# Confirm that duplicates have been removed (should print 0)
print(data.duplicated().sum())

# Type casting: Convert 'id' column to object type (string) for consistency
# This ensures IDs are treated as categorical rather than numerical
data['id'] = data['id'].astype(object)
print(data.dtypes)

# Similarly, convert 'host_id' to object type
data['host_id'] = data['host_id'].astype(object)
print(data.dtypes)

# Filter the dataset to include only listings with price less than 1500
# This creates a subset to focus on more affordable listings and reduce outlier impact in visualizations
df = data[data['price'] < 1500]

# Print the available Seaborn color palettes (for reference, though not directly used here)
print(sns.palettes.SEABORN_PALETTES)

# Set the Seaborn theme to 'notebook' for better visualization in Jupyter-like environments
sns.set_theme('notebook')

# Set the style to 'darkgrid' for a dark background with grid lines
sns.set_style('darkgrid')

# Set the context to 'notebook' with a font scale of 1 for appropriate sizing
sns.set_context('notebook', font_scale=1)

# Create a boxplot to identify outliers in the 'price' column for the filtered data
# Parameters customize the appearance: color, width, linewidth, etc.
sns.boxplot(
    data=df,
    x='price',
    color='#FBAFE4',        # Custom color for the box
    width=0.4,              # Width of the box
    linewidth=1.2,          # Thickness of the box border
    fliersize=5,            # Size of outlier points
    whis=1.5,               # Whisker length as a multiple of IQR
    showmeans=True          # Display the mean value as a point
)
plt.title('identifying outliers in price', fontsize=20)
plt.xlabel('Price', fontsize=10)
plt.show()

# Create a histogram to visualize the distribution of prices
# Custom bins, color, and other parameters for detailed styling
plt.figure(figsize=(8,5))
sns.set_theme('notebook')
sns.set_style('darkgrid')
sns.set_context('notebook', font_scale=1)
sns.histplot(
    data=df,
    x='price',
    bins=[0, 200, 400, 600, 800, 1000, 1200, 1400],  # Custom bin edges
    color='#FFC400',
    kde=True,              # Add a kernel density estimate curve
    edgecolor='white',     # Color of bar edges
    alpha=0.7,             # Transparency level
    stat='count',          # Y-axis shows count of observations
    cumulative=False,      # Not cumulative
    multiple='layer',      # How to handle multiple elements
    discrete=False,        # For continuous data
    linewidth=2            # Thickness of bar edges
)     
plt.title('Price distribution', fontsize=20)
plt.xlabel('Price', fontsize=10)
plt.ylabel('Count', fontsize=10)                  
plt.show()

# Another histogram for the distribution of 'availability_365'
plt.figure(figsize=(6, 3))
sns.histplot(data=df, x='availability_365', color='orange')
plt.title('availability_365 Distribution', fontsize=20)
plt.xlabel('Availability_365', fontsize=10)
plt.ylabel("Frequency", fontsize=10)
plt.show()

# Calculate the average price grouped by 'neighbourhood_group'
# This shows mean prices across different neighborhood groups
avg_price = df.groupby(by='neighbourhood_group')['price'].mean()
print(avg_price)

# Create a new column 'price per bed' by dividing price by the number of beds
# This derives a metric for cost efficiency per bed
data['price per bed'] = data['price'] / data['beds']

# Display the first 5 values of the new column
print(data['price per bed'].head())

# Print all column names again (now including the new one)
print(data.columns)

# Display the first 40 rows of the dataset
print(data.head(40))

# Calculate the average 'price per bed' grouped by 'neighbourhood_group'
avg_price_per_bed = data.groupby(by='neighbourhood_group')['price per bed'].mean()
print(avg_price_per_bed)

# Create a barplot to show average price by neighbourhood group and room type
# Hue parameter differentiates by room type
plt.figure(figsize=(10,6))
sns.barplot(
    data=data, 
    x='neighbourhood_group', 
    y='price', 
    hue='room_type', 
    errorbar=None  # Suppress error bars for cleaner look
)
plt.title('Average Price by Neighbourhood Group and Room Type')
plt.xlabel('Neighbourhood Group')
plt.ylabel('Average Price')
plt.show()

# Scatterplot to explore the relationship between number of reviews and price
# Hue by neighbourhood group to see patterns across groups
plt.figure(figsize=(8, 5))
plt.title("Locality and Review Dependency")
sns.scatterplot(data=data, x='number_of_reviews', y='price', hue='neighbourhood_group')
plt.show()

# Pairplot to visualize pairwise relationships between selected numerical variables
# Hue by room type for differentiation
sns.pairplot(data=df, vars=['price', 'minimum_nights', 'number_of_reviews', 'availability_365'], hue='room_type')
plt.suptitle('Pairplot of Price, Minimum Nights, Number of Reviews, and Availability by Room Type', y=1.02)
plt.show()

# Scatterplot for geographical distribution of listings
# Longitude and latitude plotted, colored by room type
plt.figure(figsize=(10, 7))
sns.scatterplot(data=df, x='longitude', y='latitude', hue='room_type')
plt.title("Geographical Distribution of AirBnb Listing")
plt.show()

# Display data types of the filtered DataFrame (df)
df.dtypes

# Compute the correlation matrix for selected numerical columns
# This measures linear relationships between variables
corr = df[['latitude', 'longitude', 'price', 'minimum_nights', 'number_of_reviews', 'reviews_per_month', 'availability_365', 'beds']].corr()
corr

# Visualize the correlation matrix using a heatmap
# Annotations show the correlation coefficients
plt.figure(figsize=(8, 6))
sns.heatmap(data=corr, annot=True)
plt.show()