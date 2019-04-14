import pandas as pd

excel_file = "data\\big.xls"
data = pd.read_excel(excel_file)

print('Hello')
print(data.head)
print(data.shape)
