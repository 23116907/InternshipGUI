import tkinter as tk

import tksheet

# This creates the main window.
root = tk.Tk()


# You create a table, and you add to "root".
sheet1 = tksheet.Sheet(root)
sheet2 = tksheet.Sheet(root)
sheet3 = tksheet.Sheet(root)

# Divide root into a grid, tells where to place sheet in that grid


import random
n = random.randint(1, 5)
m = random.randint(1, 5)
l = random.randint(1, 5)
j = round(random.uniform(-1.00, 1.00), 2)

# The data for the table must be in a list.
# Here we create the individual rows

row1 = [n, j, 0.5]
row2 = [m, j, 0.5]
row3 = [l, j, 0.5]

cow1 = [1]
cow2 = [2]
cow3 = [3]
cow4 = [4]

# Here we put all rows together
sheet1Data = [row1, row2, row3]
sheet2data = [cow1, cow2, cow3, cow4]
sheet3data = [cow1, cow2, cow3, cow4]

# Here you input the data to the table
sheet1.set_sheet_data(sheet1Data)
sheet2.set_sheet_data(sheet2data)
sheet3.set_sheet_data(sheet3data)

rame1 = tk.Frame(master=root)
rame2 = tk.Frame(master=root)
rame3 = tk.Frame(master = root)
fram1 = tk.Frame(master = root)
fram2 = tk.Frame(master = root)
frame1 = tk.Frame(master=root)
frame2 = tk.Frame(master=root)
frame3 = tk.Frame(master = root)
frame4 = tk.Frame(master = root)
frame5 = tk.Frame(master = root)
frame6 = tk.Frame(master = root)
lab1 = tk.Label(master = rame1, text = "COM port list")
lab2 = tk.Label(master = rame2, text = "Connect")
lab3 = tk.Label(master = rame3, text = "Status")
labe1= tk.Label(master = fram1, text = "Velocities to test")
labe2= tk.Label(master = fram2, text = "Positions to test")
label = tk.Label(master=frame1, text = "Pattern Table")
label2 = tk.Label(master=frame2, text = "randomize")
label3 = tk.Label(master=frame3, text = "randomize")
label4 = tk.Label(master = frame4, text = "Run Test")
label5 = tk.Label(master = frame5, text = "Status")
label6 = tk.Label(master=frame6, text = "Storage folder address")
lab1.grid(column = 0, row = 0)
lab2.grid(column = 1, row = 0)
lab3.grid(column = 2, row = 0)
labe1.grid(column = 1, row =1)
labe2.grid(column = 2, row = 2)
label.grid(column = 0, row = 2)
label2.grid(column = 1, row = 2)
label3.grid(column = 2, row = 2)
label4.grid(column = 2, row=3)
label5.grid(column=2, row=4)
label6.grid(column=0, row=4)

rame1.grid(column = 0, row = 0)
rame2.grid(column = 1, row = 0)
rame3.grid(column = 2, row = 0)
fram1.grid(column = 1, row = 1)
fram2.grid(column = 2, row = 1)
frame1.grid(column = 0, row = 2)
frame2.grid(column = 1, row = 2)
frame3.grid(column = 2, row = 2)
frame4.grid(column=2, row=3)
frame5.grid(column=2, row=4)
frame6.grid(column = 0, row=4)
sheet1.grid(column=0, row=3)
sheet2.grid(column = 1, row = 3)
sheet3.grid(column = 2, row = 3)


# table enable choices listed below:
sheet1.enable_bindings(("single_select",

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
# sheet2 = tksheet.Sheet(root)

# Place the table
#sheet2.grid(column=1, row=0)

# Same data as the first table, but multiplied by two.
# sheetData = [row1, row2, row3]
#DoubleData = []
#for Row in sheetData:
    #DoubleRow = []
    #for Number in Row:
        #Number = Number * 2
        #DoubleRow.append(Number)
    #DoubleData.append(DoubleRow)

# Here you input the data to the table
#sheet2.set_sheet_data(DoubleData)

# Create a third table
#sheet3 = tksheet.Sheet(root)

# Place the table
#sheet3.grid(column=0, row=1)

# List comprehension
#TripleData = [[Number * 3 for Number in Row] for Row in sheetData]

# Here you input the data to the table
#sheet3.set_sheet_data(TripleData)

# Create a fourth table
#sheet4 = tksheet.Sheet(root)

# Place the table
#sheet4.grid(column=0, row=1)

# List comprehension
#FourthData = [[Number * 3 for Number in Row] for Row in sheetData]

# Here you input the data to the table
#sheet4.set_sheet_data(FourthData)

root.mainloop()