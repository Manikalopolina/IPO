import pandas as pd # Импортируем библиотеку pandas
# Создаём словарь с данными о процессорах
d = {'Модель': pd.Series(['Intel Core i9-9900K', 'AMD Ryzen 7 3700X', 'ARM Cortex-A53', 'Intel Core i7-10700K',
                          'AMD Ryzen 9 3900X', 'Apple M1', 'Qualcomm Snapdragon 865', 'AMD EPYC 7742', 'Intel Xeon E-2286M', 'NVIDIA Tegra X1']),
     'Форма-фактор': pd.Series(['LGA 1151', 'AM4', 'LGA 1151', 'LGA 1200', 'AM4', 'AM4', 'LGA 1200', 'SP3', 'BGA1440',
                                'SP3']),
     'Частота': pd.Series(['3.6 ГГц','3.6 ГГц', '3.8 ГГц', '3.8 ГГц', 'Н/Д', '2.84 ГГц', '2.25 ГГц', '2.4 ГГц',
                           '1 ГГц-1.2 ГГц', '2.2 ГГц'])}
# Создаём табличную структуру данных
s = pd.DataFrame(d)
print(s)

s.to_csv('CPU.csv') # Экспортируем данные в csv файл
CPU_df = pd.read_csv('CPU.csv') # Читаем данные из csv файла

print(CPU_df.groupby(['Частота', 'Форма-фактор'])['Модель'].count()) # Выполняем выборку