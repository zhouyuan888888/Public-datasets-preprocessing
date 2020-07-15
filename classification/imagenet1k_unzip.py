import os
import tarfile
from tqdm import tqdm
def extract(tar_path, target_path):
    tar = tarfile.open(tar_path)
    file_names = tar.getnames()
    for file_name in file_names:
        tar.extract(file_name, target_path)
    tar.close()

tar_dir = "/home/zhouyuan/datasets/imagenet_1k/"

tar_files = os.listdir(tar_dir)

for tar_file in tqdm(tar_files):
        tar_path = tar_dir + tar_file
        target_path = tar_dir + tar_file.split(".")[0]
        extract(tar_path, target_path)
        os.remove(tar_path)
        print("**debug**")