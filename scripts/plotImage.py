import os
import numpy as np
import matplotlib.pyplot as plt

curDir = os.getcwd()
print(curDir)
outFloder = os.path.join(curDir,'OUT_FOLDER')
def delete_files_in_folder(folder_path):
    # 获取文件夹中的所有文件和子文件夹
    for root, dirs, files in os.walk(folder_path):
        # 删除所有文件
        for file in files:
            file_path = os.path.join(root, file)
            os.remove(file_path)
        # 删除所有子文件夹
        for dir in dirs:
            dir_path = os.path.join(root, dir)
            os.rmdir(dir_path)

# 调用函数删除文件夹下的所有文件
delete_files_in_folder('outFloder')
print('delete file')

# 生成随机数据
np.random.seed(0)
x = np.arange(10)
y = np.random.randint(1, 20, size=10)

# 配色方案
colors = plt.cm.viridis(np.linspace(0, 1, len(x)))

# 绘制柱状图
plt.bar(x, y, color=colors)

# 添加标题和标签
plt.title('Random Bar Chart with Nice Colors')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# 显示图形

outPath = os.path.join(outFloder,'test.png')
plt.savefig(outPath)
print('finish')
