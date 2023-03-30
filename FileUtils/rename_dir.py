# coding = utf-8
"""
此脚本主要用于格式化一个目录下的全部文件的名字，达成规范化的目的 可以递归重命名
"""
import os


def rename(path, src_name=None, new_name=None):
    df_list = os.listdir(path)
    for file in df_list:
        child_path = path + os.sep + file
        if os.path.isdir(child_path):
            rename(child_path, src_name, new_name)
        os.rename(child_path, child_path.replace(src_name, new_name))


if __name__ == '__main__':
    # url = "E:\\doc\\030-MySQL实战45讲"
    url = "/Users/mac/Documents"
    rename(url, src_name="【海量资源：666java.com】", new_name="")

