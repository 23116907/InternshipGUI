import tkinter as tk
import tksheet
import random

n = round(random.uniform(1.00, 6.00), 2)
m = random.randint(1, 9)
top = tk.Tk()
top_left_fg = tk.Tk()
top_right_bg = tk.Tk()
sheet1 = tksheet.Sheet(top)
sheet2 = tksheet.Sheet(top_left_fg)
sheet3 = tksheet.Sheet(top_left_fg)
sheet4 = tksheet.Sheet(top_right_bg)
sheet5 = tksheet.Sheet(top_right_bg)

sheet1.grid(column=0, row=0)
sheet2.grid()
sheet3.grid()
sheet4.grid()
sheet5.grid()

sheet1.set_sheet_data([[f"{ri*cj*n}" for cj in range(3)] for ri in range(5)], round(2))
sheet2.set_sheet_data([[f"{ri+cj}" for cj in range(1)] for ri in range(4)])
sheet3.set_sheet_data([[f"{m+n}" for cj in range(1)] for ri in range(4)])
sheet4.set_sheet_data([[f"{n}" for cj in range(1)] for ri in range(1)])
sheet5.set_sheet_data([[f"{m+cj+ri}" for cj in range(2)] for ri in range(2)])

# table enable choices listed below:

top.mainloop()
