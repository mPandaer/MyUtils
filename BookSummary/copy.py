# 将目标源文件复制到指定目录
import re
import os
import shutil

def copy(src_path,gen_path,type="md"):
    # 把文件搜索出来
    files = os.listdir(src_path)
    md_files = []
    re_str = r'.*\.{}'.format(type)
    md_re = re.compile(re_str)
    for file_name in files:
        if md_re.match(file_name):
            src_file_path = src_path + file_name
            dec_file_path = gen_path + file_name;
            shutil.copyfile(src_file_path,dec_file_path)
    

if __name__ == "__main__":
    src_path = "E:\\doc\\030-MySQL实战45讲\\"
    gen_path = "E:\\doc\\books\\my-firstbook\\src\\"
    copy(src_path,gen_path)
    print("复制成功")
