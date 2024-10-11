import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as mbox


win = tk.Tk()
win.title("Nguyễn Đức Trung")


tabControl = ttk.Notebook(win)


tab1 = ttk.Frame(tabControl)  
tab2 = ttk.Frame(tabControl)  

tabControl.add(tab1, text='Giải Phương Trình Bậc Nhất')
tabControl.add(tab2, text='Chuyển Đổi Đơn Vị')
tabControl.pack(expand=1, fill='both')  # Pack để hiển thị


main_label = ttk.Label(tab1, text="ax + b = 0")
main_label.grid(column=0, row=0, padx=10, pady=3)

a_label = ttk.Label(tab1, text="a:")
a_label.grid(column=0, row=1)
a = tk.IntVar()
a_entered = ttk.Entry(tab1, width=12, textvariable=a)
a_entered.grid(column=1, row=1, padx=3)

b_label = ttk.Label(tab1, text="b:")
b_label.grid(column=0, row=2)
b = tk.IntVar()
b_entered = ttk.Entry(tab1, width=12, textvariable=b)
b_entered.grid(column=1, row=2)

c = tk.DoubleVar()
c.set(0)

result_label = ttk.Label(tab1, text="Kết quả:")
result_label.grid(column=0, row=3)
result_display = ttk.Entry(tab1, width=12, textvariable=c, state="readonly")
result_display.grid(column=1, row=3)


def click_me():
    try:
        if a.get() != 0:
            c.set(-b.get() / a.get())
        else:
            mbox.showerror("Error", "a phải khác 0")
    except tk.TclError:
        mbox.showerror("Input Error", "Nhập số vào a và b")
    except Exception as e:
        mbox.showerror("Something wrong", str(e))


action = ttk.Button(tab1, text="Giải", command=click_me)
action.grid(column=0, row=4, columnspan=2, pady=3)


title_label = ttk.Label(tab2, text="Chuyển đổi giữa Liters, Milliliters và Gallons")
title_label.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

entry_label = ttk.Label(tab2, text="Từ:")
entry_label.grid(row=1, column=0)

entry = tk.Entry(tab2, width=10)
entry.grid(row=1, column=1)

from_combo = ttk.Combobox(tab2, width=15, state='readonly')
from_combo['value'] = ('Liters (L)', 'Milliliters (mL)', 'Gallons (gal)')
from_combo.current(0)
from_combo.grid(row=1, column=2)

to_label = ttk.Label(tab2, text="Đến:")
to_label.grid(row=2, column=0)

re = tk.DoubleVar()
entry_to = tk.Entry(tab2, width=10, state="readonly", textvariable=re)
entry_to.grid(row=2, column=1)

to_combo = ttk.Combobox(tab2, width=15, state='readonly')
to_combo['value'] = ('Liters (L)', 'Milliliters (mL)', 'Gallons (gal)')
to_combo.current(0)
to_combo.grid(row=2, column=2)


def liters_to_milliliters(value):
    return value * 1000

def liters_to_gallons(value):
    return value * 0.264172

def milliliters_to_liters(value):
    return value / 1000

def milliliters_to_gallons(value):
    return value * 0.000264172

def gallons_to_liters(value):
    return value * 3.78541

def gallons_to_milliliters(value):
    return value * 3785.41

def convert():
    try:
        input_value = float(entry.get())
        from_unit = from_combo.get()
        to_unit = to_combo.get()
        
        
        if from_unit == 'Liters (L)':
            if to_unit == 'Milliliters (mL)':
                result = liters_to_milliliters(input_value)
            elif to_unit == 'Gallons (gal)':
                result = liters_to_gallons(input_value)
            else:
                result = input_value  

        elif from_unit == 'Milliliters (mL)':
            if to_unit == 'Liters (L)':
                result = milliliters_to_liters(input_value)
            elif to_unit == 'Gallons (gal)':
                result = milliliters_to_gallons(input_value)
            else:
                result = input_value  

        elif from_unit == 'Gallons (gal)':
            if to_unit == 'Liters (L)':
                result = gallons_to_liters(input_value)
            elif to_unit == 'Milliliters (mL)':
                result = gallons_to_milliliters(input_value)
            else:
                result = input_value  

        
        re.set(format(result, '.10f').rstrip('0').rstrip('.'))
    except tk.TclError:
        mbox.showerror("Input Error", "Nhập số hợp lệ vào ô nhập liệu")
    except ValueError:
        mbox.showerror("Lỗi nhập liệu", "Nhập số hợp lệ")
    except Exception as e:
        mbox.showerror("Something wrong", str(e))


convert_button = tk.Button(tab2, text="Chuyển đổi", command=convert)
convert_button.grid(row=4, column=0, columnspan=3, pady=10)


win.mainloop()

