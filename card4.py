import pandas as pd
import numpy as np

# загрузка файла
excel_data = pd.read_excel('cardsell.xlsx')
# Чтение файла в фрейме
data = pd.DataFrame(excel_data, columns=['Тариф', 'Выдача', 'Активация', 'ФИО'])
# Вывод результата
print (data.groupby(['ФИО', 'Тариф']).count())
#печатаю вывод в файл
with open('outcard.txt', 'w') as f:
    dfAsString = data.to_string(header=True, index=False)
    f.write(dfAsString)