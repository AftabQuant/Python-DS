# import pandas as pd

# data = pd.read_excel("D:/Ultimate Programming/Business Analytics/Ms Excel/heart_attack_dataset.xlsx")
# print(data)

import pandas as pd

# Specify the path to the Excel file, including the file extension
file_path = "D:/Ultimate Programming/Business Analytics/Ms Excel/heart_attack_dataset.xlsx"

# Read the Excel file into a DataFrame
data = pd.read_excel(file_path)

# Display the first few rows of the DataFrame
print(data.head())
