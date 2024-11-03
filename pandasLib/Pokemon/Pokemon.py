import pandas as pd

# cheetsheet for pandas library 

# read from file, delimiter = what seperates data in the file, "\t" = tab
# df sort for DataFrame 
df = pd.read_csv("code python\pandasLib\Pokemon\pokemon_data.csv",delimiter="\t")
# df = pd.read_excel("code python\pandasLib\Pokemon\pokemon_data.xlsx)
# df = pd.read_csv("code python\pandasLib\Pokemon\pokemon_data.txt",delimiter="\t")

# head = top rows, tail = bottom rows, default = 5
# print(df.head(x)) x specifies how many rows 
# print(df.tail(x)) 

# df.columns = all available columns
# df.iloc[x] = specific row 
# df.ilo[x,y] = coordinates for specific row and column

# used to print a specific column/columns 
# print(df["Name"])
# print(df[["Name","Attack"]])

# outputs all rows where type 1 = fire
# print (df.loc[df["Type 1"] == "Fire"])
# print (df.loc[df["Speed"] == max(df["Speed"])])

# quickly generating descriptive statistics of a DataFrame
# print(df.describe())

# for itterating through data frame rows 
# for index,row in df.iterrows():
   # print(index,row["Name"])

# for statistics 
# print(df["Attack"].mean())
# print(df["Attack"].sum())
# print(df["Attack"].max())
# print(df["Attack"].min())

# for sorting DataFrame
# print(df.sort_values("HP"))# default is ascending 
# print(df.sort_values("HP",ascending=False))# this is decending
#print(df.sort_values(["Type 1","HP"],ascending=[True,False])) # sorting for two conditions 

#creating column
# this is a long way of creating a totals column
# df['Total'] = df['HP'] + df['Attack'] + df['Defense'] + df['Sp. Atk'] + df['Sp. Def'] + df['Speed']

# instead we can do this
#df['Total'] = df.iloc[:,4:10].sum(axis=1)
# creates column called 'total' by adding values in coulumns 6 to 11, axis 1 is adding accross while axis 0 is adding down

# save csv 
#df.to_csv('Modified.csv')
#print(df.loc[df['Total'] == df['Total'].max()])