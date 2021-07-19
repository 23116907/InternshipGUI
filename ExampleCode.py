from tkinter import *
from tkinter.filedialog import askdirectory
import tksheet
import random


# This creates the main window.
root=Tk()

root.configure(bg = "white")


directory_name_str = StringVar()


runtest_status_label_str = StringVar()

def select_directory():
    directory_name_str.set(askdirectory())

randomize_velocity_checkbutton_bool = BooleanVar(value=False)
randomize_position_checkbutton_bool = BooleanVar(value=False)


# You create a table, and you add to "root".
sheet1 = tksheet.Sheet(root)
sheet2 = tksheet.Sheet(root)
sheet3 = tksheet.Sheet(root)


def run_test_callback():
    if not directory_name_str.get():
        runtest_status_label_str.set("Error: Empty directory address.")
        return
    else:
        runtest_status_label_str.set("")
    sheet1_data = sheet1.get_sheet_data(return_copy = True, get_header = False, get_index = False)
    if not sheet1_data:
        runtest_status_label_str.set("Error: Please enter pattern data.")
        return

    if not randomize_velocity_checkbutton_bool.get() and not randomize_velocity_checkbutton_bool.get():
        print("Velocity table and Position table are empty")



# Divide root into a grid, tells where to place sheet in that grid

velocities_com_port = StringVar()
velocities_com_port.set("COM port list")

positions_com_port = StringVar()
positions_com_port.set("COM port list")

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

dow1 = [1]
dow2 = [2]
dow3 = [3]
dow4 = [4]

# Here we put all rows together
sheet1Data = [row1, row2, row3]
sheet2data = [cow1, cow2, cow3, cow4]
sheet3data = [dow1, dow2, dow3, dow4]

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

drop_down = OptionMenu(root, velocities_com_port, "Port1", "Port2")
connect_button = Button(width=10, height=1, bg = "white", fg= "black", text="Connect")
status_label = Label(width=10, text="Status", bg="white")
drop_down1 = OptionMenu(root, positions_com_port, "Port3", "Port4")
connect_button1 = Button(width=10, height=1, bg = "white", fg= "black", text="Connect")
status_label1 = Label(width=10, text="Status", bg="white")
velocities_label = Label(velocities_table_frame, bg="white", text="Velocities to test")
positions_label = Label(positions_table_top_frame, bg="white", text="Positions to test")
pattern_Label = Label(bg="white", text="Pattern Table")
Velocity_Checkbutton = Checkbutton(velocities_table_frame, bg="white", text="Randomize",variable=randomize_velocity_checkbutton_bool)
Position_Checkbutton = Checkbutton(positions_table_top_frame, bg="white", text="Randomize",variable=randomize_position_checkbutton_bool)

runtest_button = Button(positions_table_labels_frame, width=10, height=1, bg="white", fg="black", text="Run Test", command=run_test_callback)
runtest_status_label = Label(positions_table_labels_frame, bg="white", textvariable=runtest_status_label_str)
status_label2 = Label(positions_table_labels_frame, bg="white", text="Status")
storage_folder_button = Button(width = 60, height =1, command = select_directory, bg="white", text="Storage folder address")
storage_folder_label = Label(root, bg="white", textvariable=directory_name_str)


drop_down.grid( sticky=W, column=0, row=0)
connect_button.grid(column=1, row=0, sticky=W)
status_label.grid(column=2, row=0, sticky=W)
drop_down1.grid( sticky=W, column=0, row=1)
connect_button1.grid(column=1, row=1, sticky=W)
status_label1.grid(column=2, row=1, sticky=W)
velocities_label.grid(column=0, row=0)
positions_label.grid(column=0, row=0, sticky=W)
pattern_Label.grid(column=0, row=3, sticky=W)
Velocity_Checkbutton.grid(sticky=W, column=1, row=0)
Position_Checkbutton.grid(sticky=W, column=1, row=0)
runtest_button.grid(sticky=NE, column=0, row=0)
runtest_status_label.grid(sticky=NE, column=0, row=1)
status_label2.grid(sticky=NE, column=0, row=1)
storage_folder_button.grid(column=2, row=5, sticky = NW)
storage_folder_label.grid(column=0, row=5, columnspan=2, sticky = NW)



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
