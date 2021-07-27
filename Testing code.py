from tkinter import *
from tkinter.filedialog import askdirectory
import tksheet
import random
from random import shuffle
import time


# This creates the main window.
root=Tk()

root.configure(bg = "white")


directory_name_str = StringVar()


runtest_status_label_str = StringVar()

COM_port_data = StringVar()

status_label1 = StringVar()

checkbutton_status = StringVar()

def select_directory():
    directory_name_str.set(askdirectory())

def click_velocity_checkbutton():
    checkbutton_status.set(askdirectory())

randomize_velocity_checkbutton_bool = BooleanVar(value=False)
randomize_position_checkbutton_bool = BooleanVar(value=False)


# You create a table, and you add to "root".
pattern_table = tksheet.Sheet(root)
velocities_table = tksheet.Sheet(root)
positions_table = tksheet.Sheet(root)


def send_velocity_to_MCU(velocity):
    print("Velocity sent to the MCU:")
    print(velocity)

def send_torque_to_MCU(torque):
    print("Torque sent to the MCU:")
    print(torque)

def send_command_to_start_running_MCU():
    print ("Start running MCU")


def get_number_of_rows(table_data):
    return len(table_data)


def is_table_empty(table):
    table_data = table.get_sheet_data(return_copy=True, get_header=False, get_index=False)
    if not table_data:
        return TRUE
    else:
         for row in table_data:
             for cell in row:
                 if cell:
                     print(row)
                     return FALSE
    #        if row[0]:
     #           print(row)
      #          return FALSE
       #     if row[1]:
        #        print(row)
         #       print('Please add times')
          #      return FALSE
          #  if row[2]:
           #     print(row)
            #    print('Please add velocities')
             #   return FALSE
    return TRUE

def no_COM_port(COM_port):
    COM_port_data = COM_port.get
    if COM_port_data !="COM port list":
        return TRUE
    else:
        return FALSE

def COM_port_inspect():
    if not no_COM_port(velocities_com_port):
        status_label1.set('Ready to run')
    else:
        status_label1.set('No port')






def run_test_callback():
    if not directory_name_str.get():
        runtest_status_label_str.set("Error: Empty directory address.")
        return
    else:
        runtest_status_label_str.set("Successful")
    pattern_table_data = pattern_table.get_sheet_data(return_copy = True, get_header = False, get_index = False)
    if is_table_empty(pattern_table):
        runtest_status_label_str.set("Error: Please enter pattern data.")
        return
    velocities_table_data = velocities_table.get_sheet_data(return_copy=True, get_header = False, get_index = False)


    #if not randomize_velocity_checkbutton_bool.get() and not randomize_velocity_checkbutton_bool.get():
       #print("Velocity table and Position table are empty")
    if is_table_empty(velocities_table) and is_table_empty(positions_table):
        for row in pattern_table_data:
            send_velocity_to_MCU(row[1])
            send_torque_to_MCU(row[2])
            send_command_to_start_running_MCU()
            time.sleep(row[0])
        #send_command_to_stop_running_MCU()
    elif not is_table_empty(velocities_table) and is_table_empty(positions_table):
        print("Hello")
    elif not is_table_empty(positions_table) and is_table_empty(velocities_table):
        print()
    else:
        print()


def click_velocity_checkbutton():
    if checkbutton_status.get:
        shuffle(velocities_tabledata)
    else:
        return


# Divide root into a grid, tells where to place sheet in that grid

velocities_com_port = StringVar()
velocities_com_port.set("COM port list")

positions_com_port = StringVar()
positions_com_port.set("COM port list")

n = random.randint(1, 5)
m = random.randint(1, 5)
l = random.randint(1, 5)
j = '1'
k = random.randint(1, 5)

# The data for the table must be in a list.
# Here we create the individual rows

row1 = [n, j, 0.5]
row2 = [m, 'VELOCITY', 0.5]
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
pattern_tableData = [row1, row2, row3]
velocities_tabledata = [cow1, cow2, cow3, cow4]
positions_tabledata = [dow1, dow2, dow3, dow4]

shuffle(positions_tabledata)

# Here you input the data to the table
pattern_table.set_sheet_data(pattern_tableData)
velocities_table.set_sheet_data(velocities_tabledata)
positions_table.set_sheet_data(positions_tabledata)


velocities_table_frame = Frame(root)
velocities_table_frame.grid(column=1, row=3, sticky=W, columnspan=1)

positions_table_top_frame = Frame(root)
positions_table_top_frame.grid(column=2, row=3, sticky=W, columnspan=1)

positions_table_labels_frame = Frame(root)
positions_table_labels_frame.grid(column=2, row=4, columnspan=1)

frm_entry=Frame(master=root)

drop_down = OptionMenu(root, velocities_com_port, "Port1", "Port2")
connect_button = Button(width=10, height=1, bg = "white", fg= "black", text="Connect", command=COM_port_inspect)
status_label = Label(width=10, text="Status", bg="white")
drop_down1 = OptionMenu(root, positions_com_port, "Port3", "Port4")
connect_button1 = Button(width=10, height=1, bg = "white", fg= "black", text="Connect")
status_label1 = Label(width=10, text="Status", bg="white")
velocities_label = Label(velocities_table_frame, bg="white", text="Velocities to test")
positions_label = Label(positions_table_top_frame, bg="white", text="Positions to test")
pattern_Label = Label(bg="white", text="Pattern Table")
Velocity_Checkbutton = Checkbutton(velocities_table_frame, bg="white", text="Randomize", command = click_velocity_checkbutton, variable=randomize_velocity_checkbutton_bool)
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
runtest_status_label.grid(sticky=NE, column=1, row=1)
status_label2.grid(sticky=NE, column=0, row=1)
storage_folder_button.grid(column=2, row=5, sticky = NW)
storage_folder_label.grid(column=0, row=5, columnspan=2, sticky = NW)



pattern_table.grid(sticky=W, column=0, row=4)
velocities_table.grid(column=1, row=4)
positions_table.grid(sticky = W, column=2, row=4)

pattern_table.headers(["Time(S)", "Velocity(rev/s)", "torque(NM)"])


# table enable choices listed below:
pattern_table.enable_bindings(("single_select",
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

velocities_table.enable_bindings(("single_select",
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

positions_table.enable_bindings(("single_select",
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
