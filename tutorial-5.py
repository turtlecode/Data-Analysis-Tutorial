--Example 1 :

print(df.duplicated().sum())

--Example 2 :

print(df[df.duplicated()])

--Example 3 :

df = df.drop_duplicates()
print(df.shape)

--Example 4 :

df["email_length"] = df["email"].str.len()
print(df[["email", "email_length"]].head())


--Example 5 :

df["email_lower"] = df["email"].str.upper()
print(df[["email", "email_lower"]].head())

--Example 6 :

df["email_domain"] = df["email"].str.split("@").str[1]
print(df["email_domain"].value_counts().head())
