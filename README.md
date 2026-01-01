📌 Project Title

Exploratory Data Analysis (EDA) of Airbnb Listings Dataset using Python

🎯 Project Objective

The main objective of this project is to analyze Airbnb listing data to:

Understand price distribution

Identify outliers

Study the effect of location, room type, and availability on pricing

Create meaningful visualizations for business insights

Perform data cleaning, transformation, and correlation analysis

This project demonstrates real-world data analyst skills such as data preprocessing, visualization, and insight generation 

project _data_set

.

🧰 Tools & Libraries Used
Tool	Purpose
Pandas	Data loading, cleaning, manipulation
NumPy	Numerical operations
Matplotlib	Base plotting
Seaborn	Advanced statistical visualizations
📂 Step-by-Step Project Explanation
1️⃣ Data Loading
data = pd.read_csv(r"E:\datasets.csv", encoding_errors='ignore')

Why?

Loads Airbnb data from a CSV file

encoding_errors='ignore' ensures the program does not crash due to text encoding issues

📌 Real-world relevance: Datasets often contain messy encodings.

2️⃣ Initial Data Understanding

You inspect the dataset using:

data.columns

data.head()

data.tail()

data.info()

data.describe()

data.shape

What you learn:

Column names

Data types

Number of rows & columns

Statistical summary (mean, min, max, etc.)

📌 Purpose: Understand structure before analysis.

3️⃣ Handling Missing Values
data.isnull().sum()
data.dropna(inplace=True)

Why?

Missing values distort analysis

Dropping them ensures clean insights

📌 Interview tip: Always justify missing value treatment.

4️⃣ Handling Duplicate Records
data.duplicated().sum()
data.drop_duplicates(inplace=True)

Why?

Duplicate rows can bias results

Removing them improves data accuracy

5️⃣ Data Type Conversion
data['id'] = data['id'].astype(object)
data['host_id'] = data['host_id'].astype(object)

Why?

IDs are categorical, not numerical

Prevents incorrect mathematical operations

📌 Good data modeling practice

6️⃣ Filtering Out Extreme Prices
df = data[data['price'] < 1500]

Why?

Removes extreme outliers

Improves visualization clarity

Focuses on realistic pricing

📌 Business logic applied

7️⃣ Price Outlier Detection (Boxplot)
sns.boxplot(x='price', data=df, showmeans=True)

Insight:

Detects unusually high prices

Mean and IQR visible

Helps decide filtering thresholds

📌 Used in anomaly detection

8️⃣ Price Distribution Analysis (Histogram)
sns.histplot(x='price', bins=[0,200,...,1400], kde=True)

Insight:

Most listings fall in lower price ranges

Right-skewed distribution

KDE curve shows density trend

📌 Used for pricing strategy

9️⃣ Availability Analysis
sns.histplot(x='availability_365')

Insight:

Many listings are available for most of the year

Helps understand host behavior

🔟 Average Price by Location
avg_price = df.groupby('neighbourhood_group')['price'].mean()

Insight:

Price varies significantly by neighborhood

Prime locations cost more

📌 Location-based pricing analysis

1️⃣1️⃣ Feature Engineering – Price per Bed
data['price per bed'] = data['price'] / data['beds']

Why?

Better metric than raw price

Shows value for money

📌 Advanced analytical thinking

1️⃣2️⃣ Room Type vs Price (Bar Plot)
sns.barplot(x='neighbourhood_group', y='price', hue='room_type')

Insight:

Entire homes cost more than private/shared rooms

Room type strongly affects price

1️⃣3️⃣ Reviews vs Price (Scatter Plot)
sns.scatterplot(x='number_of_reviews', y='price', hue='neighbourhood_group')

Insight:

High reviews do not always mean high price

Shows popularity vs pricing imbalance

1️⃣4️⃣ Multivariate Analysis (Pairplot)
sns.pairplot(vars=[price, minimum_nights, reviews, availability])

Why?

Understand relationships between multiple variables

Detect patterns across room types

📌 Exploratory analysis skill

1️⃣5️⃣ Geographical Distribution
sns.scatterplot(x='longitude', y='latitude', hue='room_type')

Insight:

Clustering of listings

Shows geographic concentration of room types

1️⃣6️⃣ Correlation Analysis
corr = df[[...]].corr()
sns.heatmap(corr, annot=True)

Insight:

Weak correlation between price and reviews

Availability moderately correlated with reviews

Location has minimal linear impact on price

📌 Business insight generation

✅ Final Conclusion

This project successfully:

✔ Cleaned real-world data
✔ Applied EDA techniques
✔ Created meaningful visualizations
✔ Derived pricing insights
✔ Demonstrated analytical thinking
