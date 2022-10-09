import random
import os
from tqdm import tqdm
import shutil 

# random.sample(seq, k)实现从序列或集合seq中随机选取k个独立的的元素

random.seed(100)

# 整个数据集划分比例
train_percent=0.8
val_percent=0.2

src_path = 'D:/hj/human-detection'
dst_path = 'D:/hj/human-detection/nanodet-data'

items = {'images':'.jpg', 'labels':'.txt'}

img_list = os.listdir(f'{src_path}/images')
random.shuffle(img_list) #shuffle
total_num=len(img_list)
index_list=range(total_num)

trainval_index_list = random.sample(index_list, int(total_num*(train_percent+val_percent))) # 训练集和验证集一起
train_index_list=random.sample(trainval_index_list, int(len(trainval_index_list)*(train_percent/(train_percent+val_percent)))) # 单独的训练集

for item, ext in items.items():
    train_dir=f'{dst_path}/train/{item}'
    val_dir=f'{dst_path}/val/{item}'
    test_dir=f'{dst_path}/test/{item}'

    if not os.path.exists(train_dir):
        os.makedirs(train_dir)
    if not os.path.exists(val_dir):
        os.makedirs(val_dir)
    if not os.path.exists(test_dir):
        os.makedirs(test_dir)

    for i,name in tqdm(enumerate(img_list)):
        n = os.path.splitext(name)
        file_name = n[0] + ext
        full_name = os.path.join(f'{src_path}/{item}',file_name)
        if not os.path.exists(full_name):
            continue
        if i in trainval_index_list:
            if i in train_index_list:
                shutil.copy(full_name, train_dir)
            else:
                shutil.copy(full_name, val_dir)
        else:
            shutil.copy(full_name, test_dir)
        # print(f'{i} coping {full_name}')