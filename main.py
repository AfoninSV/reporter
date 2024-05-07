import tkinter as tk
from datetime import datetime, timedelta
from pathlib import Path
import os

def get_notes() -> list:
    path = f"{Path(__file__).parent.absolute()}.20_notes.txt"
    if os.path.isfile(path):
        with open(path, 'r') as note_file:
            data = note_file.readlines()
            return data
    return list()

def get_time(delta:int) -> str:
    ftime= datetime.now() - timedelta(hours=delta)
    ftime = ftime.strftime('%H:00')
    return ftime

def compile_data(comp_to) -> None:
    data = str()
    
    # !Change to your machine name
    machine_name = "Welding line"

    time_str = f'{get_time(1)}-{get_time(0)} {machine_name}\n'
    nums_list = nums.get(1.0, "end-1c").split()
    data += time_str

    num1 = nums_list[0] if len(nums_list) >= 1 else 0
    num2 = nums_list[1] if len(nums_list) >= 2 else 0
    num3 = nums_list[2] if len(nums_list) >= 3 else 0
    num4 = nums_list[3] if len(nums_list) >= 4 else 0
    
    data +=f'{name1.get(1.0, "end-1c")} - {num1} pcs; {rep1.get(1.0, "end-1c")}\n'
    data +=f'{name2.get(1.0, "end-1c")} - {num2} pcs; {rep2.get(1.0, "end-1c")}\n'
    data +=f'{name3.get(1.0, "end-1c")} - {num3} pcs; {rep3.get(1.0, "end-1c")}\n'
    data +=f'{name4.get(1.0, "end-1c")} - {num4} pcs; {rep4.get(1.0, "end-1c")}\n'
    comp_to.delete('1.0', tk.END)
    comp_to.insert(tk.INSERT, data)

def name_field(root_w, text, x, y):
    field = tk.Text(root_w)
    field.configure(height=2, width=30, padx=5, pady=3)
    field.insert(tk.INSERT, text)
    field.grid(column=x, row=y, sticky='W')
    return field

def err_field(root_w, x, y):
    field = tk.Text(root_w)
    field.configure(height=2, pady= 3, width=215)
    field.grid(column=x, row=y, sticky='W')

    return field

def noter_field(master, x, y, text=None):
    field = tk.Text(master)
    field.configure(width=144, height=1, pady=3)
    field.grid(column=x, row=y)
    if text:
        field.insert(tk.INSERT, text)

# column -> x row -> y

root = tk.Tk()

# Set window size
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry(f"{screen_width - 100}x{screen_height // 2}")

main = tk.Frame(root)
out = tk.Frame(root)
noter = tk.Frame(root)

main.grid(column=0, row=0,columnspan=2, sticky='WN')
noter.grid(column=1, row=2, sticky='WN')
out.grid(column=0, row=2, sticky='WN')

rep_part = tk.Frame(main)
rep_part.grid(column=0, row=1)

name1 = name_field(rep_part, 'Prod. Line #9-1 (prod. type#)', 0, 0)
name2 = name_field(rep_part, 'Prod. Line #9-2 (prod. type#)', 0, 1)
name3 = name_field(rep_part, 'Prod. Line #10-1 (prod. type#)', 0, 2)
name4 = name_field(rep_part, 'Prod. Line #10-2 (prod. type#)', 0, 3)

nums = tk.Text(rep_part)
nums.configure(height=4, width=4, pady=1, font=('Helvetica bold', 21), spacing1=5)
nums.grid(column=1, row=0, rowspan=4)

rep1 = err_field(rep_part, 2, 0)
rep2 = err_field(rep_part, 2, 1)
rep3 = err_field(rep_part, 2, 2)
rep4 = err_field(rep_part, 2, 3)

# noter fields qty

noter_data = get_notes()
noter_range = (len(noter_data) - 1)
for i in range(20):
    if i > noter_range:
        noter_field(noter, 0, i)
    else:
        noter_field(noter, 0, i, text=noter_data[i])

make = tk.Button(rep_part)

make.configure(command=lambda: compile_data(output))
make.grid(column=0, columnspan=3, row=4, sticky='WE')
make['text'] = 'report'

output = tk.Text(out)
output.configure(height=32, width=110, padx=3)
output.grid(column=0, row=5, sticky='W')

if __name__ == "__main__":
    get_notes()
    root.mainloop()
