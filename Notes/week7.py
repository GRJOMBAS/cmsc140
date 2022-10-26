import pandas as pd
from pathlib import Path

datapath = Path("data") / "baseball.txt"
print(datapath)
df = pd.read_csv(datapath, sep=",")
print(df)
# subsetting likke a list of lists
print(df["W"][5]) #collum then row
#using loc
print(df.loc[5, "W"]) #row then collum
#using iloc
print(df.iloc[5, 1])