from san_utils.paths import outputs_dir
import pandas as pd
import numpy as np
import openpyxl

df = pd.DataFrame()
df["color_range"] = pd.RangeIndex(1, 24, 1)
df["pct"] = np.random.random(23)

# df.style.format(na_rep="MISS", precision=3)
highest_danger_style = "RdYlGn_r"
highest_safe_style = "RdYlGn"
# highest_danger_style = "PiYG_r"
# Calculate the maximum length of column names
max_col_name_len = max([len(col) for col in df.columns])

# Calculate the width for each column
column_widths = {col: len(col) * 8 for col in df.columns}
styled_df = (
    df.style.format(  # .set_properties(**{"width": column_widths}, subset=pd.IndexSlice[:, :])
        {"pct": "{:.2f}%"}
    )
    .background_gradient(
        subset=["pct"],
        cmap=highest_danger_style,
    )
    .map(lambda x: f"color: green" if x > 10 else "color: red", subset=["color_range"])
)

styled_df = styled_df.set_table_styles(
    [
        {
            "selector": "thead th",
            "props": [("background-color", "lightblue"), ("color", "black")],
        },
        {"selector": "", "props": [("font-size", "12pt")]},
    ]
)

# # Set column width
# styled_df = styled_df.


# styled_df = styled_df.set_properties(**{"width": "100px"}, subset=pd.IndexSlice[:, :])

# column changing
# styled_df.data["pct"]

styled_df.to_excel(outputs_dir / "test1.xlsx")
styled_df


import pandas as pd
import openpyxl

# Sample DataFrame
data = {"A": [1, 2, 3, 4], "B": [0.5, 0.7, 0.3, 0.9]}
df = pd.DataFrame(data)


# Define a function to apply styling
def color_negative_red(val):
    color = "FF0000" if val < 0 else "000000"
    # return f'=TEXT("{val}", "")&CHAR(10)&CHAR(10)&REPT(" ", 20)&CHAR(10)&CHAR(10)&REPT(" ", 20)&CHAR(10)&CHAR(10)&REPT(" ", 20)&CHAR(10)&CHAR(10)&REPT(" ", 20)&CHAR(10)&CHAR(10)&REPT(" ", 20)&CHAR(10)&CHAR(10)&REPT(" ", 20)&CHAR(10)&CHAR(10)&REPT(" ", 20)&CHAR(10)&CHAR(10)&REPT(" ", 20)&CHAR(10)&CHAR(10)&REPT(" ", 20)&CHAR(10)&CHAR(10)&REPT(" ", 20)&CHAR(10)&CHAR(10)&REPT(" ", 20)&CHAR(10)&CHAR(10)&REPT(" ", 20)&CHAR(10)&CHAR(10)&REPT(" ", 20)&CHAR(10)&CHAR(10)&REPT(" ", 20)&CHAR(10)&CHAR(10)&REPT(" ", 20)&CHAR(10)&CHAR(10)&REPT(" ", 20)&CHAR(10)&CHAR(10)&REPT(" ", 20)&CHAR(10)&CHAR(10)&REPT(" ", 20)&CHAR(10)&CHAR(10)&REPT(" ", 20)&CHAR(10)&CHAR(10)&REPT(" ", 20)&CHAR(10)&CHAR(10)&REPT(" ", 20)&CHAR(10)&CHAR(10)&REPT(" ", 20)&CHAR(10)&CHAR(10)&REPT(" ", 20)&CHAR(10)&CHAR(10)&REPT(" ", 20)&CHAR(10)&CHAR(10)&REPT(" ", 20)&CHAR(10)&CHAR(10)&REPT(" ", 20)&CHAR(10)&CHAR(10)&REPT(" ", 20)&CHAR(10)&CHAR(10)&REPT(" ", 20)&CHAR(10)&CHAR(10)&REPT(" ", 20)&CHAR(10)&CHAR(10)&REPT(" ", 20)&CHAR(10)&CHAR(10)&REPT(" ", 20)&CHAR(10)&CHAR(10)&REPT(" ", 20)&CHAR(10)&CHAR(10)&REPT(" ", 20)&CHAR(10)&CHAR(10)&REPT(" ", 20)&CHAR(10)&CHAR(10)&REPT(" ", 20)&CHAR(10)&CHAR(10)&REPT(" ", 20)&CHAR(10)&CHAR(10)&REPT(" ", 20)&CHAR(10)&CHAR(10)&REPT(" ", 20)&CHAR(10)&CHAR(10)&REPT(" ", 20)&CHAR(10)&CHAR(10)&REPT(" ", 20)&CHAR(10)&CHAR(10)&REPT(" ", 20)&CHAR(10)&CHAR(10)&REPT(" ", 20)&CHAR(10)&CHAR(10)&REPT(" ", 20)&CHAR(10)&CHAR(10)&REPT(" ", 20)&CHAR(10)&CHAR(10)&REPT(" ", 20)&CHAR(10)&CHAR(10)&REPT(" ", 20)&CHAR(10)&CHAR(10)&REPT(" ", 20)&CHAR(10)&CHAR(10)&REPT(" ", 20)&CHAR(10)&CHAR(10)&REPT(" ", 20)&CHAR(10)&CHAR(10)&REPT(" ", 20)&CHAR(10)&CHAR(10)&REPT(" ", 20)&CHAR(10)&CHAR(10)&REPT(" ", 20)&CHAR(10)&CHAR(10)&REPT(" ", 20)&CHAR(10)&CHAR(10)&REPT(" ", 20)&CHAR(10)&CHAR(10)&REPT(" ", 20)&CHAR(10)&CHAR(10)&REPT(" ", 20)&CHAR(10)&CHAR(10)&REPT(" ", 20)&CHAR(10)&CHAR(10)&REPT(" ", 20)&CHAR(10)&CHAR(10)&REPT(" ", 20)&CHAR(10)&CHAR(10)&REPT(" ", 20)&CHAR(10)&CHAR(10)&REPT(" ", 20)&CHAR(10)&CHAR(10)&REPT(" ", 20)&CHAR(10)&CHAR(10)&REPT(" ", 20)&CHAR(10)&CHAR(10)&REPT(" ", 20)&CHAR(10)&CHAR(10)&REPT(" ", 20)&CHAR(10)&CHAR(10)&REPT(" ", 20)&CHAR(10)&CHAR(10)&REPT(" ", 20)&CHAR(10)&CHAR(10)&REPT(" ", 20)&CHAR(10)&CHAR(10)&REPT(" ", 20)&CHAR(10)&CHAR(10)&REPT(" ", 20)&CHAR(10)&CHAR(10"


# Apply styling to the DataFrame
# df_styled = df.applymap(color_negative_red)
