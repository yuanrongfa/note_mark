'''
这是一个由AI生成的，用installer打包的时候，把png图片打包到exe单文件的代码。
使用的时候，把这几个函数插到相关代码部份，只需要改相对路径的png文件名就可以了。

打包的时候用下面代码:
pyinstaller -F -w -i "a.ico" --onefile --add-binary "title.png;." 窗体测试2.py
'''

import sys
import os
import tempfile
import base64
import tkinter as tk

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

def main():
    root = tk.Tk()
    img_data = get_image("image.png")
    temp_path = write_temp_file(img_data, ".png")
    image = tk.PhotoImage(file=temp_path)
    label = tk.Label(root, image=image)
    label.pack()
    root.mainloop()

if __name__ == '__main__':
    main()