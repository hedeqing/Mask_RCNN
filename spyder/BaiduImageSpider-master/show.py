
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np

import os
import shutil
filename = "orig_mask"  # 存放json转化得到的文件夹名称
fileList = os.listdir(filename)
target_dir = "deal_mask"
for i in fileList:
    print(i)
    img= Image.open("orig_mask"+"\\"+i)
    img = Image.fromarray((np.uint8(img)*50))
    img.save(target_dir+"\\"+i)
    # mask_source = "datasets/" + fileList[i] + "/label.png"
    # img = Image.open('orig_mask/label_0.png')
    # img = Image.fromarray(np.uint8(img)*50)
    # img.save("")
