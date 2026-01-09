--Example 1 

print(df["gender"].unique())

--Example 2 

print(df["gender"].value_counts())

--Example 3 

print(df["salary"].mean())

--Example 4 

print(df["salary"].min())
print(df["salary"].max())

--Example 5 

print(df["salary"].median())

--Example 6 

print(df["salary"].std())

--Example 7 

print(df["salary"].quantile([0.25, 0.5, 0.75]))

