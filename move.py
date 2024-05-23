import os
import shutil

def move_csv_files(root_dir, dest_dir=None):
    if dest_dir is None:
        dest_dir = root_dir
    # 遍历根目录及其子目录下的所有文件
    for subdir, _, files in os.walk(root_dir):
        for file in files:
            if file.endswith(".csv"):
                # 如果文件名包含下划线 _
                if '_' in file:
                    # 去掉文件扩展名
                    file_name = os.path.splitext(file)[0]
                    # 使用下划线分隔文件名，创建新目录结构
                    new_path = os.path.join(root_dir, *file_name.split('_')) + ".csv"
                    new_dir = os.path.dirname(new_path)
                    # 创建新目录
                    os.makedirs(new_dir, exist_ok=True)
                    # 移动文件
                    shutil.move(os.path.join(subdir, file), new_path)

# 示例调用
root_directory = "./data"
move_csv_files(root_directory)
