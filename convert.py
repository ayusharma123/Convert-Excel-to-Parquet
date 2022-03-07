import pandas as pd

sheet_df = []
read_path = r"C:/Users/ash159/Downloads/Ops Reporting Materials Sample data SP23.xlsx"
write_path = r""

excel = pd.ExcelFile(read_path)
sheets = excel.sheet_names

print("Beginning the conversion !!!")

for i in range(len(sheets)):
    print("################################")
    print("Converting sheet - {}".format(sheets[i]))
    pd.read_excel(excel, i).astype(str).to_parquet("{}{}.parquet".format(write_path, sheets[i]))
    print("################################")

print("Action Completed")