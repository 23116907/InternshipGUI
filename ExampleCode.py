import tkinter as tk

from tkinter import *


import tksheet

# This creates the main window.
root = Tk()


# You create a table, and you add to "root".
sheet1 = tksheet.Sheet(root)
sheet2 = tksheet.Sheet(root)
sheet3 = tksheet.Sheet(root)

# Divide root into a grid, tells where to place sheet in that grid

clicked = StringVar()
clicked.set("COM port list")

clicked1 = StringVar()
clicked1.set("COM port list")

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




#drop_down = tk.Label(text = "COM port list                                                                                                                     ")
drop_down = OptionMenu(root, clicked, "Port1", "Port2")
connect_button = tk.Button(width = 10, height = 1, bg = "white", fg= "red", text = "Connect")
status_label = tk.Label(text = "Status                                                                                                                             ")
drop_down1 = OptionMenu(root, clicked1, "Port3", "Port4")
#drop_down1 = tk.Label(text = "COM port list                                                                                                                     ")
connect_button1 = tk.Button(width = 10, height = 1, bg = "white", fg= "red", text = "Connect")
status_label1 = tk.Label(text = "Status                                                                                                                             ")
velocities_label= tk.Label(text = "Velocities to test                                                                                                             ")
positions_label= tk.Label(text = "Positions to test                                                                                                             ")
pattern_Label = tk.Label(text = "Pattern Table                                                                                                                      ")
c = Checkbutton(text = "Randomize")
c2 = Checkbutton(text = "Randomize")
runtest_button = tk.Button(width = 10, height = 1, bg="white", fg="black", text = "Run Test")
status_label2 = tk.Label(text = "Status")
address_bar = tk.Label(text = "Storage folder address")

drop_down.grid(column = 0, row = 0)
connect_button.grid(column = 1, row = 0)
status_label.grid(column = 2, row = 0)
drop_down1.grid(column = 0, row = 1)
connect_button1.grid(column = 1, row = 1)
status_label1.grid(column = 2, row = 1)
velocities_label.grid(column = 1, row =2)
positions_label.grid(column = 2, row = 2)
pattern_Label.grid(column = 0, row = 3)
c.grid(column = 1, row = 3)
c2.grid(column = 2, row = 3)
runtest_button.grid(column = 2, row=4)
status_label2.grid(column=2, row=5)
address_bar.grid(column=0, row=5)


sheet1.grid(column=0, row=4)
sheet2.grid(column = 1, row = 4)
sheet3.grid(column = 2, row = 4)


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
sheet2.enable_bindings(("single_select",

                       "row_select",

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
sheet3.enable_bindings(("single_select",

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

root.mainloop()