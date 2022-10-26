import pandas as pd
from pathlib import Path

datapath = Path("data") / "baseball.txt"
print(datapath)
df = pd.read_csv(datapath, sep=",")
print(df)
# subsetting likke a list of lists
print(df["W"][5]) #collum then row
#using loc
print(df.loc[5, "W"]) #row then column
#using iloc
print(df.iloc[5, 1]) #loc and iloc are faster on a computational level

def ratio(row):
    w = row["W"]
    l = row["L"]
    return int(w)/int(l)

df["newcol"] = 0
df["anothercol"] = list(range(len(df)))

df["ratio"] = df.apply(lambda row: ratio(row), axis=1)
idx_max = print(df["ratio"].idxmax) #returns highest id value

print(df.loc[idx_max, "Team"])

outfile = Path("data") / "baseball_edited.csv"

df.to_csv(outfile, index=False) # index_label=idx creates a header for the first colum