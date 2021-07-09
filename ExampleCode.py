import tkinter as tk

import tksheet

# This creates the main window.
root = tk.Tk()

# You create a table, and you add to "root".
sheet = tksheet.Sheet(root)

# Divide root into a grid, tells where to place sheet in that grid
sheet.grid(column=0, row=0)

# The data for the table must be in a list.
# Here we create the individual rows
row1 = [1, 3, 4]
row2 = [6, 34, 7]
row3 = [4, 7, 8]

# Here we put all rows together
sheetData = [row1, row2, row3]

# Here you input the data to the table
sheet.set_sheet_data(sheetData)



# table enable choices listed below:
sheet.enable_bindings(("single_select",

                       "row_select",

                       "column_width_resize",

                       "arrowkeys",

                       "right_click_popup_menu",

                       "rc_select",

                       "rc_insert_row",

                       "rc_delete_row",

                       "copy",

                       "cut",

                       "paste",

                       "delete",

                       "undo",

                       "edit_cell"))
# Another way of doing this:
# sheet.enable_bindings(bindings='all')

# Create a second table
sheet2 = tksheet.Sheet(root)

# Place the table
sheet2.grid(column=1, row=0)

# Same data as the first table, but multiplied by two.
# sheetData = [row1, row2, row3]
DoubleData = []
for Row in sheetData:
    DoubleRow = []
    for Number in Row:
        Number = Number * 2
        DoubleRow.append(Number)
    DoubleData.append(DoubleRow)

# Here you input the data to the table
sheet2.set_sheet_data(DoubleData)

# Create a third table
sheet3 = tksheet.Sheet(root)

# Place the table
sheet3.grid(column=0, row=1)

# List comprehension
TripleData = [[Number * 3 for Number in Row] for Row in sheetData]

# Here you input the data to the table
sheet3.set_sheet_data(TripleData)

# Create a fourth table
sheet4 = tksheet.Sheet(root)

# Place the table
sheet4.grid(column=0, row=1)

# List comprehension
FourthData = [[Number * 3 for Number in Row] for Row in sheetData]

# Here you input the data to the table
sheet4.set_sheet_data(FourthData)

root.mainloop()