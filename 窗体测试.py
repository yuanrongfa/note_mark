import tkinter as tk

from tkinter import filedialog

def choose_file():
    # label.config(text='已改变...')
    file_path = filedialog.askopenfilename()

    label.config(text=file_path)

root=tk.Tk()

root.title("半自动身份证号15位转18位")

root.geometry('500x250')

label = tk.Label(root,text='请选择需要转换的文件(xlsx)')

label.place(x=10,y=50)

button1 = tk.Button(root,text='请选择文件',command=choose_file)

button1.place(x=10,y=80)

# 请选择表格的列字母
label2 = tk.Label(root,text='请输入身份证所在的列字母，如在A列，输入:a')

label2.place(x=10,y=120)

# entry = tk.Entry(root)

# entry.insert(0,'请输入身份证所在的列字母，如在A列，输入:a')

# entry.place(x=10,y=120)

root.mainloop()

