import os
import argparse
import sys
import numpy as np
import shutil


parse = argparse.ArgumentParser()
parse.add_argument("-d", "--data_path", required=True, help="data_path")
parse.add_argument("-t", "--save_path", required=True, help="path to save train file")
parse.add_argument("-v", "--val_path", required=True, help="path to save val file")
parse.add_argument("--img_suf", default='images')
parse.add_argument("--lab_suf", default="labels")
parse.add_argument("--img_ext", default="jpg")
parse.add_argument("--lab_ext", default="png")
args = parse.parse_args()


path = os.path.abspath(args.data_path)

img_path = os.path.join(path, args.img_suf)
label_path = os.path.join(path, args.lab_suf)

save_image_path = os.path.join(args.save_path, args.img_suf)
save_label_path = os.path.join(args.save_path, args.lab_suf)
if not os.path.exists(save_image_path):
    os.makedirs(save_image_path)
if not os.path.exists(save_label_path):
    os.makedirs(save_label_path)

val_image_path = os.path.join(args.val_path, args.img_suf)
val_label_path = os.path.join(args.val_path, args.lab_suf)
if not os.path.exists(val_image_path):
    os.makedirs(val_image_path)
if not os.path.exists(val_label_path):
    os.makedirs(val_label_path)


imgs = os.listdir(img_path)
labels = os.listdir(label_path)

# 随机取出10%的数据作为测试集
val_imgs = np.random.choice(imgs, size=int(len(imgs) * 0.4), replace=False)

for i in imgs:
    cur_image_path = os.path.join(img_path, i)
    cur_label_path = cur_image_path.replace(args.img_suf, args.lab_suf).replace(args.img_ext, args.lab_ext)
    if i not in val_imgs:  
        print(cur_image_path)
        print(cur_label_path)
        shutil.copy(cur_image_path, save_image_path)
        shutil.copy(cur_label_path, save_label_path)
    else:
        print(cur_image_path)
        print(cur_label_path)
        shutil.copy(cur_image_path, val_image_path)
        shutil.copy(cur_label_path, val_label_path)


# print(path)



