import sys

import pandas as pd

import os

print("Running file:", os.path.abspath(__file__))

print('argument', sys.argv)

month = int(sys.argv[1])


df = pd.DataFrame({"day" : [1,2], "no_of_passengers":[3,4]})
df['month'] = month

df.to_parquet(f"output :{month}.parquet")

print(df)


print(f'hello pipeline , month = {month}')
