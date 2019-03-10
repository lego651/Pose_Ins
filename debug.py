import pandas as pd

filename = "./df_matrix_200.csv"
M = pd.read_csv(filename)

print(M.describe())

print("#################")

print(M.head(100))

print("#################")

print(M.tail(20))