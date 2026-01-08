import pandas as pd

# Read dataset
df = pd.read_csv("MOCK_DATA.csv")

# Example 1: head() default and custom value
print("Example 1: First 5 rows")
print(df.head())
print("-" * 50)

print("Example 1.1: First 10 rows")
print(df.head(10))
print("-" * 50)

# Example 2: Dataset information
print("Example 2: Dataset info")
print(df.info())
print("-" * 50)

# Example 3: Sort salary ascending and show lowest values
print("Example 3: Lowest salaries")
print(df.sort_values("salary").head(10))
print("-" * 50)

# Example 4: Sort salary descending and show highest values
print("Example 4: Highest salaries")
print(df.sort_values("salary", ascending=False).head(5))
print("-" * 50)

# Example 5: Filter salaries greater than 6000
print("Example 5: Salary greater than 6000")
print(df[df["salary"] > 6000].head(15))
print("-" * 50)

# Example 6: Multiple conditions filtering
print("Example 6: Salary > 6000 and Gender = Female")
filtered_df = df[(df["salary"] > 6000) & (df["gender"] == "Female")]
print(filtered_df.head())
