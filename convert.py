import pandas as pd

df = pd.read_excel("entrada.xlsx")
df.to_csv("saida.csv", sep=";", index =False)