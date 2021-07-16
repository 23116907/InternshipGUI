from tkinter import *
from tkinter.filedialog import askdirectory
import tksheet



# This creates the main window.
root=Tk()

root.configure(bg = "white")


String_Var = StringVar()

def select_directory():
    String_Var.set(askdirectory())


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


velocities_table_frame = Frame(root)
velocities_table_frame.grid(column=1, row=3, sticky=W, columnspan=1)

positions_table_top_frame = Frame(root)
positions_table_top_frame.grid(column=2, row=3, sticky=W, columnspan=1)

positions_table_labels_frame = Frame(root)
positions_table_labels_frame.grid(column=2, row=4, columnspan=1)

frm_entry=Frame(master=root)

drop_down = OptionMenu(root, clicked, "Port1", "Port2")
connect_button = Button(width=10, height=1, bg = "white", fg= "red", text="Connect")
status_label = Label(width=10, text="Status")
drop_down1 = OptionMenu(root, clicked1, "Port3", "Port4")
connect_button1 = Button(width=10, height=1, bg = "white", fg= "red", text="Connect")
status_label1 = Label(width=10, text="Status")
velocities_label = Label(velocities_table_frame, bg="white", text="Velocities to test")
positions_label = Label(positions_table_top_frame, bg="white", text="Positions to test")
pattern_Label = Label(bg="white", text="Pattern Table")
c = Checkbutton(velocities_table_frame, text="Randomize")
c2 = Checkbutton(positions_table_top_frame, bg="white", text="Randomize")
runtest_button = Button(positions_table_labels_frame, width=10, height=1, bg="white", fg="black", text="Run Test")
status_label2 = Label(positions_table_labels_frame, bg="white", text="Status")
storage_folder_button = Button(width = 60, height =1, command = select_directory, bg="white", text="Storage folder address")


drop_down.grid( sticky=W, column=0, row=0)
connect_button.grid(column=1, row=0, sticky=W)
status_label.grid(column=2, row=0, sticky=W)
drop_down1.grid( sticky=W, column=0, row=1)
connect_button1.grid(column=1, row=1, sticky=W)
status_label1.grid(column=2, row=1, sticky=W)
velocities_label.grid(column=0, row=0)
positions_label.grid(column=0, row=0, sticky=W)
pattern_Label.grid(column=0, row=3, sticky=W)
c.grid(sticky=W, column=1, row=0)
c2.grid(sticky=W, column=1, row=0)
runtest_button.grid(sticky=NE, column=0, row=0)
status_label2.grid(sticky=NE, column=0, row=1)
storage_folder_button.grid(column=0, row=5, sticky = NW)


sheet1.grid(sticky=W, column=0, row=4)
sheet2.grid(column=1, row=4)
sheet3.grid(sticky = W, column=2, row=4)

sheet1.headers(["Time(S)", "Velocity(rev/s)", "torque(NM)"])


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
