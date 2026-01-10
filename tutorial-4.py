--example 1 : 

print(df.groupby("gender")["salary"].mean())


--Example 2 : 

print(
    df.groupby("gender")["salary"]
      .mean()
      .sort_values(ascending=False)
)

--Example 3 :

print(
    df.groupby("gender")["salary"]
      .agg(["mean", "min", "max"])
)

--Example 4 : 

print(df.nlargest(5, "salary"))

--Example 5 :

print(df.nsmallest(5, "salary"))

--Example 6 : 

df["salary_level"] = df["salary"].apply(
    lambda x: "High" if x > 6500 else "Low"
)

print(df[["salary", "salary_level"]].head())


--Example 7 :

overall_mean = df["salary"].mean()

df["above_average"] = df["salary"] > overall_mean

print(df[["salary", "above_average"]].head())
