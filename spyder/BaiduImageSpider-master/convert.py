import os
path = r'C:\Users\hedeqing\Desktop\Homework\datasets\animals\BaiduImageSpider-master\all\json'  # path为json文件存放的路径
json_file = os.listdir(path)
os.system("activate labelme") # 博主labelme所在的环境名就叫labelme，读者应修改成activate [自己labelme所在的环境名]
for file in json_file:
    os.system("python D:\Anaconda\envs\labelme\Scripts/labelme_json_to_dataset.exe %s" % (path + '/' + file))

