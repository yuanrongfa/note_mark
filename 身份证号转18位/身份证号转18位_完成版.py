import tkinter as tk

from tkinter import filedialog

import openpyxl

import re

import datetime

import os

import tempfile

import base64

# 这个是最后才加进去的。
import sys

wi = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2, 1, ]
vi = [1, 0, 'X', 9, 8, 7, 6, 5, 4, 3, 2, ]


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

def get_image(file):
    with open(resource_path(file), "rb") as f:
        return f.read()

def write_temp_file(img_data, extension):
    fd, path = tempfile.mkstemp(extension)
    with os.fdopen(fd, "wb") as f:
        f.write(img_data)
    return path




def get_verity(eighteen_card):
    """

    :param eighteen_card:
    :return:
    """
    ai = []
    remaining = ''
    if len(eighteen_card) == 18:
        eighteen_card = eighteen_card[0:-1]
    if len(eighteen_card) == 17:
        s = 0
        for i in eighteen_card:
            ai.append(int(i))
        for i in range(17):
            s = s + wi[i] * ai[i]
        remaining = s % 11
    return 'X' if remaining == 2 else str(vi[remaining])


def up_to_eighteen(fifteen_card):
    """
    15λת18λ
    :param fifteen_card:
    :return:
    """
    eighteen_card = fifteen_card[0:6] + '19' + fifteen_card[6:15]
    return eighteen_card + get_verity(eighteen_card)


# 检查15位字符是否为身份证号码，主要是通过生日来检查
def validate_15_id_number(id_number):
    if len(id_number) != 15:
        return False
    if not re.match(r'^\d{15}$', id_number):
        return False
    year = int(id_number[6:8])
    month = int(id_number[8:10])
    day = int(id_number[10:12])
    if year < 0 or year > 99:
        return False
    if month < 1 or month > 12:
        return False
    if day < 1 or day > 31:
        return False
    birth_year = year + 1900 if year >= 0 and year <= 99 else year + 2000
    today = datetime.datetime.now().date()
    if birth_year > today.year:
        return False
    return True



# 用于选择文件返回路径的函数
def choose_file():

    file_path = filedialog.askopenfilename()

    # 选择到的文件路径在label1中显示。
    label1.config(text=file_path)

    if file_path[-4:] == 'xlsx':
        label3.config(text='状态：已选择正确的文件，请输入身份证所在的列...')
        label3.update()
        button2.config(state='normal')

# go为主程序
def go():

    # 判断是否超期使用
    preset_date = datetime.datetime(2025,1,1)
    current_date = datetime.datetime.now()

    if current_date > preset_date:
        label3.config(text='请联系发哥，程序运行中止!')
        return


    

    # 判断文件是否选择正确
    if label1.cget('text')=='1.请选择需要转换的文件(xlsx)' or label1.cget('text')=='' or label1.cget('text')[-4:] != 'xlsx':
        
        label3.config(text='状态：请选择正确的xlsx文件...')
        label3.update()
        
        return

    # 判断表格的列是否正确，最多2位字母。
    if  not bool(re.match(r"^[a-zA-Z]{1,2}$", entry.get())):

        label3.config(text='状态：请输入正确的列...')
        label3.update()

        return


    # 注意cget函数的用法
    label3.config(text='状态：正在读取文件，请稍候...')
    label3.update()
    workbook = openpyxl.load_workbook(label1.cget('text'))

    worksheet = workbook.active

    # 从第2行开始，到最后一行，因索引的关系，必须要加1
    i_rows = worksheet.max_row + 1

    for i in range(2,i_rows):

        label3.config(text='状态：正在转换' + str(int(i / i_rows * 100)) + '%')
        label3.update()
        # 以下为输入的字母加序号组成如['a1]这样的显示形式
        # 注意entry.get().获取输入框的内容。
        id_tmp = str(worksheet[entry.get() + str(i)].value)

        # print(validate_15_id_number(id_tmp))

        if validate_15_id_number(id_tmp):

            worksheet[entry.get() + str(i)] = up_to_eighteen(id_tmp)

        

        # print(label1.cget('text'))
    
    label3.config(text='状态：正在保存文件，请稍候...')
    label3.update()

    workbook.save('./out.xlsx')

    button2.config(state='disabled')
    
    label3.config(text='状态：处理完成,请查看out.xlsx文件！版权归田阳农商行发哥所有！')

root=tk.Tk()

root.title("半自动身份证号15位转18位")

root.geometry('500x250')

root.resizable(False, False)

# 从这里开始读图
img_data = get_image("title.png")

temp_path = write_temp_file(img_data, ".png")

image = tk.PhotoImage(file=temp_path)
# 从这里结束读图

# img = tk.PhotoImage(file='title.png')
# img = os.path.join(os.path.dirname(os.path.abspath(__file__)), "title.png")

label_title = tk.Label(root,image=image)

label_title.place(x=0,y=0)

label1 = tk.Label(root,text='1.请选择需要转换的文件(xlsx)')

label1.place(x=10,y=50)

button1 = tk.Button(root,text='请选择文件',command=choose_file)

button1.place(x=10,y=80)

# 请选择表格的列字母
label2 = tk.Label(root,text='2.请输入身份证所在的列字母，如在A列，输入:a')

label2.place(x=10,y=120)

entry = tk.Entry(root,width=5)

entry.place(x=10,y=150)

button2 = tk.Button(root,text='开始转换',command=go)

button2.place(x=10,y=180)

label3 = tk.Label(root,text='状态：请选择文件...')
label3.update()

label3.place(x=10,y=220)

label4 = tk.Label(root,text='温馨提示：\n 1.i5、12G内存配置，\n  跑65万条原始表。 \n 2.读取表格和保存表格 \n  花时最多。 \n 3.从开始到出表，共用 \n  了2个小时，内存高度 \n  保持在99%。', \
    justify=tk.LEFT)

label4.place(x=320,y=48)

root.mainloop()

