import pandas as pd
import numpy as np

df = pd.read_excel('cardsell.xlsx')
df.head()

df["Выдача"] = df["Выдача"].astype("category")
df["Выдача"] = df["Выдача"].cat.set_categories(["Базовый", "Премиальный"])

pd.pivot_table(df,index=['ФИО', 'Тариф'], values=['Выдача'], aggfunc=np.sum)
print(df)


