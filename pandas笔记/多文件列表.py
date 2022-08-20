# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import os

path = r'/Users/yuan/list/'


files = os.listdir(path)

for file in files:
    if file[-4:]=='xlsx':
        print('这个文件是:' + path + file)