import os
import shutil
filename = "datasets"  # 存放json转化得到的文件夹名称
fileList = os.listdir(filename)
for i in range(len(fileList)):
    # img_source = "datasets/" + fileList[i] + "/img.png"
    mask_source = "datasets/" + fileList[i] + "/label.png"
    # yaml_source = "datasets/" + fileList[i] + "/info.yaml"
    print(mask_source)
    # img_target = "pic/img_{}.png".format(i)
    mask_target = "mask/"+fileList[i]+".png"
    mask_target = mask_target.replace('_json','')
    print(mask_target)
    # yaml_target = "yaml/info_{}.yaml".format(i)

    # shutil.copy(img_source, img_target)
    shutil.copy(mask_source, mask_target)
    # shutil.copy(yaml_source, yaml_target)
