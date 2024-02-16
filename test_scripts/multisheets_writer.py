from pathlib import Path
import pandas as pd
from san_utils.paths import outputs_dir
from san_utils.excel import NewExcelFile


excel_file = NewExcelFile()
# Create sample data frames
df1 = pd.DataFrame({"Fruits": ["Apple", "Banana"], "Quantity": [10, 20]})
df2 = pd.DataFrame({"Vegetables": ["Carrot", "Spinach"], "Quantity": [15, 25]})
excel_file.add_sheet("universe", df1)
excel_file["fc"] = df2

excel_file.save(outputs_dir / "santo.xlsx")


import pandas as pd

# Create some sample DataFrames
df1 = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})
df2 = pd.DataFrame({"X": ["a", "b", "c"], "Y": ["d", "e", "f"]})

# Create a Pandas Excel writer using OpenPyXL as the engine
writer = pd.ExcelWriter(outputs_dir / "multiple_sheets222.xlsx", engine="openpyxl")

# Write each DataFrame to a separate sheet
df1.to_excel(writer, sheet_name="Sheet1", index=False)
df2.to_excel(writer, sheet_name="Sheet2", index=False)

# Close the Pandas Excel writer
writer.close()


# # Example usage:
# if __name__ == "__main__":
#     # Create an instance of ExcelSheetWriter
#     excel_writer = ExcelSheetWriter()

#     # Create sample data frames
#     df1 = pd.DataFrame({"Fruits": ["Apple", "Banana"], "Quantity": [10, 20]})
#     df2 = pd.DataFrame({"Vegetables": ["Carrot", "Spinach"], "Quantity": [15, 25]})

#     # Write data frames to different sheets
#     excel_writer.write_dataframe(df1, sheet_name="Fruits")
#     excel_writer.write_dataframe(df2, sheet_name="Vegetables")

#     # Save the Excel file to a specific path (without index)
#     excel_writer.save("path_to_file/filename.xlsx", index=False)
