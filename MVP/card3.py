import pandas as pd
import numpy as np

excel_data = pd.read_excel('cardsell.xlsx')
data = pd.DataFrame(excel_data, columns=['Тариф', 'Выдача', 'Активация', 'ФИО'])
result = [f'{row[3]}: {row[0]} - {row[1] + row[2]} ' for row in data.values]

print(result)

#я только столбцы указал

#а по строкам он сам проходится в цикле

for i, row in data.iterrows():
	print(f"Index: {i}")
	print(f"{row}\n")

#
for row in data.itertuples():
    print(row)

#
import pandas as pd

# Load the xlsx file
excel_data = pd.read_excel('cardsell.xlsx')
# Read the values of the file in the dataframe
data = pd.DataFrame(excel_data, columns=['Тариф', 'Выдача', 'ФИО'])
# Print the content
print("The content of the file is:\n", data)
print(data.groupby(['ФИО', 'Тариф']).count())

#
pd.pivot_table(data, index=["ФИО"], values=["Выдача"], columns=["Тариф"], aggfunc=[np.sum])
