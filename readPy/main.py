import pandas as pd

excel_file = 'data\small.xls'
data = pd.read_excel(excel_file)

print('Hello')
print(data.head)
print(data.shape)

